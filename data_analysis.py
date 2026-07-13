import pandas as pd
from data_extraction import load_data, simplify_data, linear_data, tree_data
from create_models import split_data

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



# extracts data for both lienar and tree models
linear_x, y = linear_data(simplify_data(load_data("data/df2023-2026_anon.csv")))
tree_x, y = tree_data(simplify_data(load_data("data/df2023-2026_anon.csv")))

# split both data types
train_linear_x, test_linear_x, train_linear_y, test_linear_y = split_data(linear_x, y)
train_tree_x, test_tree_x, train_tree_y,  test_tree_y = split_data(tree_x, y)

print(train_linear_x.isna().sum().sum())
print(train_tree_x.isna().sum().sum())
print(train_tree_x.isna().sum()[train_tree_x.isna().sum() > 0])
