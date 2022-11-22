import numpy as np
import matplotlib.pyplot as plt

N_steps = 5
t_start = 0
t_end = 30
y = np.zeros((2, N_steps + 1))
t =  np.linspace(t_start,t_end,N_steps + 1)
A = np.array([[1,2],[2,1]])
vectorB = np.array([1, 2])
c = A@vectorB

print(c)
