import nbformat


def empty_notebook(fname):
    with open(fname, 'r', encoding='utf-8') as fp:
        nb = nbformat.read(fp, as_version=4)

    for cell in nb.cells:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if '# preserve' in source:
                continue
            elif 'Image(url=' in source:
                continue
            elif 'HTML(' in source:
                continue
            else:
                # Don't preserve cell
                cell['outputs'].clear()
                cell['execution_count'] = None
                cell['source'] = '\n'.join([l for l in source.splitlines() if l.startswith('#')])

    return nb


if __name__ == '__main__':
    import glob
    import os.path
    
    if os.path.isdir('notebooks_completos'):
        prepath = '.'
    elif os.path.isdir(os.path.join('..','notebooks_completos')):
        prepath = '..'
    else: raise OSError('Carpeta de notebooks no encontrada')
        
    vacios_path = os.path.join(prepath , 'notebooks_vacios')
    completos_path = os.path.join(prepath , 'notebooks_completos')

    if not os.path.isdir(vacios_path):
        os.makedirs(vacios_path)
    for fname in glob.glob(os.path.join(completos_path , '*.ipynb')):
        new_fname = os.path.join(vacios_path, os.path.basename(fname))
        with open(new_fname, 'w', encoding='utf-8') as fp:
            nbformat.write(empty_notebook(fname), fp)
            
            
            
