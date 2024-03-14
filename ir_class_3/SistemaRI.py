from coletor import Coletor
from indexador import IndexadorUm, IndexadorN

urls = ['https://www.ifmg.edu.br/ribeiraodasneves', 'http://www.ufop.br', 'https://www.serpro.gov.br', 'https://www.caixa.gov.br']

# Coletor para n urls
coletor = Coletor('Root')
for url in urls:
    coletor.add_url(url)

# Indexador para cada url (Abordagem N:1)
coletor.extract_information()
for object in coletor.objects_url:
    indexer = IndexadorUm(object)
    indexer.inverted_index_generator()
    indexer.save_index()
    
# Indexador para n urls (Abordagem N:N)
indexer = IndexadorN(coletor)
indexer.inverted_index_generator()
indexer.save_index()