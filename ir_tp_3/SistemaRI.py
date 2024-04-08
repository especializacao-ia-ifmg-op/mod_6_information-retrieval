from coletor import Coletor
from indexador import *
from buscador import Buscador

# urls = ['https://sobest.com.br/', 'https://pt.wikipedia.org/wiki/Estomaterapia', 'https://www.estomaterapiauerj.com.br/', 'https://www.souenfermagem.com.br/fundamentos/estomia-e-ostomia/', 'https://www.cuf.pt/mais-saude/ostomia-o-que-e-e-em-que-casos-e-necessaria', 'https://www.hnipo.org.br/conheca-tudo-sobre-a-estomaterapia-do-hospital-nipo-brasileiro-e-seus-beneficios-aos-pacientes/#:~:text=O%20que%20%C3%A9%20estomaterapia%3F,e%20incontin%C3%AAncias%20urin%C3%A1ria%20e%20anal', 'https://nutritotal.com.br/pro/material/ostomia-o-que-e-e-quais-sao-os-cuidados/']
# urls = ['https://www.paho.org/pt/topicos/enfermagem', 'https://pt.wikipedia.org/wiki/Enfermagem', 'https://www.corenmg.gov.br/', 'https://www.cofen.gov.br/enfermagem-em-numeros/', 'https://enfermfoco.org/', 'https://www.gov.br/capes/pt-br/acesso-a-informacao/acoes-e-programas/avaliacao/sobre-a-avaliacao/areas-avaliacao/sobre-as-areas-de-avaliacao/colegio-de-ciencias-da-vida/ciencias-da-saude/enfermagem', 'https://cmmg.edu.br/enfermagem/']

contexto = 'enfermagem'
# coletor = Coletor(contexto, 2) # Opcionalmente, pode-se passar o nível máximo de aprofundamento, max_depth.
# for url in urls:
    # coletor.add_url(url)

# #coletor.extract_information()
# coletor.bfs_extract_information(0)
# coletor.print_results()
# coletor.save_results()

# indexer = Indexador(coletor)
# indexer.inverted_index_generator()
# indexer.update_F()
# indexer.save_index()

query = input("[buscador ] O que você deseja pesquisar? ")
searcher = Buscador("index-"+contexto+".json")
query_type = 1 # 1 = Interseção; 2 = União.
assessment = False

relevantes_curso_enfermagem = ["https://www.educamaisbrasil.com.br/cursos-e-faculdades/enfermagem",
            "https://querobolsa.com.br/cursos-e-faculdades/enfermagem",
            "https://querobolsa.com.br/cursos-e-faculdades/enfermagem",
            "https://cmmg.edu.br/enfermagem/"
]
relevants = relevantes_curso_enfermagem

results = searcher.new_search(query, query_type)
print(f'\n[buscador ] Resultados: ')
for r in results:
   print(f"\t* {r}")

if assessment and len(relevants) > 0 and len(results) > 0:
    print(f'\n[buscador ] Avaliação do Sistema de Recuperação de Informação:')
    print(f'[buscador ]\tPrecisão = {searcher.precision(relevantes_curso_enfermagem, results)}')
    print(f'[buscador ]\tRevocação = {searcher.recall(relevantes_curso_enfermagem, results)}')