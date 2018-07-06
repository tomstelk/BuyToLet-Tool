__author__ = 'tomstelk'

airBnBTable='AirBnBPrices'
htmlClass='rich-toggle wish_list_button wishlist-button'
airBnBSearchParams={'Geog':'', 'numGuests':'','checkIn':'02-08-2015', 'checkOut':'09-08-2015'}
airBnBPaths={'Price':'//span[@class="' + htmlClass + '"]/@data-price',
                'Description':'//span[@class="' + htmlClass + '"]/@data-name',
                'ID':'//span[@class="' + htmlClass + '"]/@data-listing_id',
                'StarRating':'//span[@class="' + htmlClass + '"]/@data-star_rating',
                'Address':'//span[@class="' + htmlClass + '"]/@data-address'}
airBnBNextPath='//link[@rel="next"]/@href'
airBnBURL="https://www.airbnb.co.uk/s/london-${Geog}?checkin=${checkIn}&checkout=${checkOut}&guests=${numGuests}&room_types%5B%5D=Entire+home%2Fapt"

