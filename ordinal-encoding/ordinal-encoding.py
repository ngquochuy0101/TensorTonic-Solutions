import numpy as np
def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """

    values = np.array(values)
    ordering = np.array(ordering)
    mask = values[:, None] == ordering
    row, cols = np.where(mask)
    return cols.tolist()
    

    
values = ["low","medium","high","medium"]
ordering = ["low","medium","high"]
print(ordinal_encoding(values, ordering))