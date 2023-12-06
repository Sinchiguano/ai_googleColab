#IMPORT REQUIRED LIBRARIES
import pandas as pd


#IMPORT OUR INPUT DATA FOR HOUSE PRICE PREDICTION 
df=pd.read_csv('USA_Housing.csv')
print(df.head(2))
print('--------------')
print(df.columns)
print('--------------')
print(df.shape)



#DESCRIBING OUR DATA
print('#DESCRIBING OUR DATA')
print(df.describe())

#ANALYZING INFORMATION FROM OUR DATA
print('#ANALYZING INFORMATION FROM OUR DATA')
print(df.info())


#PLOT TO VISUALIZE DATA OF HOUSE PRICE PREDICTION.
print('#PLOT TO VISUALIZE DATA OF HOUSE PRICE PREDICTION.')
#PRICE IS HIGHLY CORRELATED TO AVERAGE AREA INCOME 
import seaborn as sns
import matplotlib.pyplot as plt
# sns.pairplot(df)
# plt.show()

'''What is Correlation?

Ever wondered how your data variables are linked to one another? Variables within a dataset can be related for lots of reasons.
For example:

    One variable could cause or depend on the values of another variable.
    One variable could be lightly associated with another variable.
    Two variables could depend on a third unknown variable. 

All of these aspects of correlation and how data variables are dependent or can relate to one another get us thinking about their use. Correlation is very useful in data analysis and modelling to better understand the relationships between variables. The statistical relationship between two variables is referred to as their correlation.

A correlation could be presented in different ways: 

    Positive Correlation: both variables change in the same direction.
    Neutral Correlation: No relationship in the change of the variables.
    Negative Correlation: variables change in opposite directions. '''


#SCALING OUR DATA
#ENHANCES MODEL PERFORMANCE
#AVOID NUMERICAL LINSTABILITIES (EXTREMELY LARGE OR SMALL VALUES CAN LEAD TO NUMERICAL PRECISION ISSUES)
#REGULARIZATION


from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

x=df.drop(['Price','Address'],axis=1)
y=df['Price']


featuresNames=x.columns
x=scaler.fit_transform(x)

#SPLITTING OUR DATA FOR TRAINING AND TEST PURPOSES
from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y, test_size=0.3,random_state=101)



#TRAINING OUR LINEAR REGRESSION MODEL FOR HOUSE PRICE PREDICTION 

from sklearn.linear_model import LinearRegression


model=LinearRegression()
model.fit(xtrain, ytrain)

predictions=model.predict(xtest)

#EVALUATION METRIC OF THE MODEL
from sklearn.metrics import r2_score
print(f'The performance of the model {r2_score(ytest,predictions)}')


#LET'S VISULIZE OUR PREDICTIONS OF HOUSE PRICE PREDICTION


sns.scatterplot(x=ytest,y=predictions)
plt.show()









