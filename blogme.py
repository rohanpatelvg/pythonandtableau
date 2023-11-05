# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 12:45:40 2023

@author: rohan
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer




#Reading excel files
data= pd.read_excel("articles.xlsx")

#Summary of Data
data.describe()

#Summary of Columns
data.info()


#Counting the number of articles per source
data.groupby(['source_id'])['article_id'].count()

#Number of reactions by Publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()


#Dropping column
data= data.drop('engagement_comment_plugin_count', axis= 1)


#Creating a Keyword flag to find if we have KW like "Murder, Kill", etc. in the title
# keyword= 'crash'

# #let's create a forloop to isoltae each title


# keyword_flag= []
# for x in range(0,10):
#     heading= data['title'][x]
#     if keyword in heading.lower():
#         flag= 1
#     else:
#         flag= 0
#     keyword_flag.append(flag)
    

length= len(data)
keyword_flag= []
def keywordFlag(keyword):
    total_flag= 0
    for x in range(0, length):
        title= data['title'][x]
        try:
            if keyword in title.lower():
                flag= 1
            else:
                flag= 0
        except: 
            flag= 0
        total_flag= total_flag+ flag
        keyword_flag.append(flag)
    print(total_flag)
    return keyword_flag


#Creating a new column in Data DF
murder_keyword_flag= keywordFlag('murder')
data["murder_keyword_flag"]= pd.Series(keyword_flag)




#SentimentIntensityAnalyzer
senti_int= SentimentIntensityAnalyzer()

text= data["title"][16]
sentiment= senti_int.polarity_scores(text)
print(sentiment)

neg= sentiment['neg']
pos= sentiment['pos']
neu= sentiment['neu']
print(neu)


#Addidng For Loop to extract sentiment for our Title
title_neg_sentiment= []
title_pos_sentiment= []
title_neu_sentiment= []

for x in range(0, length):
    try:
        text= data['title'][x]
        sentiment= senti_int.polarity_scores(text)
        
        title_neg_sentiment.append(sentiment['neg'])
        title_pos_sentiment.append(sentiment['pos'])
        title_neu_sentiment.append(sentiment['neu'])
    except:
        title_neg_sentiment.append(0)
        title_pos_sentiment.append(0)
        title_neu_sentiment.append(0) 


data['title_neg_sentiment']= pd.Series(title_neg_sentiment)
data['title_pos_sentiment']= pd.Series(title_pos_sentiment)
data['title_neu_sentiment']= pd.Series(title_neu_sentiment)


#Writing the data into Excel
data.to_excel('blogme_clean.xlsx', sheet_name= 'blogmedata')



        
        
    
    
    

    





































