# 00 Imports

import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import json
import os

# 01 Pulling from CNN Lite

response = requests.get('https://lite.cnn.com')

soup = BeautifulSoup(response.content, 'html.parser')

headline = []
content_div = soup.find('div')
if content_div:
    for para in content_div.find_all('li'):
        headline.append(para.text.strip())
else:
    print("No article content found.")

links = []
content_a = soup.find('div')
if content_a:
    for para in content_a.find_all('a'):
        links.append(para.get('href'))
else:
    print("No link content found.")
print("01 Done!")
print(f"FOR DEBUG: {headline}")

#01.1 Finding old articles

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

with open(file_path, 'r') as f:
    data = json.load(f)

old_story = data["story1"]['text']
print(old_story)

# 02 Gemini Link in

client = genai.Client(api_key="AIzaSyBf9WqsaSIzcHBcYJd6YpH9-F0dff3rb3M")
def hl1():
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Using this list provided to you, find an article that is the most relevent today. Make sure it is completly and entirly differnt from this story: {old_story}. THESE TWO STORIES SHOULD BE DIFFERNT!! Then simplify it down to be 1-2 sentence, easy to digest and understandable. ONLY draw from this list and ONLY output the simplifed headline using ZERO MARKDOWN! Here is the list: {headline}"
)
    return response
head1 = hl1()

print(f"HEADLINE 1 {head1.text}")
print("02 Done!")

# 03 Link to Json

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

with open(file_path, "r") as f:
    data = json.load(f)

data["story1"]["headline"] = f"{head1.text}"

with open("backend/data.json", "w") as f:
    json.dump(data, f , indent=4)

print("03 Done!")

# 04 Identify with gemini

def findLink():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=f"Based on the headline given find the corrisponding link for it, only give me the link without additional syntax or it will mess up the code i want to do, thanks! Headline: {head1}, Links: {links}. If you cant find the link please output: Error!!"
)
    return response
    
link = findLink()
print(f"{link.text}")
print("04 Done!")

# 05 Find Decription

url_extension = link.text.strip()

response2 = requests.get(f'https://lite.cnn.com{url_extension}')

soup = BeautifulSoup(response2.content, 'html.parser')

article_text = []

content_article = soup.find('article')
if content_article:
    for para in content_article.find_all('p'):
        article_text.append(para.text.strip())
else:
    print("No article content found.")
    print("TEXT:", link.text)
print(article_text)
print("05 Done!")

# 06 Generate Desc

def ds1():
  response = client.models.generate_content(
        model="gemini-2.0-flash", contents=f"Based on the headline given and article description create a non-biasased, understandable, and complete yet easy to digest description of the news article. Dont use markdown. Make sure it works with the fact that this is a news site and the headline. Headline: {head1}, Desc: {article_text} If the description isnt an article and just a repeat of the headline output: ERROR!!!. Finally Don't add speculation or questions to the description"
)   
  return response

desc1 = ds1()
print("06 Done!")

# 07 Set Description

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.json")

with open(file_path, "r") as f:
    data = json.load(f)

data["story1"]["text"] = f"{desc1.text}"

with open("backend/data.json", "w") as f:
    json.dump(data, f , indent=4)

print("07 Done!")