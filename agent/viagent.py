import numpy as np
from copy import deepcopy

from agent import AgentInterface
from world.deterministic_maze import DeterministicMazeModel

import pandas as pd

class VIAgent(AgentInterface):
    """ 
    Un agent capable de résoudre un labyrinthe donné grâce à l'algorithme d'itération 
    sur les valeurs (VI = Value Iteration).
    """

    def __init__(self, maze_model: DeterministicMazeModel, gamma: float):
        """"À COMPLÉTER!
        Ce constructeur initialise une nouvelle instance de la classe ValueIteration.
        Il doit stocker les différents paramètres nécessaires au fonctionnement de l'algorithme et initialiser à 0 la 
        fonction de valeur d'état, notée V.

        :param maze_model: Le modèle du problème
        :type maze_model: DeterministicMazeModel

        :param gamma: le facteur d'atténuation
        :type gamma: float
        :requirement: 0<gamma<1

        #visualisation des données
        :attribut mazeValues: la fonction de valeur stockée qui sera écrite dans un fichier de log après la résolution complète
        :type mazeValues: data frame pandas
        :penser à bien stocker aussi la taille du labyrinthe (nx,ny)
        """

    def solve(self, error: float):
        """À COMPLÉTER!
        Cette méthode résoud le problème avec une tolérance donnée.
        Elle doit proposer l'option de stockage de la fonction de valeur dans un fichier de log (logVI.csv)
        """
    def done(self, V, V_copy, error) -> bool:
        """À COMPLÉTER!
        Cette méthode retourne vraie si la condition d'arrêt de 
        l'algorithme est vérifiée. Sinon elle retourne faux.
        """

    def bellman_operator(self, s) -> float:
        """À COMPLÉTER!
        Cette méthode calcul l'opérateur de mise à jour de bellman pour un état s.

        :param s: Un état quelconque
        :return: La valeur de mise à jour de la fonction de valeur

        doit retourner une exception si l'état n'est pas valide
        """

    def select_action(self, s):
        """À COMPLÉTER!
        Cette méthode retourne l'action optimale.

        :param state: L'état courant
        :return: L'action optimale

        doit retourner une exception si l'état n'est pas valide
        """