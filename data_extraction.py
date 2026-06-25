import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

def load_data(file_path):
    """
    Loads the CSV file and returns its contents in the form of a DataFrame

    file_path: path to the csv file

    Returns: a DataFrame
    """
    return pd.read_csv(file_path)


def simplify_data(df):
    """
    Removes unnecessary data and reduces data from 51 to 17 categories

    df: a DataFrame

    Returns: a DataFrame
    """
    # remove all 4 repeated columns
    duplicate_cols = [val for val in df.columns.tolist() if ".1" in val]
    df = df.drop(duplicate_cols, axis = 1)

    # remove all 12 columns with trivial information
    trivial_cols = ["AMB_ESTADO_HORA", "Cantidad", "AMB_NOMBRE_LUGAR", "AMB_NRO_BOX",
                    "AMB_PROCEDIMIENTO", "AMB_TIPO_HORA", "Año_Ingreso", "AMB_SOBRECUPO",
                    "AMB_USUARIO_SOBRECUPO", "AMB_FECHA_SOBRECUPO", "AMB_HORA_SOBRECUPO",
                    "AMB_FEC_CREACION"]
    df = df.drop(trivial_cols, axis = 1)

    # remove all 14 columns with redundant information
    redundant_cols = ["AG_HORA_ATEN", "nom_institucion", "AMB_COD_ESPECI", "AMB_COD_SUBESP",
                      "AMB_COD_LUGAR", "AMB_COD_CENTRO", "CodigoComuna", "cod_prestacion",
                      "Glosa_Ed", "Día_Ingreso", "AMB_MODALIDAD_ATENCION", "nom_especialidad",
                      "Día_ATEN", "AMB_HORA_CITA"]
    df = df.drop(redundant_cols, axis = 1)

    # rename all all the remaining 18 columns with their english translation
    df.rename(columns={"AG_AMB_FECHA_CITA": "Appointment Date", "AG_HORA_CITA": "Appointment Time",
                       "VER": "Attendance Status", "AG_AMB_FECHA_ATEN": "Visit Date",
                       "Mes_Ingreso": "Month of Entry", "AMB_DESC_ESPECI": "Speciality Description",
                       "AMB_DESC_SUBESP": "Subspeciality Description","Nacionalidad": "Nationality",
                       "FEC_NACIMIENTO": "Birthdate", "Sexo": "Sex", "Comuna": "Municipality",
                       "Prevision": "Insurance", "Edad_fecha_aten": "Age at Visit Date",
                       "Glosa_Prestación": "Procedure Description",
                       "AMB_NOMBRE_C": "Medical Center Name", "AMB_TIPO_ATENCION": "Type of Visit",
                       "AMB_HORA_LLEGADA": "Arrival Time", "new_id": "New ID"}, inplace=True)

    # removes any row where appointment date is after visit date (useful later on)
    df["Appointment Date"] = pd.to_datetime(df["Appointment Date"], format="%d/%m/%Y")
    df["Visit Date"] = pd.to_datetime(df["Visit Date"], format="%d/%m/%Y")
    df = df[df["Visit Date"] >= df["Appointment Date"]]
    df["Appointment Date"] = df["Appointment Date"].dt.strftime("%d/%m/%Y")
    df["Visit Date"] = df["Visit Date"].dt.strftime("%d/%m/%Y")

    return df


def linear_data(df):
    """
    Processes data into Variables of Interest for a linear regression model

    df: a DataFrame

    Returns: (df, attendance_status)
        df is the modified DataFrame and attendance_status is the numerical
        representation of the attendance status of each appointment
    """
    # encode appointment time, arrival time, and month of entry
    df["Appointment Time"], df["Arrival Time"], df["Month of Entry"] = encode_times_month(df["Appointment Time"], df["Arrival Time"], df["Month of Entry"])

    # shorten larger categories into 20 unique categories and an OTHER category
    large_categories = ["Speciality Description", "Subspeciality Description",
                        "Municipality", "Procedure Description"]
    for category in large_categories:
        top_n = df[category].value_counts().index[:20]
        df[category] = df[category].where(df[category].isin(top_n), "OTHER")

    # save appointment status into a different variable
    attendance_status = (df["Attendance Status"] == "NSP").astype(int)

    # create categories for no-show records, late arrival records, date of the week, and time interval
    df["Previous No-Show"] = previous_no_show(attendance_status, df["Visit Date"], df["New ID"])
    df["Previous Late Arrival"] = previously_late(df["Arrival Time"], df["Appointment Time"], df["Visit Date"], df["New ID"])
    df["Day of the Week"] = day_of_the_week(df["Visit Date"])
    df["Time Interval"] = time_interval(df["Appointment Date"], df["Visit Date"])

    # categorize intervals into numbers for time, age, and time interval (only for linear regression model)
    df["Time"] = pd.cut(df["Appointment Time"],
                        bins=[0, 420, 540, 720, 1020, np.inf],
                        labels=["Night", "Early Morning", "Morning", "Afternoon", "Evening"],
                        include_lowest=True).astype(str)
    df["Age"] = pd.cut(df["Age at Visit Date"],
                       bins=[0, 17, 30, 59, 79, np.inf],
                       labels=["Child", "Young Adult", "Adult", "Senior", "Elderly"],
                       include_lowest=True).astype(str)
    df["Time Interval"] = pd.cut(df["Time Interval"],
                                 bins=[-1, 0, 10, 50, np.inf],
                                 labels=["Same Day", "Short", "Medium", "Long"]).astype(str)

    # remove the 8 columns that won't be used
    used_cols = ["Appointment Date", "Appointment Time", "Attendance Status", "Visit Date",
                 "Birthdate", "Age at Visit Date", "Arrival Time", "New ID"]
    df = df.drop(used_cols, axis = 1)

    # use one-hot encoding to convert strings to ints
    df = pd.get_dummies(df)

    return df, attendance_status


def tree_data(df):
    """
    Processes data into Variables of Interest for tree-based models

    df: a DataFrame

    Returns: (df, attendance_status)
        df is the modified DataFrame and attendance_status is the numerical
        representation of the attendance status of each appointment)
    """
    # encode appointment time, arrival time, and month of entry
    df["Appointment Time"], df["Arrival Time"], df["Month of Entry"] = encode_times_month(df["Appointment Time"], df["Arrival Time"], df["Month of Entry"])

    # shorten larger categories into 20 unique categories and an OTHER category
    large_categories = ["Speciality Description", "Subspeciality Description",
                        "Municipality", "Procedure Description"]
    for category in large_categories:
        n = df[category].value_counts().index[:20]
        df[category] = df[category].where(df[category].isin(n), "OTHER")

    # save appointment status into a different variable
    attendance_status = (df["Attendance Status"] == "NSP").astype(int)

    # create categories for no-show records, late arrival records, day of the week, and time interval
    df["Previous No-Show"] = previous_no_show(attendance_status, df["Visit Date"], df["New ID"])
    df["Previous Late Arrival"] = previously_late(df["Arrival Time"], df["Appointment Time"], df["Visit Date"], df["New ID"])
    df["Day of the Week"] = day_of_the_week(df["Visit Date"])
    df["Time Interval"] = time_interval(df["Appointment Date"], df["Visit Date"])

    # simply rename time and age for tree-based models
    df["Time"] = df["Appointment Time"]
    df["Age"] = df["Age at Visit Date"]

    # remove the 8 columns that won't be used
    used_cols = ["Appointment Date", "Appointment Time", "Attendance Status", "Visit Date",
                 "Birthdate", "Age at Visit Date", "Arrival Time", "New ID"]
    df = df.drop(used_cols, axis = 1)

    # use ordinal encoding to convert strings to ints
    categories = ["Speciality Description", "Subspeciality Description", "Nationality", "Sex", "Municipality",
                  "Day of the Week", "Insurance", "Procedure Description", "Medical Center Name", "Type of Visit"]
    encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    df[categories] = encoder.fit_transform(df[categories])

    return df, attendance_status


#######################################################################################################
########################################## HELPER FUNCTIONS ###########################################
#######################################################################################################


def previous_no_show(attendance, visit_date, id):
    """
    Uses attendance status and the pseudo ids to track and
    construct a series for previous records of no show

    Params:
        attendance: a Series
        visit_date: a Series
        id: a Series

    Returns: a Series of a previous no show record
    """
    # creates a new temporary DataFrame that holds the ID, Date, and Attendance Status sorted by Date and ID
    sorted_order = pd.DataFrame({"ID": id, "Date": visit_date, "Attendance": attendance}).sort_values(["ID", "Date"])

    # creates a no show column that counts the previous number of no shows
    no_show = sorted_order["Attendance"].groupby(sorted_order["ID"]).cumsum().groupby(sorted_order["ID"]).shift(1)

    # fills in the NaN that resulted from shift 1 with 0s
    no_show = no_show.fillna(0).astype(int)

    # sorts back by index
    no_show = no_show.sort_index()

    return no_show


def previously_late(arrival_time, appointment_time, visit_date, id):
    """
    Uses arrival time, appontment time, and ids to track and
    construct a series for previous records of lateness
    (measured if more than 5 minutes late to the appointment)

    Params:
        arrival_time: a Series
        appointment_time: a Series
        visit_date: a Series
        id: a Series

    Returns: a Series of a previously late record
    """
    # creates a temporary column of 1 and 0 if the patient was late to the appointment
    was_late = np.where((arrival_time != -1) & (arrival_time > appointment_time + 15), 1, 0)

    # converts NumPy Array into a Pandas Series
    was_late = pd.Series(was_late, index=appointment_time.index)

    # creates a new temporary DataFrame that holds the ID, Date, and Late Record sorted by Date and ID
    sorted_order = pd.DataFrame({"ID": id, "Date": visit_date, "Late": was_late}).sort_values(["ID", "Date"])

    # creates a late column that counts the previous number of late arrivals
    late = sorted_order["Late"].groupby(sorted_order["ID"]).cumsum().groupby(sorted_order["ID"]).shift(1)

    # fills in the NaN that resulted from shift 1 with 0s
    late = late.fillna(0).astype(int)

    # sorts back by index
    late = late.sort_index()

    return late


def day_of_the_week(visit_date):
    """
    Uses appointment date to construct a series for the day of the week

    visit_date: a Series

    Returns: a Series of the day of the week
    """
    # converts the appointment into a numerical date and calculates the day of the week
    date = pd.to_datetime(visit_date, format="%d/%m/%Y")
    day = date.dt.dayofweek

    return day


def encode_times_month(appointment_time, arrival_time, month_of_entry):
    """
    Encodes appointment time, arrival time, and month of entry

    Params:
        appointment_time: a Series
        arrival_time: a Series
        month_of_entry: a Series

    Returns: (app_time, arr_time, month)
        app_time, arr_time, and month are all Series of appointment
        time, arrival time, and month encoded
    """
    # encode appointment time
    t1 = pd.to_datetime(appointment_time, format="%H:%M:%S", errors="coerce")
    app_time = (t1.dt.hour * 60 + t1.dt.minute).fillna(-1).astype(int)

    # encode arrival time
    t2 = pd.to_datetime(arrival_time, format="%d-%m-%Y %H:%M:%S.%f", errors="coerce")
    arr_time = (t2.dt.hour * 60 + t2.dt.minute).fillna(-1).astype(int)

    # encode month of entry
    month_map = {"ENERO": 1, "FEBRERO": 2, "MARZO": 3, "ABRIL": 4,
                 "MAYO": 5, "JUNIO": 6, "JULIO": 7, "AGOSTO": 8,
                 "SEPTIEMBRE": 9, "OCTUBRE": 10, "NOVIEMBRE": 11, "DICIEMBRE": 12}
    month = month_of_entry.map(month_map)

    return app_time, arr_time, month


def time_interval(appointment_date, visit_date):
    """
    Uses appointment date and visit date to determine the
    time interval between the date the appointment was
    booked and the actual date of the appointment, in days

    Params:
        appointment_date: a Series
        visit_date: a Series

    Returns: a Series of the time interval between booking and visit date
    """
    # converts the appointment date and visit date into a pandas date time
    app_date = pd.to_datetime(appointment_date, format="%d/%m/%Y")
    vis_date = pd.to_datetime(visit_date, format="%d/%m/%Y")

    # finds the interval between the visit date and the appointment date
    interval = (vis_date - app_date).dt.days

    return interval


if __name__ == "__main__":
    df1, attendance1 = linear_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
    df2, attendance2 = tree_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
    check_list_1 = df1.columns.tolist()
    check_list_2 = df2.columns.tolist()
    print(check_list_1)
    print()
    print(attendance1)
    print()
    print(check_list_2)
    print()
    print(attendance2)
    pass
