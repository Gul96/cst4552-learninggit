import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y,marker='x',color='red',linestyle='--',linewidth=1)
plt.bar(x,y,color='blue',width=0.5)
plt.scatter(x,y,color='green',s=100)    
df = pd.DataFrame({'category': ["A","B","C"], 'Values': [10,20,25]})
df = sns.barplot(x='category',y='Values',data=df)
plt.show()