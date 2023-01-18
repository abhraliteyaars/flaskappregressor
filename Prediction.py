import pandas as pd
import pickle



df=pd.read_csv('Data.csv')

df.drop(columns='Customer ID',inplace=True)
X=df.iloc[:,:3]

y=df[['Orders']]


from sklearn.linear_model import LinearRegression

model=LinearRegression()

model.fit(X,y)


# Saving model to disk- wb==write binary
pickle.dump(model, open('model.pkl','wb'))


# Loading model to compare the results--rb=read binary
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[10, 90, .3]]))