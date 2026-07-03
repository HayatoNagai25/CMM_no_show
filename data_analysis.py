import pandas as pd
from data_extraction import load_data

df = load_data("data/df2023-2026_anon.csv")

duplicate_cols = [val for val in df.columns.tolist() if ".1" in val]
df = df.drop(duplicate_cols, axis=1)

trivial_cols = ["AMB_ESTADO_HORA", "Cantidad", "AMB_NOMBRE_LUGAR", "AMB_NRO_BOX", "AMB_PROCEDIMIENTO",
                "AMB_TIPO_HORA", "AMB_SOBRECUPO", "AMB_USUARIO_SOBRECUPO", "AMB_FECHA_SOBRECUPO",
                "AMB_HORA_SOBRECUPO", "AMB_FEC_CREACION", "Glosa_Prestación", "Prevision"]
df = df.drop(trivial_cols, axis=1)

redundant_cols = ["AG_HORA_ATEN", "nom_institucion", "AMB_COD_ESPECI", "AMB_COD_SUBESP",
                    "AMB_COD_LUGAR", "AMB_COD_CENTRO", "CodigoComuna", "cod_prestacion",
                    "Glosa_Ed", "Día_Ingreso", "AMB_MODALIDAD_ATENCION", "nom_especialidad",
                    "Día_ATEN", "AMB_HORA_CITA"]
df = df.drop(redundant_cols, axis=1)

df.rename(columns={"AG_AMB_FECHA_CITA": "Appointment Date", "AG_HORA_CITA": "Appointment Time",
                    "VER": "Attendance Status", "AG_AMB_FECHA_ATEN": "Visit Date",
                    "Mes_Ingreso": "Month of Entry", "AMB_DESC_ESPECI": "Speciality Description",
                    "AMB_DESC_SUBESP": "Subspeciality Description","Nacionalidad": "Nationality",
                    "FEC_NACIMIENTO": "Birthdate", "Sexo": "Sex", "Comuna": "Municipality",
                    "Edad_fecha_aten": "Age at Visit Date", "AMB_NOMBRE_C": "Medical Center Name",
                    "AMB_TIPO_ATENCION": "Type of Visit", "AMB_HORA_LLEGADA": "Arrival Time",
                    "Año_Ingreso": "Year of Entry", "new_id": "New ID"}, inplace=True)

df["Attendance Status"] = (df["Attendance Status"] == "NSP").astype(int)

ct = pd.crosstab(df["Speciality Description"], df["Subspeciality Description"], df["Attendance Status"], margins=True)

print(ct)
