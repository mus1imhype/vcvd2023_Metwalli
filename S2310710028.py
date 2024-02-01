__doc__ = "file for the main method"

#import system libs
import argparse
import sys

#own modules
from examples.plot import draw_plot_
from calculation import calculate_braking_distance

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
cmd_call_args_ = arg_parser_.parse_args()
print (cmd_call_args_.pdf_file_out)

#defining parameters
vehicle_mass = float(input("Enter the mass of the car [in kilograms]: "))
vehicle_velocity = float(input("Enter the velocity of the car [in m/s]: "))
inclination = float(input("Enter the inclination of the road [in degrees]: "))
road_type = input("Enter the road type [concrete/ice/water]: ")
wet_dry = input("Enter the road condition [wet/dry/aquaplaning]: ")

#calling method
velocity, distance, time = calculate_braking_distance(
vehicle_mass,vehicle_velocity,inclination, road_type, wet_dry)

#calling method
draw_plot_(cmd_call_args_.pdf_file_out,velocity, distance, time)

#terminate program
sys.exit()
