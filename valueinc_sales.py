# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:55:19 2023

@author: rohan
"""

import pandas as pd

# Reading the file
data= pd.read_csv("transaction2.csv", sep=";")

##Working with calculations

#Defining Variables
cost_per_item= data['CostPerItem']
# =============================================================================
# selling_price_per_item= data['SellingPricePerItem']
# number_of_items_purchased= data['NumberOfItemsPurchased']
# 
# cost_per_transaction= cost_per_item* number_of_items_purchased
# 
# =============================================================================

#Adding New Column to DataFrame == "CostPerTransaction"
data["CostPerTransaction"]= data["CostPerItem"]* data["NumberOfItemsPurchased"]

##Adding New Column to Datafram == "SalesPerTransaction"
data["SalesPerTransaction"]= data["SellingPricePerItem"]* data['NumberOfItemsPurchased']

##Adding Margin Column to DataFrame == "MarginPerTransaction"
data["ProfitPerTransaction"] = data["SalesPerTransaction"]- data["CostPerTransaction"]
data["Margin"]= round((data["ProfitPerTransaction"]/ data["SalesPerTransaction"])*100, 2)
data["Markup"]= round((data["ProfitPerTransaction"]/ data["CostPerTransaction"])*100, 2)

#Combining Data fields - (Date)
my_date= data["Day"].astype(str)+"-"+data["Month"]+"-"+data["Year"].astype(str)
data["Date"]= my_date


#Using Iloc to View specific Columns & Rows
# =============================================================================
# data.iloc[0] # To view 0th Row
# data.iloc[0:3]# To view first 3 rows
# =============================================================================


#SPLIT() to split the "Clent_keyword" field
## e.g., new_var= column.str.split('sep', expand= True)

split_client_keyword= data['ClientKeywords'].str.split(",", expand= True)

#New Columns for the split in Client Keyword
data["ClientAge"]= split_client_keyword[0]
data["ClientType"]= split_client_keyword[1]
data["LengthofContract"]= split_client_keyword[2]


#Using the replace function cleaning above 3 columns
data["ClientAge"]= data["ClientAge"].str.replace("[", "")
data["LengthofContract"]= data["LengthofContract"].str.replace("]", "")


#How to merge files?
#Bringing new dataset
data_seasons= pd.read_csv("value_inc_seasons.csv")
print("data_seasons")

#Merging two Dataframes
data= pd.merge(data, data_seasons, on= 'Month')


#Dropping Columns
data= data.drop(["Year", "Month", "Day", "ClientKeywords"], axis=1)

#Export into csv
data.to_csv("Valueinc_CleanedData.csv")
















