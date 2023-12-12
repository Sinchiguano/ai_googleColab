import pandas as pd
import pickle





df=pd.read_csv('daily_weather.csv')
print(df.head(5))

print('------first check of nan values-----------')

print(df[df.isnull().any(axis=1)].head(10))


print()
print()
print()
df=df.dropna(axis=0)
# print(df.head(5))

print('---------check again for null values--------')
print(df[df.isnull().any(axis=1)].head(3))




del df['number']

#CONVERT TO A CLASSIDICATION TALK

clean_data=df.copy()
# clean_data.columns
#BINARIZE THE RELATIVE HUMIDITY AT 3PM TO 0 OR 1
# clean_data.shape

clean_data['high_humidity_label']=(clean_data['relative_humidity_3pm']>24.99)*1

print(clean_data['high_humidity_label'].head(10))


morning_features=['air_pressure_9am', 'air_temp_9am', 'avg_wind_direction_9am',
       'avg_wind_speed_9am', 'max_wind_direction_9am', 'max_wind_speed_9am',
       'rain_accumulation_9am', 'rain_duration_9am', 'relative_humidity_9am', 'high_humidity_label']




x=clean_data[morning_features].copy()
x.columns


y=clean_data[['high_humidity_label']].copy()
# y.head(5)


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# you set the same random_state value, you will get the same results each time you run your code.
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.33,random_state=324)

# Create a StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data and transform both training and testing data
# X_train_scaled = scaler.fit_transform(x_train)
# X_test_scaled = scaler.transform(x_test)


X_train_scaled = x_train
X_test_scaled = x_test


print('x_train.shape')
print(x_train.shape)

print('--------LOADING THE MODEL ---------')
# Load the pickled model
model = pickle.load(open('lastModel.pkl', 'rb'))


predictions=model.predict(X_test_scaled)
print(predictions[:10])

print('done!!!!!!!')