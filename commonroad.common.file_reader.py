import os
import matplotlib.pyplot as plt

from commonroad.common.file_reader import CommonRoadFileReader
from commonroad.visualization.draw_dispatch_cr import draw_object

file_path = os.path.join(os.getcwd(), 'scenarios/NGSIM/Lankershim/USA_Lanker-1_1_T-1.xml')

scenario, planning_problem_set = CommonRoadFileReader(file_path).open()

plt.figure(num=1,figsize=(25, 10))
draw_object(scenario)
draw_object(planning_problem_set)
plt.gca().set_aspect('equal')


draw_parameters = {'time_begin': 11}

plt.figure(num=2,figsize=(25, 10))
draw_object(scenario, draw_params=draw_parameters)
draw_object(planning_problem_set)
plt.gca().set_aspect('equal')
plt.show()