import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fig=plt.figure(figsize=(16,9), dpi=100)
rng = np.random.default_rng(42)
N=1000
steps = rng.choice([-1, 1], size=N)
y_arr1=[0]
for i in range (len(steps)):
    y_arr1.append(y_arr1[i]+steps[i])
plt.plot(list(range(1001)),y_arr1,'g')
plt.xlabel('N')
plt.ylabel('x(N)')
plt.title("Случайный путь одной частицы")
plt.grid()
plt.show()

fig=plt.figure(figsize=(16,9), dpi=100)
M=1000
hist=[]
steps1 = rng.choice([-1, 1], size=(M, N))
for i in steps1:
    hist.append(sum(i))
plt.hist(hist,100)
X = np.cumsum(steps1, axis=1)
plt.title("Распределение положений 1000 частиц")
plt.xlabel("Положение x после 1000 шагов")
plt.ylabel("Число частиц")
plt.grid()
plt.show() 

fig=plt.figure(figsize=(16,9), dpi=100)
rms = np.sqrt(np.mean(X**2, axis=0))
Ns=np.arange(1,N+1) 
plt.plot(Ns,rms, label='RMS из симуляции')
plt.plot(Ns,np.sqrt(Ns), label='RMS теория')
plt.title('Зависимость RMS от числа шагов')
plt.xlabel('N')
plt.ylabel('RMS x')
plt.legend()
plt.grid()
plt.show()


