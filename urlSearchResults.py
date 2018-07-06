__author__ = 'tomstelk'
import urlHolder
from string import Template
class urlSearchResults(urlHolder.urlHolder):
    def __init__(self, templateURL, searchParams):
        self.templateURL=templateURL

        for key in searchParams:
            if not key in templateURL:
                raise Exception('Search parameter not in URL')

        s=Template(templateURL)
        urlHolder.urlHolder.__init__(self, s.substitute(searchParams))