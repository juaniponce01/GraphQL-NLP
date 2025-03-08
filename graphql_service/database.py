import pandas as pd

def load_data():
    return pd.read_csv("data.csv")

df = load_data()

# eliminamos columnas con todos los valores nulos
df.dropna(axis=1, how='all', inplace=True)

# eliminamos columnas que no aportan nueva información
df.drop(columns=["desc_ga_sku_producto_1", "SASASA"], inplace=True)

column_rename = {
    "id_tie_fecha_valor": "fecha",
    "id_cli_cliente": "id_cliente",
    "id_ga_vista": "id_vista",
    "id_ga_tipo_dispositivo": "id_tipo_dispositivo",
    "id_ga_fuente_medio": "id_fuente_medio",
    "desc_ga_sku_producto": "sku_producto",
    "fc_agregado_carrito_cant": "agregado_carrito_cant",
    "fc_ingreso_producto_monto": "ingreso_producto_monto",
    "fc_detalle_producto_cant": "detalle_producto_cant",
    "fc_producto_cant": "producto_cant",
    "id_ga_producto": "id_producto",
    "desc_ga_nombre_producto_1": "nombre_producto",
    "desc_ga_marca_producto": "marca_producto",
    "desc_ga_cod_producto": "cod_producto",
    "desc_categoria_producto": "categoria_producto",
    "desc_categoria_prod_principal": "categoria_prod_principal",
}

# renombramos columnas para mantener legibilidad
df.rename(columns=column_rename, inplace=True)

# convertimos la columna fecha a tipo datetime para poder filtrar por fecha
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y%m%d').dt.date

# convertimos valores NaN a None porque GraphQL no puede operar con NaNs
df = df.applymap(lambda x: None if pd.isna(x) else x)
