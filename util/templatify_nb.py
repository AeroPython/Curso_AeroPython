# coding: utf-8
import os.path
import json

NOTEBOOK_NAME = "Clase3a_Entrada-Salida-Algebra-Lineal"
TEMPLATE_NAME = "Template"
IPYNB_EXT = ".ipynb"

with open(NOTEBOOK_NAME + IPYNB_EXT, 'r') as fp:
    contents = json.load(fp)

with open(TEMPLATE_NAME + IPYNB_EXT, 'r') as fp:
    template = json.load(fp)

extra_cells = template['worksheets'][0]['cells'][-10:]
contents['worksheets'][0]['cells'].extend(extra_cells)
    
with open(NOTEBOOK_NAME + '_TEMPLATED' + IPYNB_EXT, 'w') as fp:
    json.dump(contents, fp)
    
