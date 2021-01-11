import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import re
from colorama import Fore, Style

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


f = open('data_Train/all.txt', 'r')
k=1
for i in f.readlines():
    if k==1:
        input_lines = i
    elif k%3 == 1 :
        input_lines = input_lines+ i

    k = k + 1
f.close()

f = open('data_Train/normal.txt', 'r')
k = 1
for i in f.readlines():
    if k % 3 == 1:
        input_lines = input_lines + i

    k = k + 1
f.close()

k=1
for i in input_lines.split("\n"):

   if k%3==1:
       if k==1:
            doc_part = i
       else:
            doc_part =doc_part+"\n"+i
   k=k+1
f = open('Data_Collector/data_Collector_Input.txt', 'r')



doc_part1 = f.readline() + doc_part

k = 1

for u in doc_part1.split("\n"):
    if k == 1:
        documents = [u]
    else:

        documents = documents + [u]

    k = 2

documents_df = pd.DataFrame(documents, columns=['documents'])
stop_words_l = stopwords.words('english')
documents_df['documents_cleaned'] = documents_df.documents.apply(lambda x: " ".join(re.sub(r'[^a-zA-Z]', ' ', w).lower() for w in x.split() if re.sub(r'[^a-zA-Z]', ' ', w).lower() not in stop_words_l))
sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
document_embeddings = sbert_model.encode(documents_df['documents_cleaned'])
pairwise_similarities = cosine_similarity(document_embeddings)

similar_ix = np.argsort(pairwise_similarities[0])[::-1]
print(similar_ix)
k =0
for ix in similar_ix:
    if k==0:
        print(f'Document: {documents_df.iloc[ix]["documents"]} {ix}')

    if k==1:
        print(f'Document: {documents_df.iloc[ix]["documents"]}' + '|||' + f'Cosine Similarity : {pairwise_similarities[0][ix]} {ix}' )
        if pairwise_similarities[0][ix] < 0.6:
            print(Fore.RED + 'Warning data is not so similar by BERT Analysis' + Style.RESET_ALL)

    k=k+1

