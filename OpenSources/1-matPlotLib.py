# https://matplotlib.org/
import matplotlib.pyplot as plt
import numpy as np


# make a very basic scatter plot
plt.plot([1, 2, 3, 4, 5, 6, 7], [30, 20, 10, 0, 10, 20, 30], 'ro')
plt.xlabel('time')
plt.ylabel('speed (mph)')
plt.title('ball speed over time')


# multiple trials plots
time_points = np.arange(0, 10, 1)
response_1 = [0, .2, .4, .8, 1.6, 3.2, 3.2, 3.2, 3.2, 3.2]
response_2 = [0, .1, .2, .4, .8, 1.6, 3.2, 6.4, 12, 12]
response_3 = [0, .1, .2, .3, .4, .8, 1.6, 1.6, 1.6,  1.6]
plt.plot(time_points, response_1, 'g*', label='trial1')
plt.plot(time_points, response_2, 'rH', label='trial2')
plt.plot(time_points, response_3, 'bv', label='trial3')
plt.ylabel('response')
plt.xlabel('time (min)')
plt.title('Drug response over time')
plt.legend(loc='upper left')

# scatter plot based on size; data with more than 2 dimensions
age = [5, 6, 7, 8, 9, 10, 11, 12]
avg_continuous_sleep = [5, 5, 7, 6.5, 8, 6.5, 7, 8]
total_participants = [1000, 900, 200, 230, 670, 420, 900, 150]
colors = np.random.rand(len(age))
plt.scatter(age, avg_continuous_sleep, s=total_participants, c=colors, alpha=0.50)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.xlabel('age (years)', fontsize=15)
plt.ylabel('average hours of continuous sleep', fontsize=15)
plt.title('average contnuous sleep within each age group', fontsize=15)
plt.show()