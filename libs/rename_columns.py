from pyspark.sql.types import StructType, StructField, StringType
from typing import Dict

def columns(table: str) -> Dict[str, str]:
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
    '_c4': 'matriz_filial',
    '_c5': 'nome_fantasia',
    '_c6': 'situaçao_cadastral',
    '_c7': 'data_situacao_cadastral',
    '_c8': 'motivo_situacao_cadastral',
    '_c9': 'cidade_exterior',
    '_c10': 'pais',
    '_c11': 'inicio_atividade',
    '_c12': 'cnae_fiscal_principal',
    '_c13': 'cnae_fiscal_secundaria',
    '_c14': 'tipo_logradouro',
    '_c15': 'logradouro',
    '_c16': 'numero',
    '_c17': 'complemento',
    '_c18': 'bairro',
    '_c19': 'cep',
    '_c20': 'uf',
    '_c21': 'municipio',
    '_c22': 'ddd_1',
    '_c23': 'telefone_1',
    '_c24': 'ddd_2',
    '_c25': "telefone_2",
    '_c26': "ddd_fax",
    '_c27': 'fax',
    '_c28': 'correio_eletronico',
    '_c29': 'situacao_especial',
    '_c30': 'data_situacao'
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
    '_c1': 'identificador_sócio',
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

  variables = vars()

  for chave, valor in variables.items():
    if chave == table:
        dict_columns = valor

  return dict_columns
