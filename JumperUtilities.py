# -*- coding: utf-8 -*-
"""
Created 2018 March 3
@author: Jean-Christophe Perrin

Utility functions for calculating the required forces of our jumper.
"""

import numpy as np

def takeoffSpeed(mass, height):
    """ Returns the speed required to reach a height
    Accepts:
        * mass - mass of object in kg
        * height - height at top of arc in m
    Returns:
        * v - speed at takeoff [m/s^2]
    """
    g = 9.8 # [m/s^2]
    gravitational_energy = mass * g * height
    velocity = np.sqrt(2 * gravitational_energy / mass)
    return velocity
