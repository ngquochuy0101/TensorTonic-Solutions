import numpy as np
def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """

    values = np.array(values)
    ordering = np.array(ordering)
    mask = values[:, None] == ordering
    output =np.argmax(mask, axis = 1)
    return output.tolist()
    

    
values = ["low","medium","high","medium"]
ordering = ["low","medium","high"]
print(ordinal_encoding(values, ordering))