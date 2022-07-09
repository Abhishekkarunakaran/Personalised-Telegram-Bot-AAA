import requests
from bs4 import BeautifulSoup
from filtration import filt



def scrap(lt=0):
#Making a GET request
  r = requests.get('https://ktu.edu.in/eu/core/announcements.htm')
  # lt = 0
  if r.status_code == 200 :
    print("Scrapping website...")
    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    s = soup.find('div', class_='c-details')
  
    content = s.find_all('li')
    
    links = s.find_all('a')
    sss = links[lt].get('href').split(" ")
    description = content[lt].text
    # if description[len(content[0].b.text)+1:] == "Notification" :
    #   description=""
      
    link ='https://ktu.edu.in' + sss[0].strip("\r\n") +sss[len(sss) - 1].strip("\t")
    title = content[lt].b.text
    des = description[len(content[lt].b.text)+1:].replace("Notification","").strip("\n")
    
    
    message = f'*{title}*\n\n{des}\n\n{link}'
    filt(title)
    print("Successfully parsed!")
    
    return message 