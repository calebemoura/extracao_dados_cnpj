# Importação das bibliotecas necessárias
from requests import get
from lxml import etree
from urllib.request import urlretrieve
from datetime import datetime
from zipfile import ZipFile

myparser = etree.HTMLParser(encoding='utf-8')

# Caminhos onde os arquivos serão baixados e descompactados
path_souce = '/Volumes/landing/raw/rfb_cnpj/temp/'  # arquivos compactados zip
path_destination = '/Volumes/landing/raw/rfb_cnpj/' # Arquivos descompactados

url_base = 'https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/'
mes = datetime.today().strftime('%Y-%m/')

# Realizando a requisição
requisicao = get(f"{url_base}{mes}")
if requisicao.status_code != 200:
    print('Arquivos ainda não disponíveis')
else:
    html = requisicao.content
# Processando o HTML e buscando os arquivos zip
tree = etree.HTML(html, parser=myparser)

for link in tree.xpath('//table'):
    folders = [f for f in link.xpath('./tr/td/a/@href') if f.endswith('.zip')]

# Realizando o download dos arquivos
for folder in folders:
    url = f"{url_base}{mes}{folder}"
    print(url)
    urlretrieve(url, f"{path_souce}/temp/{folder}")
paths = dbutils.fs.ls(path_souce)

for path in paths:
    with ZipFile(f"{path_souce}{path.name}", 'r') as zipObj:
        zipObj.extractall(f"{path_destination}/{path.name.split('.')[0].lower()}")