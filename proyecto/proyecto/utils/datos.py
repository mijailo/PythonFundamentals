from pandas import DataFrame, read_csv, concat


RUTA_DATOS = 'proyecto/data/'

def leer_datos(fuente):
    
    ruta = f"{RUTA_DATOS}{fuente}.csv"
    
    datos = read_csv(ruta)
    
    datos.set_index('nombre', inplace=True)

    datos.drop(['cve_ent', 'poblacion'], axis=1, inplace=True)
    
    datos.drop(['Nacional'], axis=0, inplace=True)
    
    registros = datos.sum(axis=1)
    
    registros.name = fuente
    
    registros = DataFrame(registros)
    
    return registros.reset_index()


def datos_totales():

    ruta = f"{RUTA_DATOS}totales.csv"
    
    return read_csv(ruta, index_col=0)

    