from pyspark.sql.types import StructType, StructField, StringType

empresas = StructType([
    StructField('cnpj_basico', StringType(), True,
                metadata = {'coment': 'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('razao_social', StringType(), True,
                metadata = {'coment': 'nome empresarial da pessoa jurídica'}
            ),
    StructField('natureza_juridica', StringType(), True, 
                {'coment': 'código da natureza jurídica'}
            ),
    StructField('qualificacao_responsavel', StringType(), True,
                metadata = {'coment': 'qualificação da pessoa física responsável pela empresa'}
            ),
    StructField('capital_social', StringType(), True,
                metadata = {'coment': 'capital social da empresa'}
            ),
    StructField('porte', StringType(), True,
                metadata = {'coment': 'código do porte da empresa: 00 – não informado 01 - micro empresa 03 - empresa de pequeno porte 05 - demais'}
            ),
    StructField('ente_federativo', StringType(), True,
                metadata = {'coment': 'o ente federativo responsável é preenchido para os casos de órgãos e entidades do grupo de natureza jurídica 1xxx. para as demais naturezas, este atributo fica em branco.'}
            ) 
])

estabelecimentos = StructType([
    StructField('cnpj_basico', StringType(), True, 
                metadata={'coment':'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('cnpj_ordem', StringType(), True, 
                metadata={'coment':'número do estabelecimento de inscrição no cnpj (do nono até o décimo segundo dígito do cnpj)'}
                ),
    StructField('cnpj_dv', StringType(), True, 
                metadata={'coment': 'dígito verificador do número de inscrição no cnpj (dois últimos dígitos do cnpj).'}
                ),
    StructField('identificador', StringType(), True,
                metadata={'coment': ''}
            ),
    StructField('matriz_filial', StringType(), True, 
                metadata={'coment': 'código do identificador matriz/filial: 1–matriz, 2–filial'}
            ),
    StructField('nome_fantasia', StringType(), True, 
                metadata={'coment': 'corresponde ao nome fantasia'}
            ),
    StructField('situacao_cadastral', StringType(), True, 
                metadata={'coment': 'corresponde ao nome fantasia código da situação cadastral: 01–nula, 02–ativa, 03–suspensa, 08–baixada'}
            ),
    StructField('data_situacao_cadastral', StringType(), True, 
                metadata={'coment': 'data do evento da situação cadastral'}
            ),
    StructField('motivo_situacao_cadastral', StringType(), True, 
                metadata={'coment': 'código do motivo da situação cadastral'}
            ),
    StructField('cidade_exterior', StringType(), True, 
                metadata={'coment': 'nome da cidade no exterior'}
            ),
    StructField('pais', StringType(), True, 
                metadata={'coment': 'código do pais'}
            ),
    StructField('inicio_atividade', StringType(), True, 
                metadata={'coment': ''}
            ),
    StructField('cnae_fiscal_principal', StringType(), True, 
                metadata={'coment': 'data de início da atividade'}
            ),
    StructField('cnae_fiscal_secundaria', StringType(), True, 
                metadata={'coment': 'código da atividade econômica principal do estabelecimento'}
            ),
    StructField('tipo_logradouro', StringType(), True, 
                metadata={'coment': 'código da(s) atividade(s) econômica(s) secundária(s) do estabelecimento'}
            ),
    StructField('logradouro', StringType(), True, 
                metadata={'coment': 'descrição do tipo de logradouro'}
            ),
    StructField('numero', StringType(), True, 
                metadata={'coment': 'número onde se localiza o estabelecimento. quando não houver preenchimento do número haverá s/n.'}
            ),
    StructField('complemento', StringType(), True, 
                metadata={'coment': 'complemento para o endereço de localização do estabelecimento'}
            ),
    StructField('bairro', StringType(), True, 
                metadata={'coment': 'bairro onde se localiza o estabelecimento.'}
            ),
    StructField('cep', StringType(), True, 
                metadata={'coment': 'código de endereçamento postal referente ao logradouro no qual o estabelecimento esta localizado'}
            ),
    StructField('uf', StringType(), True, 
                metadata={'coment': 'sigla da unidade da federação em que se encontra o estabelecimento'}
            ),
    StructField('municipio', StringType(), True, 
                metadata={'coment': 'código do município de jurisdição onde se encontra o estabelecimento'}
            ),
    StructField('ddd_1', StringType(), True, 
                metadata={'coment': 'contém o ddd 1'}
            ),
    StructField('telefone_1', StringType(), True, 
                metadata={'coment': 'contém o número do telefone 1'}
            ),
    StructField('ddd_2', StringType(), True, 
                metadata={'coment': 'contém o ddd 2'}
            ),
    StructField('telefone_2', StringType(), True, 
                metadata={'coment': 'contém o número do telefone 2'}
            ),
    StructField('ddd_fax', StringType(), True, 
                metadata={'coment': 'contém o ddd do fax'}
            ),
    StructField('fax', StringType(), True, 
                metadata={'coment': 'contém o número do fax'}
            ),
    StructField('correio_eletronico', StringType(), True, 
                metadata={'coment': 'contém o e-mail do contribuinte'}
            ),
    StructField('situacao_especial', StringType(), True, 
                metadata={'coment': 'situação especial da empresa'}
            ),
    StructField('data_situacao', StringType(), True, 
                metadata={'coment': 'data em que a empresa entrou em situação especial'}
            )
])

simples = StructType([
    StructField('cnpj_basico', StringType(), True, 
                metadata={'coment': 'número base de inscrição no cnpj (oito primeiros dígitos do cnpj).'}
            ),
    StructField('opcao_pelo_simples', StringType(), True, 
                metadata={'coment': 'indicador da existência da opção pelo simples. s-sim, n-não, em branco–outros data de opção pelo simples'}
            ),
    StructField('data_opcao_pelo_simples', StringType(), True, 
                metadata={'coment': 'data de exclusão do simples'}
            ),
    StructField('data_exclusao_simples', StringType(), True, 
                metadata={'coment': 'data de exclusão do simples opção pelo mei'}
            ),
    StructField('opcao_pelo_mei', StringType(), True, 
                metadata={'coment': 'indicador da existência da opção pelo mei s-sim, n-não, em branco-outros'}
            ),
    StructField('data_opcao_pelo_mei', StringType(), True, 
                metadata={'coment': 'data de opção pelo mei'}
            ),
    StructField('data_exclusao_mei', StringType(), True, 
                metadata={'coment': 'data de exclusão do mei'}
            )
])

socios = StructType([
    StructField('cnpj_basico', StringType(), True, 
                metadata={'coment': 'número base de inscrição no cnpj (cadastro nacional da pessoa jurídica).'}
            ),
    StructField('identificador_socio', StringType(), True, 
                metadata={'coment': 'código do identificador de sócio 1–pessoa jurídica, 2–pessoa física, 3–estrangeiro'}
            ),
    StructField('nome_socio', StringType(), True, 
                metadata={'coment': 'nome do sócio pessoa física ou a razão social e/ou nome empresarial da pessoa jurídica e/ou nome do sócio/razão social do sócio estrangeiro'}
            ),
    StructField('cnpj_cpf_socio', StringType(), True, 
                metadata={'coment': 'cpf ou cnpj do sócio (sócio estrangeiro não tem esta informação).'}
            ),
    StructField('qualificacao_socio', StringType(), True, 
                metadata={'coment': 'código da qualificação do sócio'}
            ),
    StructField('data_entrada', StringType(), True, 
                metadata={'coment': 'data de entrada na sociedade'}
            ),
    StructField('pais', StringType(), True, 
                metadata={'coment': 'código país do sócio estrangeiro'}
            ),
    StructField('representante_legal', StringType(), True, 
                metadata={'coment': 'número do cpf do representante legal'}
            ),
    StructField('nome_representante', StringType(), True, 
                metadata={'coment': 'nome do representante legal'}
            ),
    StructField('qualificacao_representante', StringType(), True, 
                metadata={'coment': 'código da qualificação do representante legal'}
            ),
    StructField('faixa_etaria', StringType(), True, 
                metadata={'coment': 'código correspondente à faixa etária do sócio'}
            )
])

paises = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código de pais'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome do país'}
            )
])

municipios = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código do município'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome do município'}
            )
])

cnaes = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código do cnaes'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome do cnaes'}
            )
])


qualificacoes  = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código da qualificação do sócio'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome da qualificação do sócio'}
            )
])

naturezas = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código da natureza juridica'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome da natureza juridica'}
            )
])

motivos = StructType([
    StructField('codigo', StringType(), True, 
                metadata={'coment': 'Código do motivo de situação'}
            ),
    StructField('descricao', StringType(), True, 
                metadata={'coment': 'Nome do motivo de situação'}
            )
])
