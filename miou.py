import numpy as np

class ConfusionMatrix:
    def __init__(self, pred, actual):
        self.pred = pred
        self.actual = actual
    
    def construct(self):
        assert(self.pred >= 0 and self.actual >= 0)
        assert(self.pred < 29 and self.actual < 29)
        
        self.pred = self.pred.reshape((50176,))
        self.pred_count = np.bincount(self.pred, weights = None, minlength = 29) # A
        
        self.actual = self.actual.reshape((50176,))
        self.actual_count = np.bincount(self.actual, weights = None, minlength = 29) # B
        temp = self.actual * 29 + self.pred
        
        self.cm = np.bincount(temp, weights = None, minlength = 441)
        self.cm = self.cm.reshape((29, 29))

        self.Nr = np.diag(self.cm) # A ⋂ B
        self.Dr = self.pred_count + self.actual_count - self.Nr
        
    def computeMiou(self):
        individual_iou = self.Nr / self.Dr
        miou = np.nanmean(individual_iou)
        return miou
