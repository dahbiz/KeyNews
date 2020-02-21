from newsapi import NewsApiClient

def status():
    print("#####################################################################################################")
    print("# Server status: ",top_headlines['status'],"                    |                    ","\t Number of results: ", top_headlines['totalResults'])
    print("#####################################################################################################")
    return
#def store():
#    savenews[f'title']=item['title']
#    savenews[f'content']=item['content']
#    newslist.append(savenews)
#    return
#savenews= {}
#newslist=[]
#GET_API=https://newsapi.org/
user_api=input("Please Enter your NewsAPI: ")
keyword=input('Keyword: ')
newsapi = NewsApiClient(api_key=user_api)
top_headlines = newsapi.get_top_headlines(q=keyword)
status()
while int(top_headlines['totalResults'])==0:
    print("Sorry! A result cannot be found!!")
    keyword=input('Try a new keyword: ')
    top_headlines = newsapi.get_top_headlines(q=keyword)
    status()
for item in top_headlines["articles"]:
    print(f"ºººººººººººººººººººººººººººººººººººººººººº\\\ººººººººººººººººººººººººººººººººººººººººººººººººººº")
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
    #store()
