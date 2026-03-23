import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    precision = 0.0
    recall = 0.0
    f1 = 0.0
    accuracy = 0.0
    if average == 'binary':
        TP = np.sum((y_pred == pos_label) & (y_true == pos_label))
        FP = np.sum((y_pred == pos_label) & (y_true !=pos_label))
        FN = np.sum((y_pred != pos_label) & (y_true == pos_label))
        precision = TP / (TP + FP)
        recall = TP / (TP + FN)
        f1 = 2 * precision * recall /(precision + recall)
    else:
        tps, fps, fns = [], [], []
        
        element, counts = np.unique(y_true, return_counts = True)
        for i in element:
            TP = np.sum((y_pred == i) & (y_true == i))
            FP = np.sum((y_pred == i) & (y_true !=i))
            FN = np.sum((y_pred != i) & (y_true == i))
            
            tps.append(float(TP))
            fps.append(float(FP))
            fns.append(float(FN))
        # Tính sẵn các mảng (Vectorization)
        tps = np.array(tps)
        fps = np.array(fps)
        fns = np.array(fns)
        p_array = tps / (tps + fps + 1e-9)
        r_array = tps / (tps + fns + 1e-9)
        f1_array = (2 * p_array * r_array) / (p_array + r_array + 1e-9)
        if average == 'micro':
            tps = np.sum(tps)
            fps = np.sum(fps)
            fns = np.sum(fns)
            precision = tps / (tps + fps + 1e-9)
            recall = tps / (tps + fns + 1e-9)
            
            f1 = (2 * precision * recall) / (precision + recall + 1e-9)
        elif average == "macro":
            precision = np.mean(p_array)
            recall = np.mean(r_array)
            f1 = np.mean(f1_array)
        elif average == "weighted":
            precision = np.average(p_array, weights = counts)
            recall = np.average(r_array, weights = counts)
            f1 = np.average(f1_array, weights = counts)
    accuracy= np.mean(y_pred == y_true)
    return {"accuracy": float(accuracy), "precision": float(precision),
    "recall": float(recall), "f1": float(f1)}
y_true = [0,1,2,2]
y_pred = [0,1,0,2]
average = "micro"
pos_label = 1
print(classification_metrics(y_true, y_pred, average, pos_label))