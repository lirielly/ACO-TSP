# -*- coding: utf-8 -*-
"""
Authors: Lirielly Vitorugo Nascimento & Rafael Nascimento
E-mail: lvitorugo@gmail.com & rafael.correian@gmail.com
Date and hour: 01-07-2018 05:00:00 PM
"""

import argparse
import pandas as pd
from antColony import AntColony

def read_distances(file_name):
    distance_matrix = pd.read_csv(file_name, header=None, sep=';', decimal=",")
    if(distance_matrix.shape[0] != distance_matrix.shape[1]):
        raise Exception('Distance matrix has to be a square matrix!')
    return distance_matrix.values

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ACO')
    parser.add_argument('-k', '--ants', type=int, dest='k', default='17',
                        help='ants number')
    parser.add_argument('-p', '--ro', type=float, dest='p', default='0.99',
                        help='pheromone rate decay')
    parser.add_argument('-a', '--alpha', type=float, dest='a', default='0.5',
                        help='pheromone trail importance')
    parser.add_argument('-b', '--beta', type=float, dest='b', default='8.0',
                        help='local heuristic importance')
    parser.add_argument('-c', '--distance_cost', type=float, dest='c', 
                        default='1.0', help='one unit distance cost')
    parser.add_argument('-n', '--n_best_ants', type=int, dest='n', 
                        default='10', help='best ants number')
    parser.add_argument('-i', '--iterations', type=int, dest='i', 
                        default='1', help='iterations number')
    parser.add_argument('-d', '--distance_matrix', 
                        dest='file_name_distance_matrix', 
                        default='distances.csv', 
                        help='local heuristic importance')
    args = parser.parse_args()
    
    print('Starting ACO Python!')    
    
    distance_matrix = read_distances(args.file_name_distance_matrix)
    
    colony = AntColony(distance_matrix, args.c, args.k, args.n, args.i, args.p,
                       args.a, args.b)
    best_ant = colony.run()
    
    print("OF: ")
    print(best_ant.of())
    print("PATH: ")
    print(best_ant.path)