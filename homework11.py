import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def grafic(x,y,subplot,title):
    ax = fig.add_subplot(subplot)
    ax.plot(x,y,'g', label='График')
    ax.set_title(title)
    X_ax=np.array(x)
    Y_ax=np.array(y)
    LS_ax=np.polyfit(X_ax, Y_ax, 1)
    X_ax_line = np.linspace(X_ax.min(), X_ax.max(), 100)
    Y_ax_line = LS_ax[1] + LS_ax[0] * X_ax_line
    ax.plot(X_ax_line, Y_ax_line, color='red', label=f'МНК: y={np.poly1d(LS_ax)}')
    plt.grid()
    plt.legend(fontsize=9.5)
    print(np.corrcoef(x, y)[0, 1])

df = pd.read_csv('iris_data.csv')
df1=list(df['SepalLengthCm'])
df2=list(df['SepalWidthCm'])
df3=list(df['PetalLengthCm'])
df4=list(df['PetalWidthCm'])
fig=plt.figure(figsize=(16,9), dpi=100)
grafic(df1,df2,231,'SepalLength от SepalWidthCm')
grafic(df1,df3,232,'SepalLength от PetalLengthCm')
grafic(df1,df4,233,'SepalLength от PetalWidthCm')
grafic(df2,df4,234,'SepalWidthCm от PetalWidthC')
grafic(df3,df2,235, 'PetalLengthCm от SepalWidthCm')
grafic(df3,df4,236,'PetalLengthCm от PetalWidthCm')
plt.show()



