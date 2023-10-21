''' This is a program which collects all the ratings of every vijay movie till date and then graphs them to see the trend '''

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

#set url and get webpage
url = "https://en.wikipedia.org/wiki/Vijay_filmography"
req = requests.get(url)

#Get tags in webpage
wiki = BeautifulSoup(req.text, "html.parser")

'''Make list of movies'''
movies=list()

#Get the names of movies from wikipedia
for tag in wiki.find_all("th"):
    movies.append(tag.text.strip())

#Cleaning the list
for i in range(5):
    movies.pop(0)

'''Make list of rating of movies'''
rating=list()

for movie in movies:
    #set url and get webpage
    url = "https://www.google.com/search?client=opera&q="+movie+"+Vijay+movie+IMDB+rating&sourceid=opera&ie=UTF-8&oe=UTF-8"
    #url="https://www.google.com/search?q="+movie+"+Vijay+movie+rating&client=opera&hs=98a&ei=C4msYsydOMyq4t4Pu9m5uAU&ved=0ahUKEwiMz6jx0rT4AhVMldgFHbtsDlcQ4dUDCA0&uact=5&oq="+movie+"+Vijay+movie+rating&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABMgUIIRCgATIFCCEQoAE6BwgAELADEEM6CAgAEIAEELADOgcIABAeELADOgkIABAeELADEAg6DAguEMgDELADEEMYAToPCC4Q1AIQyAMQsAMQQxgBOgQILhBDOgUIABCABDoHCC4QgAQQCjoGCAAQHhAWOgQIIRAVOggIIRAeEBYQHUoECEEYAUoECEYYAVCj2ANYzNwDYJPdA2gBcAB4AIABswGIAbsFkgEDMS40mAEAoAEByAEUwAEB2gEGCAEQARgI&sclient=gws-wiz"
    req = requests.get(url)

    #Get tags in webpage
    search = BeautifulSoup(req.text, "html.parser")

    #Get the rating of movies from searchpage
    mydivs = search.find_all("span",{"class":"oqSTJd"})
    print(movie, end= "  ")
    #print(mydivs[0], end= "  ")
    rating.append(float(mydivs[0].text[0:mydivs[0].text.find("/")])/10)
    print(mydivs[0].text)

''' Making graph'''
plt.plot(movies,rating)
plt.title("Vijay movies vs ratings")
plt.xlabel("Vijay_movie")
plt.ylabel("Rating as per IMDB")
plt.show()


#"oqSTJd"
#<div class="yQ8hqd zr7Aae nQaFad RW3Gwf">
#<span class="gsrt IZACzd" aria-hidden="true">6.9/10</span>
#<div class="NJo7tc Z26q7c" data-content-feature="2"><div class="fG8Fp uo4vr"><g-review-stars aria-hidden="true"><span class="Fam1ne tPhRLe" role="img"><span style="width:46px"></span></span></g-review-stars> <span>Rating: 6.9/10</span>
