#missing data
def missing_data(all_data):
	total = df_train.isnull().sum().sort_values(ascending=False)
	percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
	missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
	return missing_data

cols = missing_data[missing_data['Total'] > 2000].index

all_data.drop(cols, 1, inplace=True)