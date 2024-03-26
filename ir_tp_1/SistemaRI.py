from coletor import *

"""
Coletor simples cujo contexto é a Estomaterapia, especialidade de enfermagem voltada para a assistência de 
pacientes com estomias, fístulas, tubos, catéteres, drenos, feridas agudas e crónicas (diabetes, úlceras, hérnias) e 
incontinências urinária e anal.
A estratégia de busca para aprofundamento das páginas encontradas foi a Breadth-First Search (Busca em Largura), com limite de profundidade (max_depth).
"""
urls = ['https://sobest.com.br/', 'https://pt.wikipedia.org/wiki/Estomaterapia']

coletor = Coletor('estomaterapia', 2) # Opcionalmente, pode-se passar o nível máximo de aprofundamento, max_depth.
for url in urls:
    coletor.add_url(url)

coletor.bfs_extract_information(0)
coletor.print_results()
coletor.save_results()