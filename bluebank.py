# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 08:50:28 2023

@author: rohan
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Method 1 to read json data
json_file= open('loan_data_json.json')
data= json.load(json_file)

#Transform to Dataframe
loandata= pd.DataFrame(data)


#Finding Unique valuse in "Purpose" Column
print(loandata["purpose"].unique())

#Describing Data
loandata["int.rate"].describe()
loandata["fico"].describe()
loandata["dti"].describe()


#Using exponant to get the Annual Income of "log.annual.inc"
income= np.exp(loandata["log.annual.inc"])
loandata["annualincome"]= income

#FICO/Credit Score

ficocategory= []
for ficoscore in loandata['fico']:
    try:
        if ficoscore >=300 and ficoscore <400:
            ficocat= 'Very Poor'
        elif ficoscore >= 400 and ficoscore <600:
            ficocat= 'Poor'
        elif ficoscore >=601 and ficoscore <660:
            ficocat= 'Fair'
        elif ficoscore>= 660 and ficoscore< 700:
            ficocat= 'Good'
        elif ficoscore>= 700:
            ficocat= 'Excellent'
        else:
            ficocat= 'Unknown'
    except:
        ficocat= "Unknown"
    ficocategory.append(ficocat)
    
    
#Convert list into Series to add column in dataframe
ficocategory= pd.Series(ficocategory)
loandata['fico.category']= ficocategory

#for interest rates a new Column is needed if the rate is >0.12 then high, else low
loandata.loc[loandata["int.rate"]> 0.12, 'int.rate.type']= 'High'
loandata.loc[loandata["int.rate"]<= 0.12, 'int.rate.type']= 'Low'


#Number of loans/rows by ficoCategory
catplot= loandata.groupby(['fico.category']).size()
catplot.plot.bar()
plt.show()

purposecount= loandata.groupby(['purpose']).size()
purposecount.plot.bar(color= 'green', width= 0.5)
plt.show()


#Scatteplot -> Annual Income & DebtToRatio
y_axis= loandata['annualincome']
x_axis= loandata['dti']
plt.scatter(x_axis, y_axis)
plt.show()


#save as csv
loandata.to_csv('BlueBank_cleaned.csv', index= True)































