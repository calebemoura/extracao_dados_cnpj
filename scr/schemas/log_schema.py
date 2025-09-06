from pyspark.sql.types import StructType, StructField, StringType, TimestampType

logs_extracao = StructType([
    StructField('codigo', StringType(), False,
                metadata = {'coment': 'Pasta dos dados que foram baixados no site do gov'}
            ),
    StructField('inicio', TimestampType(), False,
                metadata = {'coment': 'Data e hora que iniciou o processo de extracao'}
            ),
    StructField('fim', TimestampType(), False, 
                {'coment': 'Data e hora que terminou o processo de extracao'}
            ),
    StructField('descricao', StringType(), True,
                metadata = {'coment':'Descrição do processo'}
            ),
    StructField('observacao', StringType(), True,
                metadata = {'coment':'Descrição de informações adicionais importantes para consideração'}
            ) 
])