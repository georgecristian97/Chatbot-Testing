import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords') #database train download update if necessary// currently broken and downloaded manually
import re
from colorama import Fore, Back, Style

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


f=open('data_Train/all1.txt','r')
doc_part1 = f.readlines()
f.close()
k=1
txt = ''

for i in  doc_part1:
    if k%3 == 1:
        documents = [i]
    elif k%3 ==2:

        documents = documents + [i]
        documents_df = pd.DataFrame(documents, columns=['documents'])
        stop_words_l = stopwords.words('english')
        documents_df['documents_cleaned'] = documents_df.documents.apply(lambda x: " ".join(re.sub(r'[^a-zA-Z]', ' ', w).lower() for w in x.split() if re.sub(r'[^a-zA-Z]', ' ', w).lower() not in stop_words_l))
        sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
        document_embeddings = sbert_model.encode(documents_df['documents_cleaned'])
        pairwise_similarities = cosine_similarity(document_embeddings)
        similar_ix = np.argsort(pairwise_similarities[0])[::-1]
        for ix in similar_ix:

            if ix == 0:
                print(f'Document: {documents_df.iloc[0]["documents"]}')
                continue
            print(f'Document: {documents_df.iloc[ix]["documents"]}' + '|||' + f'Cosine Similarity : {pairwise_similarities[0][ix]}')
            if pairwise_similarities[0][ix] < 0.6 :
                print(Fore.RED+'Warning data is not so similar by  BERT Analysis'+Style.RESET_ALL)
                txt = txt + '=====>' + f'{documents_df.iloc[0]["documents"]}' + f'{documents_df.iloc[ix]["documents"]}' + f'{pairwise_similarities[0][ix]}' + '\n==========='


    k=k+1


f = open ('bertSim.txt','w')
f.write(txt)
f.close()
