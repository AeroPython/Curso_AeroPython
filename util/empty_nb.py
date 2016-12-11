import nbformat


def empty_notebook(fname):
    with open(fname, 'r') as fp:
        nb = nbformat.read(fp, as_version=4)

    for cell in nb.cells:
        if cell['cell_type'] == 'code':
            source = cell['source']
            if '# aeropython: preserve' in source:
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

    for fname in glob.glob("notebooks_completos/*.ipynb"):
        new_fname = os.path.join("notebooks_vacios", os.path.basename(fname))
        with open(new_fname, 'w') as fp:
            nbformat.write(empty_notebook(fname), fp)
