import matplotlib.pyplot as pltt
import seaborn as sns

pltt.figure(figsize= (10,6))
sns.barplot(x="categoria", y="ventas", data=df)