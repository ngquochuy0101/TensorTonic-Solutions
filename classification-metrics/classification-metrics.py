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
        
        element, count = np.unique(y_true, return_counts = True)
        for i in element:
            TP = np.sum((y_pred == i) & (y_true == i))
            TN = np.sum((y_pred == i) & (y_true == i))
            FP = np.sum((y_pred == i) & (y_true !=i))
            FN = np.sum((y_pred != i) & (y_true == i))
            
            tps.append(float(TP))
            fps.append(float(FP))
            fns.append(float(FN))
        tps = np.array(tps)
        fps = np.array(fps)
        fns = np.array(fns)
        if average == 'micro':
            tps = np.sum(tps)
            fps = np.sum(fps)
            fns = np.sum(fns)
            precision = ( tps/ (tps +fps ))
            recall = tps /(tps + fns)
            f1 = (2 * precision *recall) / (precision + recall)
        elif average == "macro":
            precision = np.mean(tps / (tps + fps))
            recall = np.mean(tps/(tps +fns))
            f1 = np.mean(((2 * (tps / (tps + fps)) *(tps/(tps +fns)))) / (tps / (tps + fps) + (tps/(tps +fns))))
        elif average == "weighted":
            precision = np.average((tps / (tps + fps)), weights = count)
            recall = np.average((tps/(tps +fns)), weights = count)
            f1 = np.average((((2 * (tps / (tps + fps)) *(tps/(tps +fns)))) / (tps / (tps + fps) + (tps/(tps +fns)))), weights = count)
            
    accuracy= np.mean(y_pred == y_true)
    return {"accuracy": float(accuracy), "precision": float(precision),
    "recall": float(recall), "f1": float(f1)}
y_true = [0,1,2,2]
y_pred = [0,1,0,2]
average = "micro"
pos_label = 1
print(classification_metrics(y_true, y_pred, average, pos_label))