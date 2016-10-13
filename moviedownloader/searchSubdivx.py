import requests
from bs4 import BeautifulSoup

class SearchSubdivx():

    #Search Subdivx website with entered query
    def searchSubdivx(self, query, currentPage):
        subdivxUrl = "http://www.subdivx.com/index.php?"
        
        if currentPage == "1":
            subdivxSearch = requests.get(subdivxUrl + "q=" + query + "&accion=5&masdesc=&subtitulos=1&realiza_b=1")
        else:
            subdivxSearch = requests.get(subdivxUrl + "q=" + query + "&accion=5&masdesc=&subtitulos=1&realiza_b=1&pg=" + str(currentPage))
        
        page = BeautifulSoup(subdivxSearch.content, "html.parser")
        
        pages = page.find("div", {"class":"pagination"})
        title = page.find_all("div", {"id":"menu_detalle_buscador"})
        download = page.find_all("div", {"id":"buscador_detalle"})
        
        if title and download:
            data = [0 for x in range(2)]
            
            data[1] = self.getSubtitles(title, download)
            self.calculatePages(pages, data)
            
            return data
        else:
            return None


    #Handles the data retrieved and organizes it
    def getSubtitles(self, title, download):
       
        subtitlesList = []
        counter = 0

        for tag in title:

            subtitlesList.append([tag.find("a", {"class":"titulo_menu_izq"}).text])

        for tag in download:

            subtitlesList[counter].append(tag.find("a", {"target":"new"})['href'])
            counter += 1

        return subtitlesList


    #Calculate the number of pages of results that the query entered had
    def calculatePages(self, pages, data):

        if len(pages.contents) > 1:

            del pages.contents[0]
            del pages.contents[-1]

            data[0] = int(pages.contents[-1].text)
