import requests
# response[1]["title"]
def get_data():
    url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=be805478ab5840a3b820a974b56fe770"
    # Hit the url
    response=requests.get(url)

    # get the article
    response=response.json()["articles"]

    return response

# Get the title
def get_title(response,index):
    return response[index]["title"]

# Get description
def get_description(response,index):
    return response[index]["description"]

def get_image(response,index):
    return response[index]['urlToImage']

def get_content(response,index):
    return response[index]['content'][:-13]

def get_url(response,index):
    return response[index]['url']
