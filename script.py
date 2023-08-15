import pandas as pd
import numpy as np

# code goes here
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.head())
#Number of Columns
print(len(diabetes.columns))

#Number of Rows
print(len(diabetes))

#Does it have null values?
print(diabetes.isnull().sum())

#Summary Statistics
print(diabetes.describe())

#Making the 0 -> Nan YOU HAVE TO COMENT THIS FUNCTION SO THE LAST ONE ON THIS EXERCISE CAN RUN
#diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
#print(diabetes.isnull().sum()) #Now we see a LOT of Nan values comparing to the 0 values

#Checking every row that have these occurancies
print(diabetes[diabetes.isnull().any(axis = 1)])

#Finding the error on Outcome and correcting it
print(diabetes.Outcome.unique())
diabetes['Outcome'] = diabetes['Outcome'].replace('O','0')

#Changing the value to a Int64
diabetes['Outcome'] = diabetes['Outcome'].astype('int64')
print(diabetes.Outcome.unique())

#Fully Exploring the values
Pregnancies_count = diabetes['Pregnancies'].value_counts()
print(Pregnancies_count) #We see here possible outliers pregnancies from 12 to 17

Skin_count = diabetes['SkinThickness'].value_counts()
print(Skin_count) #Here we find an absurd outlier 99 skin thickness where the closer value is 39 thicknesses away

#Opose to Nan we input to the missing values in this case the median of the values of the columns
for i in diabetes:
  list = diabetes[i].median()
  diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,abs(list))
print(diabetes)

#print(diabetes.dtypes)
