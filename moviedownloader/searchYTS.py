import requests
from bs4 import BeautifulSoup

class SearchYTS():

    #Search YTS website with entered query
    def searchYTS (self, query, currentPage):
        ytsUrl = "https://yts.ag/"
        
        if currentPage == "1":
            ytsSearch = requests.get(ytsUrl + "browse-movies/" + query + "/all/all/0/latest")
        else:
            ytsSearch = requests.get(ytsUrl + "browse-movies/" + query + "/all/all/0/latest?page=" + currentPage)
        
        page = BeautifulSoup(ytsSearch.content, "html.parser")
        
        pages = page.find("ul", {"class":"tsc_pagination tsc_paginationA tsc_paginationA06"})
        ytsTag = page.find_all("div", {"class":"browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4"})

        if ytsTag:
            data = [0 for x in range(2)]
            
            data[1] = self.getMovieListYTS(ytsTag)
            self.calculatePages(pages, data)
            
            return data
        else:
            return None


    #Handles the data retrieved and organizes it
    def getMovieListYTS(self, ytsTag):
        
        movieList = []
        
        for tag in ytsTag:

            movieFound = []
            movieImg = tag.find("img", {"class":"img-responsive"})
            movieTitle = tag.find("a", {"class":"browse-movie-title"}).text
            divHD = tag.find("a", string="720p")
            divFullHD = tag.find("a", string="1080p")

            if divHD and divFullHD:
                movieFound = [movieTitle, movieImg.attrs['src'], [divHD.attrs['href'], "720p"], [divFullHD.attrs['href'], "1080p"]]
            elif not divFullHD and divHD:
                movieFound = [movieTitle, movieImg.attrs['src'], [divHD.attrs['href'], "720p"]]
            else:
                movieFound = [movieTitle, movieImg.attrs['src'], [divFullHD.attrs['href'], "1080p"]]

            movieList.append(movieFound)

        return movieList

    #Calculate the number of pages of results that the query entered had
    def calculatePages(self, pages, data):

        if len(pages.contents) > 1:

            del pages.contents[0]
            del pages.contents[-1]

            data[0] = int(pages.contents[-3].text)
