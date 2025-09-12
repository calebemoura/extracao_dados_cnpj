# Automatização da extração de dados das empresas do Brasil

## Objetivos
Projeto tem como objetivo automatizar à extração dos dados das empresas do Brasil disponibilizado pelo o govervo  que é atualizado mensalmente pela receita federal no link. E também colocar em prática os conhecimentos: 
* lógica de programação
* conhecimentos da linguagem de programação python
* Web scraping
* Conhecimento na plataforma databriks

## Fontes de dados
[Cadastro Nacional de Pessoas Jurídicas](https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/?C=N;O=D)

[Metadados](https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf)

## Etapas do projeto
* Criar um script que realiza a requisição onde os arquivos estão hospedados
* Realizar a descompactação dos arquivos, pois em estão no formato .zip
* Realizar um papiline da camada bronze e silver

## Etapa 01

Nesta primeira do projeto é realizar a solicitação ao site onde estão hospedados os arquivos que são disponibilizados pela receita federal, que são atualizados mensalmente, porém eles não são disponibilizados em dias fixos, então neste caso teremos que realizar uma verificação se os dados atualizados foram disponibilizados. E para isso usarei a biblioteca ``requestes`` que tem essa funcionalidade de usando o método ``get`` verifica qual o ``status_code`` da requisição e a partir realizar um ação.

Tendo o ``status_code`` como ``200`` será necessário processar o ``HTML`` e extrair somente o necessário, que a pasta de arquivo mais atualizada, e para esse precessamento irei usar a biblioteca ``lxml``, que usando o ``XPATH`` para nevegar entre as hierarquias do ``HTML`` para extrair o que é necessario.

Até aqui tudo certo, foi requisitado ao servidor onde está os arquivos de cnpj, houve como retorno o `200` como `status_code` e já temos o link para o download, irei usar agora da biblioteca `ulrlib` do módulo `requests` a função `urlretrieve`, que rcebe o link do download e local que irá ser salvo.

Os arquivos baixados estão compactado no formato .zip, então urei usar outra biblioteca da para relizar este trabalho, a biblioteca `zipfile` possui um módulo `ZipFile` que recebe o arequivo e salva os arquivos descompactados no caminho estipulado. Então basicamente este é todo a lógica por trás da etapa de extração dos dados brutos.

Mas ainda tem uma questão que está aberta. Os arquivos disponibilizados pela receita federal são atualizados mensalmente, e não tem um dia e hora determinado, para contar isso criei uma tabela de log, que armazena algumas informações e para controle, desta forma antes de executar o papiline realizo um select e verifico se a ultima pasta que está no site já foi baixada, e no job adiciono um tarefa de `if/else condition` se na consta no log, não executa o job, caso contrário executa o job completo

![](https://dbc-d480a3bd-bff0.cloud.databricks.com/editor/files/1921649055843981?o=4302201714431038)