"""
    1 para os intervalos entre 0 a 12 anos;
    2 para os intervalos entre 13 a 20 anos;
    3 para os intervalos entre 21 a 30 anos;
    4 para os intervalos entre 31 a 40 anos;
    5 para os intervalos entre 41 a 50 anos;
    6 para os intervalos entre 51 a 60 anos;
    7 para os intervalos entre 61 a 70 anos;
    8 para os intervalos entre 71 a 80 anos;
    9 para maiores de 80 anos.
    0 para não se aplica. 
"""

# Criando a tabela
spark.sql(
    """
        CREATE TABLE projeto_cnpj.silver.faixa_etaria(
            codigo INT NOT NULL COMMENT ' Código da faixa etária',
            descricao STRING NOT NULL COMMENT 'Descrição faixa etária'
        )
        USING DELTA
            TBLPROPERTIES (
            'delta.autoOptimize.optimizeWrite' = 'true',
            'delta.autoOptimize.autoCompact' = 'true',
            'delta.enableChangeDataFeed' = 'true'
        )
    """
)

# Inserindo os dados
spark.sql(
    """
        INSERT INTO projeto_cnpj.silver.faixa_etaria
        VALUES
            (1, '0 a 12 anos'),
            (2, '13 a 20 anos'),
            (3, '21 a 30 anos'),
            (4, '31 a 40 anos'),
            (5, '41 a 50 anos'),
            (6, '51 a 60 anos'),
            (7, '61 a 70 anos'),
            (8, '71 a 80 anos'),
            (9, 'maiores de 80 anos'),
            (0, 'não se aplica')
    """
)