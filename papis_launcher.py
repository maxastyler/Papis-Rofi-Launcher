import papis.api
from rofi import Rofi

docs = papis.api.get_all_documents_in_lib()

def info_string(doc):
    s = ""
    try:
        s += doc.title
    except AttributeError:
        pass
    try:
        s += doc.author
    except AttributeError:
        pass
    return s

options = [info_string(d) for d in docs]

r=Rofi()
i = r.select("Select a paper", options, fullscreen=True)[0][0]
if i >= 0:
    files = docs[i].get_files()
    print(files)
    if len(files) > 1:
        j = r.select("Select file ", files)[0][0]
        if j >= 0:
            papis.api.open_file(files[j])
    elif len(files) == 1:
        papis.api.open_file(files[0])
