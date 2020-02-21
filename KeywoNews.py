#The goal of this small project is using newsAPI to access the last news that contains a specific keyword. 

from newsapi import NewsApiClient
#GET_API=https://newsapi.org/
user_api=input("Please Enter your NewsAPI: ")
keyword=input('News with a keyword: ')
newsapi = NewsApiClient(api_key=user_api)
top_headlines = newsapi.get_top_headlines(q=keyword)
print("#####################################################################################################")
print("Server status: ",top_headlines['status'],"                    |                    ","\t Number of results: ", top_headlines['totalResults'])
print("#####################################################################################################")
while int(top_headlines['totalResults'])==0:
    print("Sorry! A result cannot be found!!")
    keyword=input('Try a new keyword: ')
    top_headlines = newsapi.get_top_headlines(q=keyword)
    print("#####################################################################################################")
    print("Server status: ",top_headlines['status'],"                    |                    ","\t Number of results: ", top_headlines['totalResults'])
    print("#####################################################################################################")
for item in top_headlines["articles"]:
    print(f"ººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº")
    print("-------------------------------------------------------------------------------------------------")
    print("Title: ", item['title'])
    print("-------------------------------------------------------------------------------------------------")
    print("Author: ", item['author'])
    print("-------------------------------------------------------------------------------------------------")
    print("Description:\n", item['description'])
    print("-------------------------------------------------------------------------------------------------")
    print("Link: ", item['url'])
    print("-------------------------------------------------------------------------------------------------")
    print("Source: ", item['source']['name'])
    print("-------------------------------------------------------------------------------------------------")
    print("Published: ", item['publishedAt'].replace("T"," Time: "))
    print("-------------------------------------------------------------------------------------------------")
    print("ºººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººººº\n")
print("\n Enjoy reading!!")

#This code is written by Zakaria Dahbi | etriziko@gmail.com
#This project can be used to develop huge news projects and earn money from. 
