from bs4 import BeautifulSoup
import requests
import pprint



def sortedByVotes(selection):
    return sorted(selection,key=lambda i:i['votes'],reverse=True)


def customised(links,subTexts):
    selection =[]
    for i ,item in enumerate(links):
        title =item.getText()
        ref =item.get('href',None)
        vote =subTexts[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if(points>99):
                selection.append({'title': title,'link':ref,'votes':points})

    #print(selection)
    return sortedByVotes(selection)

def controlPannel(req):
    soup1 = BeautifulSoup(req.text, 'html.parser')
    links = soup1.select('.storylink')
    # votes = soup1.select('.score')
    subTexts = soup1.select('.subtext')
    pprint.pprint(customised(links, subTexts))


req=requests.get('https://news.ycombinator.com/news')
controlPannel(req)
print('\n\n\n\n\n\n\n\n\n')
for i in range (2,5):
    req=requests.get(f'https://news.ycombinator.com/news?p={i}')
    controlPannel(req)
    print('\n\n\n\n\n\n\n\n\n')




