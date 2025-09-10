from pyspark.sql.types import StructType, StructField, StringType, FloatType, DateType, IntegerType

empresas = StructType([
    StructField('cnpj_basico', StringType(), nullable=False,
                metadata = {'coment': 'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('razao_social', StringType(), nullable=True,
                metadata = {'coment': 'nome empresarial da pessoa jurídica'}
            ),
    StructField('natureza_juridica', IntegerType(), nullable=False, 
                metadata={'coment': 'código da natureza jurídica'}
            ),
    StructField('qualificacao_responsavel', IntegerType(), nullable=True,
                metadata = {'coment': 'qualificação da pessoa física responsável pela empresa'}
            ),
    StructField('capital_social', FloatType(), nullable=True,
                metadata = {'coment': 'capital social da empresa'}
            ),
    StructField('porte', StringType(), nullable=True,
                metadata = {'coment': 'código do porte da empresa: 00 – não informado 01 - micro empresa 03 - empresa de pequeno porte 05 - demais'}
            ),
    StructField('ente_federativo', StringType(), nullable=True,
                metadata = {'coment': 'o ente federativo responsável é preenchido para os casos de órgãos e entidades do grupo de natureza jurídica 1xxx. para as demais naturezas, este atributo fica em branco.'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
                metadata = {'coment': 'Data que o arquivo foi carregado'}
            )
])

estabelecimentos = StructType([
    StructField('cnpj_basico', StringType(), nullable=False, 
                metadata={'coment':'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('cnpj_ordem', StringType(), nullable=False, 
                metadata={'coment':'número do estabelecimento de inscrição no cnpj (do nono até o décimo segundo dígito do cnpj)'}
                ),
    StructField('cnpj_dv', StringType(), nullable=False, 
                metadata={'coment': 'dígito verificador do número de inscrição no cnpj (dois últimos dígitos do cnpj).'}
                ),
    StructField('identificador', StringType(), nullable=False,
                metadata={'coment': 'código do identificador matriz/filial: 1–matriz, 2–filial'}
            ),
    StructField('nome_fantasia', StringType(), nullable=True,
                metadata={'coment': 'corresponde ao nome fantasia'}
            ),
    StructField('situacao_cadastral', StringType(), nullable=True, 
                metadata={'coment': 'corresponde ao nome fantasia código da situação cadastral: 01–nula, 02–ativa, 03–suspensa, 08–baixada'}
            ),
    StructField('data_situacao_cadastral', DateType(), nullable=True, 
                metadata={'coment': 'data do evento da situação cadastral'}
            ),
    StructField('motivo_situacao_cadastral', IntegerType(), nullable=True, 
                metadata={'coment': 'código do motivo da situação cadastral'}
            ),
    StructField('cidade_exterior', StringType(), nullable=True, 
                metadata={'coment': 'nome da cidade no exterior'}
            ),
    StructField('pais', IntegerType(), nullable=True, 
                metadata={'coment': 'código do pais'}
            ),
    StructField('inicio_atividade', DateType(), nullable=True, 
                metadata={'coment': 'Data do inicio da atividade'}
            ),
    StructField('cnae_fiscal_principal', IntegerType(), nullable=True, 
                metadata={'coment': 'código da atividade econômica principal do estabelecimento'}
            ),
    StructField('cnae_fiscal_secundaria', StringType(), nullable=True, 
                metadata={'coment': 'código da(s) atividade(s) econômica(s) secundária(s) do estabelecimento'}
            ),
    StructField('tipo_logradouro', StringType(), nullable=True, 
                metadata={'coment': 'código do tipo de logradouro'}
            ),
    StructField('logradouro', StringType(), nullable=True, 
                metadata={'coment': 'descrição do tipo de logradouro'}
            ),
    StructField('numero', StringType(), nullable=True, 
                metadata={'coment': 'número onde se localiza o estabelecimento. quando não houver preenchimento do número haverá s/n.'}
            ),
    StructField('complemento', StringType(), nullable=True, 
                metadata={'coment': 'complemento para o endereço de localização do estabelecimento'}
            ),
    StructField('bairro', StringType(), nullable=True, 
                metadata={'coment': 'bairro onde se localiza o estabelecimento.'}
            ),
    StructField('cep', StringType(), nullable=True, 
                metadata={'coment': 'código de endereçamento postal referente ao logradouro no qual o estabelecimento esta localizado'}
            ),
    StructField('uf', StringType(), nullable=True, 
                metadata={'coment': 'sigla da unidade da federação em que se encontra o estabelecimento'}
            ),
    StructField('municipio', StringType(), nullable=True, 
                metadata={'coment': 'código do município de jurisdição onde se encontra o estabelecimento'}
            ),
    StructField('ddd_1', StringType(), nullable=True, 
                metadata={'coment': 'contém o ddd 1'}
            ),
    StructField('telefone_1', StringType(), nullable=True, 
                metadata={'coment': 'contém o número do telefone 1'}
            ),
    StructField('ddd_2', StringType(), nullable=True, 
                metadata={'coment': 'contém o ddd 2'}
            ),
    StructField('telefone_2', StringType(), nullable=True, 
                metadata={'coment': 'contém o número do telefone 2'}
            ),
    StructField('ddd_fax', StringType(), nullable=True, 
                metadata={'coment': 'contém o ddd do fax'}
            ),
    StructField('fax', StringType(), nullable=True, 
                metadata={'coment': 'contém o número do fax'}
            ),
    StructField('correio_eletronico', StringType(), nullable=True, 
                metadata={'coment': 'contém o e-mail do contribuinte'}
            ),
    StructField('situacao_especial', StringType(), nullable=True, 
                metadata={'coment': 'situação especial da empresa'}
            ),
    StructField('data_situacao_especial', DateType(), nullable=True, 
                metadata={'coment': 'data em que a empresa entrou em situação especial'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

simples = StructType([
    StructField('cnpj_basico', StringType(), nullable=False, 
                metadata={'coment': 'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('opcao_pelo_simples', StringType(), nullable=False, 
                metadata={'coment': 'indicador da existência da opção pelo simples. s-sim, n-não, em branco–outros data de opção pelo simples'}
            ),
    StructField('data_opcao_pelo_simples', DateType(), nullable=False, 
                metadata={'coment': 'data de exclusão do simples'}
            ),
    StructField('data_exclusao_simples', DateType(), nullable=True, 
                metadata={'coment': 'data de exclusão do simples opção pelo mei'}
            ),
    StructField('opcao_pelo_mei', StringType(), nullable=False, 
                metadata={'coment': 'indicador da existência da opção pelo mei s-sim, n-não, em branco-outros'}
            ),
    StructField('data_opcao_pelo_mei', DateType(), nullable=True, 
                metadata={'coment': 'data de opção pelo mei'}
            ),
    StructField('data_exclusao_mei', DateType(), nullable=True, 
                metadata={'coment': 'data de exclusão do mei'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

socios = StructType([
    StructField('cnpj_basico', StringType(), nullable=False, 
                metadata={'coment': 'número base de inscrição no cnpj (cadastro nacional da pessoa jurídica).'}
            ),
    StructField('identificador_socio', StringType(), nullable=False, 
                metadata={'coment': 'código do identificador de sócio 1–pessoa jurídica, 2–pessoa física, 3–estrangeiro'}
            ),
    StructField('nome_socio', StringType(), nullable=True, 
                metadata={'coment': 'nome do sócio pessoa física ou a razão social e/ou nome empresarial da pessoa jurídica e/ou nome do sócio/razão social do sócio estrangeiro'}
            ),
    StructField('cnpj_cpf_socio', StringType(), nullable=True, 
                metadata={'coment': 'cpf ou cnpj do sócio (sócio estrangeiro não tem esta informação).'}
            ),
    StructField('qualificacao_socio', IntegerType(), nullable=True, 
                metadata={'coment': 'código da qualificação do sócio'}
            ),
    StructField('data_entrada', DateType(), nullable=True, 
                metadata={'coment': 'data de entrada na sociedade'}
            ),
    StructField('pais', StringType(), nullable=True, 
                metadata={'coment': 'código país do sócio estrangeiro'}
            ),
    StructField('representante_legal', StringType(), nullable=True, 
                metadata={'coment': 'número do cpf do representante legal'}
            ),
    StructField('nome_representante', StringType(), nullable=True, 
                metadata={'coment': 'nome do representante legal'}
            ),
    StructField('qualificacao_representante', IntegerType(), nullable=True, 
                metadata={'coment': 'código da qualificação do representante legal'}
            ),
    StructField('faixa_etaria', IntegerType(), nullable=True, 
                metadata={'coment': 'código correspondente à faixa etária do sócio'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
            metadata = {'coment': 'Data que o arquivo foi carregado'}
        )
])

paises = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código de pais'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome do país'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

municipios = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código do município'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome do município'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

cnaes = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código do cnaes'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome do cnaes'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

qualificacoes  = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código da qualificação do sócio'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome da qualificação do sócio'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
            metadata = {'coment': 'Data que o arquivo foi carregado'}
        )
])

naturezas = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código da natureza juridica'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome da natureza juridica'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])

motivos = StructType([
    StructField('codigo', IntegerType(), nullable=False, 
                metadata={'coment': 'Código do motivo de situação'}
            ),
    StructField('descricao', StringType(), nullable=False, 
                metadata={'coment': 'Nome do motivo de situação'}
            ),
    StructField('data_ingestao', DateType(), nullable=False,
        metadata = {'coment': 'Data que o arquivo foi carregado'}
    )
])
