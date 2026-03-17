import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    words = []
    for d in documents:
        d_split = d.split()
        words.extend(d.split())
    vocabulary = np.unique(words)
    matrix_count = np.zeros((len(documents),len(vocabulary)))

    for i,d in enumerate(documents):
        d_split = d.split()
        index = np.searchsorted(vocabulary,d_split)
        np.add.at(matrix_count[i], index, 1)

    for i,d in enumerate(documents):
        index = np.searchsorted(vocabulary,d.split())
        matrix_count[i,index] = matrix_count[i,index]/len(d.split())
    matrix_count_df = np.where(matrix_count>0,1,0)
    df = np.sum(matrix_count_df, axis = 0)
    idf = np.log(len(documents)/df)
    tf_idf = matrix_count * idf
    return (tf_idf, vocabulary)
documents =["go go go","stop stop","go stop go"]
print(tfidf_vectorizer(documents))