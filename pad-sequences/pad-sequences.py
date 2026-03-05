import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.zeros((0,0))
    if max_len is None:
        max_len = max(map(len, seqs))
    len_seqs = len(seqs) 
    arr_pad = np.full((len_seqs, max_len), pad_value)
    for i in range(len_seqs):
        seq = seqs[i]
        len_seq = min(len(seq), max_len)
        arr_pad[i,: len_seq] = seq[:len_seq]
    return  arr_pad
seqs = [[1,2,3,4],[5,6]]
pad_value = 0
print(pad_sequences(seqs, pad_value=0, max_len=3))