# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:28:31 2022

@author: benja
"""

import pandas as pd
import math
#This function will get the Term Frequency X Inverse Doc Frequency for an attribute
def tfidf(item,doc):
    tf=doc.value_counts()[item]/len(doc);
    #Holds the length
    idf=math.log2(len(doc)/doc.value_counts()[item]);
    return tf*idf;

#This function will return the sales catergoy that will be focused on
def switch(demo):
    if demo == "NA":
        return'NA_Sales';
    elif demo == "EU":
        return'EU_Sales';
    elif demo == 'JP':
        return'JP_Sales';
    elif demo == 'Other':
        return'Other_Sales'

#This function will find which console the game should be released in based on genre, region, and maybe the rating
def recommend(genre,rate,demo,addrate):
    region=None;
    #This will determine which region sales the system should consider for sales
    
    region=switch(demo);
    #Holds the games for each 7th generation console based on their genre and rating
    sales=[]
    #This function will determine which console is the best for the game by finding the 
    max=0;
    console="";
    #If we are including the rating, create a dataframe that will include only the user passed rating value
    if(addrate):
        sales.append(df[df['Platform'].str.contains('Wii') & df['Genre'].str.contains(genre) & df['Rating'].str.contains(rate)]);
        sales.append(df[df['Platform'].str.contains('X360') & df['Genre'].str.contains(genre) & df['Rating'].str.contains(rate)]);
        sales.append(df[df['Platform'].str.contains('DS') & df['Genre'].str.contains(genre) & df['Rating'].str.contains(rate)]);
        sales.append(df[df['Platform'].str.contains('PS3') & df['Genre'].str.contains(genre) & df['Rating'].str.contains(rate)]);
    #If we're noting taking rating into consideration, the dataframe will include the games that fit a genre regardless of rating.
    else:
          sales.append(df[df['Platform'].str.contains('Wii') & df['Genre'].str.contains(genre)]);
          sales.append(df[df['Platform'].str.contains('X360') & df['Genre'].str.contains(genre)]);
          sales.append(df[df['Platform'].str.contains('DS') & df['Genre'].str.contains(genre)]);
          sales.append(df[df['Platform'].str.contains('PS3') & df['Genre'].str.contains(genre)]);  
    #This function will try to find 
    for x in range(len(sales)):
        s=sales[x][region].median()
        if(s>max):
            max=s
            console=sales[x];
    return console;

#Import the list of video games
df=pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv', sep=',', low_memory=(False));
#Shrinks the dataframe to only include 7th generation consoles
df=df[df["Platform"].isin(['Wii','X360','DS','PS3'])]
#This asks for user input for the genre, rating, and region for the game they plan to release
genre= input('What is the genre of the game?\n');
rate= input('What is the game rated?\n');
demo= input('What is the target region for the game?\nPlease type in either: "NA", "EU", "JP", or "Other".\n')


results=recommend(genre,rate,demo,True);
if(len(results)>0):
    print("For a "+genre+" game rated "+rate+", the best 7th generation console for them to port their game to would be the "+ results.iloc[-1]["Platform"]);
else:
    results=recommend(genre,rate,demo,False);
    print("For a "+genre+" game, the best 7th generation console for them to port their game to would be the "+ results.iloc[-1]["Platform"]);