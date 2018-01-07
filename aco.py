# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 05:00:00 PM
"""

import argparse
import pandas as pd
from ant import Ant

def read_distances(file_name):
    distance_matrix = pd.read_csv(file_name, header=None, sep=';')
    if(distance_matrix.shape[0] != distance_matrix.shape[1]):
        raise Exception('Distance matrix has to be a square matrix!')
    return distance_matrix

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ACO')
    parser.add_argument('-k', '--ants', type=int, dest='k', default='10',
                        help='ants number')
    parser.add_argument('-p', '--ro', type=float, dest='p', default='0.01',
                        help='pheromone rate decay')
    parser.add_argument('-a', '--alpha', type=float, dest='a', default='0.1',
                        help='pheromone trail importance')
    parser.add_argument('-b', '--beta', type=float, dest='b', default='1.0',
                        help='local heuristic importance')
    parser.add_argument('-d', '--distance_matrix', 
                        dest='file_name_distance_matrix', 
                        default='distances.csv', 
                        help='local heuristic importance')
    args = parser.parse_args()
    
    print('Starting ACO Python!')    
    
    distance_matrix = read_distances(args.file_name_distance_matrix)
    print(distance_matrix)
    
    swarm = [Ant() for i in range(args.k)]
    print(swarm)