# AUTOGENERATED! DO NOT EDIT! File to edit: 01_utils.data.dataloaders.ipynb (unless otherwise specified).

__all__ = ['DataLoaders']

# Cell
from ...imports import *

# Cell

class DataLoaders:
    '''Wrapper for Torch Dataloader specifically for train and valid ds'''
    def __init__(self, *ds, device='cpu', accumulate = 1):
        '''
            Args:
                *ds: train and valid Dataset
                device: on which device to put dataset on while training/ sending data to model
                accumulate: for gradient accumulation default i.e no gradient accumulation
        '''
        self.train, self.valid = ds
        self.device = device
        self.accumulate = accumulate