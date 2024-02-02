##Exemplo tirado do youtube para compreender melhor o padrão adapter

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def metodoA():
        """Um método qualquer A"""

class ClassA(IA):
    def metodoA(self):
        print("Método A")

class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def metodoB():
        """Um método qualquer B"""

class ClassB(IB):
    def metodoB(self):
        print("Método B")

class ClassBAdapter(IA):
    def __init__(self):
        self.classB = ClassB()

    def metodoA(self):
        """Classe B chama Método B"""
        self.classB.metodoB()

ITEM = ClassBAdapter()
ITEM.metodoA()
