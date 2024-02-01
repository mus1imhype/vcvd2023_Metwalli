__doc__ = "file for the plotting method"

#required imports
import matplotlib.pyplot as plt

#===============================================
# Methode for plotting the braking distance
# Parameters:
#   file_name_out: Name for the PDF
#   velocity: Calculated velocity values
#   distance: Calculated distance values
#   time: Time points for plot
# Returns:
#   No returns
#===============================================

def draw_plot_(file_name_out, velocity, distance, time):
  draw_plot_.__doc__ = "call to mathplotlib"

  #define figure
  fig = plt.figure()

  #add one plot
  #221...2 Graphs, next to each other, Nummerierung
  ax1 = fig.add_subplot(221)
  ax2 = fig.add_subplot(222)

  #add grid
  ax1.grid(True)
  ax2.grid(True)

  #define plots
  ax1.plot(time, velocity, color ="red", lw = 2)
  ax2.plot(time, distance, color ="green", lw = 2)

  #add axis label
  ax1.set_xlabel("Time (s)")
  ax1.set_ylabel("Velocity (m/s)")

  ax2.set_xlabel("Time (s)")
  ax2.set_ylabel("Distance (m)")

  #add plot label
  fig.suptitle("Braking Distance Graph\n", fontweight ="bold")

  #automatically adjust subplot parameters
  fig.tight_layout()

  #export as PDF
  plt.savefig(file_name_out)
  