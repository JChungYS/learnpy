filenames = ['01.docx', '02.docx']
with open('e:\pyscript\outcome.docx', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)