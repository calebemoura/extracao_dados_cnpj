from databricks.sdk.runtime import dbutils

import sys
workspace = dbutils.widgets.get('workspace')
sys.path.insert(0, f"{workspace}scr/")

from schemas.log_schema import logs_extracao

def create_table(spark, catalog: str, schema:str, table: str = 'log_extracao'):
    struct = logs_extracao.jsonValue()
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
