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
sns.pairplot(df)
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

