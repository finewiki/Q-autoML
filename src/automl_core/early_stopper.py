from typing import List, Optional

class EarlyStopper:
    def __init__(self, patience: int = 5, min_delta: float = 0.001):
        self.patience = patience
        self.min_delta = min_delta
        self.counter = 0
        self.best_loss = None
        
    def early_stop(self, current_loss: float) -> bool:
        if self.best_loss is None:
            self.best_loss = current_loss
            return False
            
        if current_loss < self.best_loss - self.min_delta:
            self.best_loss = current_loss
            self.counter = 0
        else:
            self.counter += 1
            
        return self.counter >= self.patience