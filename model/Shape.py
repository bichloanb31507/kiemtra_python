from abc import ABC, abstractmethod

class Shape(ABC):
    
    def __init__(x : int, y: int):
        x = x
        y = y
        
    @abstractmethod
    def chuVi():
        pass
    
    @abstractmethod
    def dienTich():
        pass