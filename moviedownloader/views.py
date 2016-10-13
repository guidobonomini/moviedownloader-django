from django.shortcuts import render
from moviedownloader.searchYTS import *
from moviedownloader.searchSubdivx import *

def index(request):
    return render(request, 'home.html')

def searchYTS(request, query, currentPage):
    
    search = SearchYTS()
    result = search.searchYTS(query, currentPage)
    if result:
        return render(request, 'search.html', {'movies': result[1], 'pages': [0 for x in range(result[0])]})
    else:
        return render(request, 'search.html', {'movies': result})

	
def searchPirateBay(request, query, currentPage):
    
    #search = SearchPirateBay()
    #result = search.searchPirateBay(query, currentPage)
    return render(request, 'search.html', {'movies': result[1], 'pages': [0 for x in range(result[0])]})


def searchSubdivx(request, query, currentPage):
    
    search = SearchSubdivx()
    result = search.searchSubdivx(query, currentPage)
    if result:
        return render(request, 'searchSubtitles.html', {'subtitles': result[1], 'pages': [0 for x in range(result[0])]})
    else:
        return render(request, 'searchSubtitles.html', {'subtitles': result})
