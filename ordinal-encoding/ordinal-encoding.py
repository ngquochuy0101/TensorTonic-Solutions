import numpy as np
def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """

    values = np.array(values)
    ordering = np.array(ordering)
    mask = values[:, None] == ordering
    cols, row = np.where(mask)
    return row.tolist()
    

    
values = ["low","medium","high","medium"]
ordering = ["low","medium","high"]
print(ordinal_encoding(values, ordering))