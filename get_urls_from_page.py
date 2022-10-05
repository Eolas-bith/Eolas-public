def get_urls_from_page(url,max_urls): #get all links from the website, from the seed top down
    import requests
    from bs4 import BeautifulSoup
    total_urls_visited=0
    #URL='https://aeronet.cz/news/vakciny-proti-covid-19-jsou-ve-skutecnosti-trojskymi-koni-magnetogenetiky-na-dalkova-ovladani-lidskych-mozku-virginska-univerzita-jiz-v-roce-2016-uspesne-otestovala-virus-ktery-v-mozku-mysi/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page=requests.get(url,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    #links=soup.find_all("a",id='link')
    links=soup.find_all("a")
    total_urls_visited+=1
    for i,link in enumerate(set(links)):
        if total_urls_visited > max_urls:
            print("Max urls exceeded, quitting!")
            break
        print(i," ",link["href"])
        #print(link["href"])
        try:
            get_urls_from_page(link)
        except:
            continue