import requests
from bs4 import BeautifulSoup

def scrap():
#Making a GET request
  r = requests.get('https://ktu.edu.in/eu/core/announcements.htm')
  
  if r.status_code == 200 :
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    s = soup.find('div', class_='c-details')
  
    content = s.find_all('li')
    
    links = s.find_all('a')
    sss = links[0].get('href').split(" ")
    description = content[0].text
    # if description[len(content[0].b.text)+1:] == "Notification" :
    #   description=""
      
    link ='https://ktu.edu.in' + sss[0].strip("\r\n") +sss[len(sss) - 1].strip("\t")
    title = content[0].b.text
    des = description[len(content[0].b.text)+1:].replace("Notification","").strip("\n")
    print(link)
    
    
    message = f'*{title}*\n\n{des}\n\n[Download Notification]({link})'
    
    return message