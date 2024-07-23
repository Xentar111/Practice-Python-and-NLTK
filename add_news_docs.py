import os
import codecs

docs = './docs'

for root, folder_docs, files_docs in os.walk(docs, topdown=False):
    #print(root, folder_docs, files_docs)
    for doc in files_docs:
        f = codecs.open(os.path.join(root, doc), 'r', 'utf-8')
        text = f.read()
        f.close
        print(text)