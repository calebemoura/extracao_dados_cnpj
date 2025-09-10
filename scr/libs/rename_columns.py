from pyspark.sql.types import StructType, StructField, StringType

empresas = {
  '_c0': 'cnpj_basico',
  '_c1': 'razao_social',
  '_c2': 'natureza_juridica',
  '_c3': 'qualificacao_responsavel',
  '_c4': 'capital_social',
  '_c5': 'porte',
  '_c6': 'ente_federativo' 
}

estabelecimentos = {
  '_c0': 'cnpj_basico',
  '_c1': 'cnpj_ordem',
  '_c2': 'cnpj_dv',
  '_c3': 'identificador',
  '_c4': 'nome_fantasia',
  '_c5': 'situacao_cadastral',
  '_c6': 'data_situacao_cadastral',
  '_c7': 'motivo_situacao_cadastral',
  '_c8': 'cidade_exterior',
  '_c9': 'pais',
  '_c10': 'inicio_atividade',
  '_c11': 'cnae_fiscal_principal',
  '_c12': 'cnae_fiscal_secundaria',
  '_c13': 'tipo_logradouro',
  '_c14': 'logradouro',
  '_c15': 'numero',
  '_c16': 'complemento',
  '_c17': 'bairro',
  '_c18': 'cep',
  '_c19': 'uf',
  '_c20': 'municipio',
  '_c21': 'ddd_1',
  '_c22': 'telefone_1',
  '_c23': 'ddd_2',
  '_c24': "telefone_2",
  '_c25': "ddd_fax",
  '_c26': 'fax',
  '_c27': 'correio_eletronico',
  '_c28': 'situacao_especial',
  '_c29': 'data_situacao_especial'
}

simples = {
  '_c0': 'cnpj_basico',
  '_c1': 'opcao_pelo_simples',
  '_c2': 'data_opcao_pelo_simples',
  '_c3': 'data_exclusao_simples',
  '_c4': 'opcao_pelo_mei',
  '_c5': 'data_opcao_pelo_mei',
  '_c6': 'data_exclusao_mei'
}

socios = {
  '_c0': 'cnpj_basico',
  '_c1': 'identificador_socio',
  '_c2': 'nome_socio',
  '_c3': 'cnpj_cpf_socio',
  '_c4': 'qualificacao_socio',
  '_c5': 'data_entrada',
  '_c6': 'pais',
  '_c7': 'representante_legal',
  '_c8': 'nome_representante',
  '_c9': 'qualificacao_representante',
  '_c10': 'faixa_etaria'
}

cnaes = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}

paises = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}

municipios = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}

qualificacoes = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}

naturezas = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}

motivos = {
  '_c0': 'codigo',
  '_c1': 'descricao'
}
