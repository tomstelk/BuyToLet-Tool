__author__ = 'tomstelk'

import urlSearchResults
import htmlSearchResults
import unicodedata
import sqlite3
#Zoopla html navigation data
import zooplaHTMLSetup

#AirBnB html navigation data
import airBnBHTMLSetup
import insertTable
import time

#Text file containing postal districts
txtfilePostalDistricts="londonPostDistricts.txt"

#Search parameters
numBeds=1
numGuests=2
text_file = open(txtfilePostalDistricts, "r")
postDistricts = text_file.read().split('\n')
text_file.close()
todaysDate=time.strftime("%d/%m/%Y")
#SQLite Database
db_name='buy2letDB.sqlite'

#Assign URL, HTML xpaths, results table
#urlTemplate=zooplaHTMLSetup.zooplaURL
#xPaths=zooplaHTMLSetup.zooplaPaths
#xpathNextSearchResults=zooplaHTMLSetup.zoopsNextPath
#resultsTable=zooplaHTMLSetup.zooplaTable



#searchParams={'Geog':'postDistrict', 'NumBeds':numBeds}

urlTemplate=airBnBHTMLSetup.airBnBURL
xPaths=airBnBHTMLSetup.airBnBPaths
xpathNextSearchResults=airBnBHTMLSetup.airBnBNextPath
resultsTable=airBnBHTMLSetup.airBnBTable
searchParams=airBnBHTMLSetup.airBnBSearchParams
searchParams['numGuests']=numGuests

"""
for i in range(0,1):
    searchParams['Geog']=postDistricts[i]
    print searchParams['Geog']
    searchURL=urlSearchResults.urlSearchResults(urlTemplate,searchParams)
    print searchURL.url
    tree=htmlSearchResults.htmlSearchResults(searchURL.url,xPaths,xpathNextSearchResults)



"""


#For each postal district get info and pop into database
#for i in range(0,len(postDistricts)):
for i in range(0,1):
    print postDistricts[i]

    #Do the searching on the internet
    searchParams['Geog']=postDistricts[i]
    searchURL=urlSearchResults.urlSearchResults(urlTemplate,searchParams)

    print searchURL.url

    #Scrape html using xpaths
    tree=htmlSearchResults.htmlSearchResults(searchURL.url,xPaths,xpathNextSearchResults)

    #Clean price string
    tree.resultList['Price']= [unicodedata.normalize('NFKD',x.strip().replace(",","").replace(u"\u00A3","")).encode('ascii','ignore') for x in tree.resultList['Price']]
    eg=list()

    print (tree.resultList['ID'][0])

    #Loop through search results pages and append hits
    for j in range(1,len(tree.resultList['ID'])):
        #eg.append([tree.resultList['ID'][i],tree.resultList['Price'][i],tree.resultList['Address'][i],searchParams['Geog'],searchParams['NumBeds']])
        eg.append([tree.resultList['ID'][j],tree.resultList['Price'][j],tree.resultList['Address'][j],searchParams['Geog'],searchParams['numGuests']],todaysDate)


    #insertTable.insertTable(db_name,resultsTable,eg)