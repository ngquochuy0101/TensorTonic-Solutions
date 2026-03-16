from scipy import stats
def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    # Write code here
    mode, _ = stats.mode(predictions)
    return mode.tolist()
    
predictions = [[0,1,2]]
print(random_forest_vote(predictions))
