train_new = pd.DataFrame(train)
train_new["SP"] = y_full
corrmat = train_new.corr()
sns.heatmap(corrmat, vmax=0.8)
sns.plt.show()