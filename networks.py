import torch
from torch import nn
import numpy as np

class MLP(nn.Module):
    def __init__(self, ny: int, nx: int, nf: int, na: int):
        """À MODIFIER QUAND NÉCESSAIRE.
        Ce constructeur crée une instance de réseau de neurones de type Multi Layer Perceptron (MLP).
        L'architecture choisie doit être choisie de façon à capter toute la complexité du problème
        sans pour autant devenir intraitable (trop de paramètres d'apprentissages). 

        :param na: Le nombre d'actions 
        :type na: int
        """
    def forward(self, x):
        """Cette fonction réalise un passage dans le réseau de neurones. 

        :param x: L'état
        :return: Le vecteur de valeurs d'actions (une valeur par action)
        """

def truncated_normal_(tensor, mean=0, std=1):

def weights_init(m):
class CNN(nn.Module):
    def __init__(self, ny: int, nx: int, nf: int, na: int):
        """À MODIFIER QUAND NÉCESSAIRE.
        Ce constructeur crée une instance de réseau de neurones convolutif (CNN).
        L'architecture choisie doit être choisie de façon à capter toute la complexité du problème
        sans pour autant devenir intraitable (trop de paramètres d'apprentissages). 

        :param na: Le nombre d'actions 
        :type na: int
        """

    def forward(self, x):
        """Cette fonction réalise un passage dans le réseau de neurones. 

        :param x: L'état
        :return: Le vecteur de valeurs d'actions (une valeur par action)
        """

