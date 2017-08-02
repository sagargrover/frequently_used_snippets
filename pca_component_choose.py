pca = PCA(whiten=True)
pca.fit(data)
variance = pd.DataFrame(pca.explained_variance_ratio_)
np.cumsum(variance).head(50)

#select index where 1 starts
pca = PCA(n_components=41,whiten=True)
pca = pca.fit(data)
dataPCA = pca.transform(data)