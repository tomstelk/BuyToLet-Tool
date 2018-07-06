__author__ = 'tomstelk'
zooplaPaths={'Price':'//a[@class="listing-results-price text-price" and string-length(@data-ga-category)=0]/text()[normalize-space()]',
                'Address':'//a[@class="listing-results-address" and string-length(@data-ga-action)=0]/text()[normalize-space()]',
                'ID':'//img[@itemprop="contentUrl"]/@data-ajax'}
zoopsNextPath='//link[@rel="next"]/@href'
zooplaURL="http://www.zoopla.co.uk/for-sale/property/${NumBeds}-bedrooms/${Geog}/?include_retirement_homes=false&include_shared_ownership=false&new_homes=include"
zooplaTable='ZooplaPrices'
