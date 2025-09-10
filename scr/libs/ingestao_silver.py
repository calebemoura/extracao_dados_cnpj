import sys
workspace = dbutils.widgets.get('workspace')
sys.path.insert(0, workspace)

import schemas.silver_schema as s
from libs.create_silver_table import create_table
from libs.valida_schemas import valida_schema

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

def ingestao_silver(
    spark: SparkSession, 
    df: DataFrame, 
    catalog: str, 
    table: str
):
    create_table(
        spark=spark,
        catalog = catalog,
        schema = 'silver',
        table = table
    )

    df_insert = df
    schema_insert = df.schema
    schema_padrao = eval(f"s.{table}")

    try:
        valida_schema(schema_padrao, schema_insert)
        df_insert.write \
            .format('delta') \
            .mode('overwrite') \
            .saveAsTable(f"{catalog}.silver.{table}")
    except Exception as e:
        print(e)