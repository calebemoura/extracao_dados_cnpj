from pyspark.sql.types import StructType

def valida_schema(schema_1: StructType, schema_2: StructType):
    """
        Esta função compara dois schemas e verifica se: 
            -> os tipos de dados são iguais.
            -> Quantidades de colunas estão iguais e qual está faltando
        Ela toma como referência o schema 1 em comparação com o schema 2
    """
    schema1 = schema_1
    schema2 = schema_2

    num_colunas = len(schema1) == len(schema2)
    zip_schemas = zip(schema1, schema2)

    # Valida a quantidade de colunas, e se faltar alguma, mostra a que falta
    if not num_colunas:
        c1 = set(schema1.names)
        c2 = set(schema2.names)
        raise ValueError(f" A coluna {c1.symmetric_difference(c2)} da tabela da bronze não consta no schema da tabela silver.")


    # Verificar o tipo dos dados
    for campo_schema_1, campo_schema_2 in zip_schemas:
        if campo_schema_1.dataType != campo_schema_2.dataType:
            raise ValueError(f"O tipo de dados do primeiro schema '{campo_schema_1.name.upper()}' espera um {campo_schema_1.dataType} mas o segundo schema está como {campo_schema_2.dataType}.")