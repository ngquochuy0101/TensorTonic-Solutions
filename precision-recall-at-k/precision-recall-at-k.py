def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = set(recommended[:k])
    relevant = set(relevant)
    hits = len(top_k & relevant)
    pre = hits / k
    re = hits / len(relevant)
    return [pre, re]