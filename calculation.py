__doc__ = "file for the calculating method"

#required imports
import numpy as np

#==============================================================================
#   Methode for calculating the braking distance for a vehicle
#   Parameters:
#       mass: Mass of the vehicle
#       initial_velocity: Initial velocity of the vehicle
#       inclination: The inclination of the road
#       road_type: The type of the road
#       wet_dry: The condition of the road
#   Returns:
#       velocity: Calculated velocity values
#       distance: Calculated distance values
#       time: Time points for plot
#==============================================================================

def calculate_braking_distance(mass, initial_velocity,inclination,
                               road_type, wet_dry):
  calculate_braking_distance.__doc__ = "braking distance calculation"

  #constants
  g = 9.81
  mue = {"concrete": {"dry": 0.65, "wet": 0.4},"ice": {"dry": 0.2, "wet": 0.1},
         "water": {"aquaplaning": 0.2,}}
  friction_coefficient = mue[road_type][wet_dry]

  #functions
  theta = np.radians(inclination)
  force_friction = friction_coefficient * mass * g * np.cos(theta)
  acceleration = - force_friction / mass
  time = np.arange(0.0, 7.5, 0.01)
  velocity = initial_velocity + acceleration * time
  distance = initial_velocity * time + 0.5 * acceleration * time**2

  return velocity, distance, time
