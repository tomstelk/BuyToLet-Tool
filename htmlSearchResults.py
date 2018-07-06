__author__ = 'tomstelk'
import requests
from lxml import html
class htmlSearchResults():
    def __init__(self, url, resultPaths, nextPath):
        self.url=url
        self.resultsTree=html.fromstring(requests.get(url).text)
        self.resultList=dict((k,v) for k,v in resultPaths.items())
        self.nextPath=nextPath
        self.resultPaths=resultPaths
        self.populateResultList()


    def populateResultList(self):
        for key in self.resultList:
            self.resultList[key]=self.resultsTree.xpath(self.resultPaths[key])

        nextURL=self.getNextURL(self.resultsTree)

        while nextURL!='searchOver':
            nextResultTree=html.fromstring(requests.get(nextURL).text)
            for key in self.resultPaths:
                self.resultList[key].extend(nextResultTree.xpath(self.resultPaths[key]))
            nextURL=self.getNextURL(nextResultTree)
            print nextURL

    def getNextURL(self, currentTree):

        if len(currentTree.xpath(self.nextPath))!=0:
            tmpNextURL=currentTree.xpath(self.nextPath)[0]
            if 'airbnb' in tmpNextURL:
                numNextPage=tmpNextURL.split('?page=',1)[1]
                tmpNextURL=self.url + '&page=' + numNextPage
        else:
            tmpNextURL='searchOver'
        return tmpNextURL

    def checkResultValid(self):
        resultsCount=self.resultsTree.xpath('//div[@class="results_count"]/p/text()')
        if len(resultsCount) > 0 and '1000+' in resultsCount[0]:
            validResult=False
        else:
            validResult=True
        return validResult