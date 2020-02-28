import json
import numpy as numpy
import re

def to_tokens(texto):
    tokens = re.findall(r'(\b\w+\b)+', texto)
    return [ t.lower() for t in tokens]

docs = []
with open('./books.jl', 'r') as f:
    for line in f:
        docs.append(json.loads(line))

terms = {}

for i in range(len(docs)):
    doc = docs[i]
    tokens = to_tokens(doc['name'])

    for token in tokens:
        if token in terms:
            token_docs = terms[token]
            token_docs.append(i)
            token_docs = list(set(token_docs))
            token_docs.sort()
            terms[token] = token_docs
        else:
            terms[token] = [i]

search_terms = ['the', 'barefoot']

indexes = [terms[st.lower()] for st in search_terms]

print(indexes)

# for index in indexes:
    # print (docs[index]['name'])

