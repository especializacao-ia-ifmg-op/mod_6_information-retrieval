from coletor import Coletor
from indexador import * # IndexadorUm, IndexadorN
from buscador import Buscador

# urls = ['https://www.ifmg.edu.br/ribeiraodasneves', 'http://www.ufop.br', 'https://www.serpro.gov.br', 'https://www.caixa.gov.br']
urls = ['https://www.vivo.com.br/para-voce', 'https://www.serpro.gov.br', 'https://www.caixa.gov.br', 'https://www.ifmg.edu.br/ribeiraodasneves']

# Coletor para n urls
coletor = Coletor('Root')
for url in urls:
    coletor.add_url(url)

# Indexador para cada url (Abordagem N:1)
coletor.extract_information()
# for object in coletor.objects_url:
#    indexer = IndexadorUm(object)
#    indexer.inverted_index_generator()
#    indexer.save_index()
    
# Indexador para n urls (Abordagem N:N) <- Melhor num contexto!
#indexer = IndexadorN(coletor)
indexer = Indexador(coletor)
indexer.inverted_index_generator()
indexer.save_index()


query = input("O que você deseja pesquisar? ")
searcher = Buscador("index-Root.json")
results = searcher.search(query)
for r in results:
   print(f"Resultado: {r}")