# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 23:24:42 2018
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 02-01-2018 09:00:00 PM
"""

from ant import Ant
import numpy as np

class AntColony(object):
    def __init__(self, distances, pheromone, n_ants, n_best, n_iterations, 
                 rho, alpha, beta):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration
            n_best (int): Number of best ants who deposit pheromone
            n_iteration (int): Number of iterations
            rho (float): Rate it which pheromone decays. The pheromone value is multiplied by decay, so 0.95 will lead to decay, 0.5 to much faster decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight. Default=1
            beta (int or float): exponent on distance, higher beta give distance more weight. Default=1
        Example:
            ant_colony = AntColony(german_distances, 100, 20, 2000, 0.95, alpha=1, beta=2)          
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) # / len(distances)
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.rho = rho
        self.alpha = alpha
        self.beta = beta
        
    def run(self):
        colony = []
        for i in range(self.n_ants):
            ant = Ant(np.random.randint(self.distances.shape[0]), self.distances.shape[0])
            ant.build_path(self.distances, self.pheromone, self.alpha, self.beta)
            # TODO: calcular distancia e calcular FO
            colony.append(ant)    
        