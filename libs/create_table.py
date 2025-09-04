from schemas.bronze_schemas import *

def create_table(catalog: str, schema: str, table: str, spark):
    struct = eval(table).jsonValue()
    column_type = ''

    # Verifica se a tabela existe
    count = (spark.sql(f"SHOW TABLES FROM {catalog}.{schema}")
         .where(f"database = '{schema}' AND tableName = '{table}'")         
    ).count()

    if count > 0:
        print('Tabela já existe')
    else:
        for v, k in struct.items():
            if v == 'fields':
                for i in k:
                    column_type += f"{i['name']} {i['type'].upper()} COMMENT '{i['metadata']['coment'].capitalize()}', "

        sql_comand = f"""
            CREATE TABLE IF NOT EXISTS {catalog}.{schema}.{table} (
                {column_type[: -2]})
            USING DELTA
            TBLPROPERTIES (
            'delta.autoOptimize.optimizeWrite' = 'true',
            'delta.autoOptimize.autoCompact' = 'true',
            'delta.enableChangeDataFeed' = 'true'
        )
        """
        spark.sql(sql_comand)
        print('Tabela criada com sucesso')
