import sys
import requests
from bs4 import BeautifulSoup
import os
import datetime

class Download(movie):
    

    def downloadMovie(self, movieToDownload, resolution):

        torrentExtension = ".torrent"

        if resolution == "720p":
            try:
                r = requests.get(movieToDownload[1][0], stream=True)
                fname = movieToDownload[0] + torrentExtension
                with open(fname, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()
            
            except requests.exceptions.RequestException as e:
                #print('\n' + str(e))
                sys.exit(1)
        else:
            try:
                r = requests.get(movieToDownload[2][0], stream=True)
                fname = movieToDownload[0] + torrentExtension
                with open(fname, "wb") as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()
            
            except requests.exceptions.RequestException as e:
                #print('\n' + str(e))
                sys.exit(1)

        self.startDownloadOnTorrentClient(fname)


    def startDownloadOnTorrentClient(self, fname):

        os.startfile(fname)

