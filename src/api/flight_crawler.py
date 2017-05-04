""" Module Docstring """

import urllib
import requests
from lxml import html

class Crawler(object):
    """ Docstring """

    def __init__(self):
        self.req = 'https://book.latam.com/TAM/dyn/air/booking/upslDispatcher'
        self.params = urllib.parse.urlencode(
            {
                'B_LOCATION_1':'FLN', 'E_LOCATION_1':'CNF', 'TRIP_TYPE':'O',
                'B_DATE_1':'201706140000', 'adults':'1', 'children':'0', 'infants':'0',
                'LANGUAGE':'BR', 'SITE':'JJBKJJBK', 'WDS_MARKET':'BR', 'MARKETING_CABIN': 'E'
            })

    def make_request(self):
        """ Docstring """
        req = requests.get(self.req, params=self.params)
        return req

    def parse_tree(self):
        """ Docstring """
        tree = html.fromstring(self.make_request().content)
        rows = tree.xpath('//*[@id="outbound_list_flight"]/tbody/tr[*]/td[5]/div/strong')

        for row in rows:
            print(row.text)

        print('')

def main():
    """ Docstring """
    crawler = Crawler()
    crawler.parse_tree()

if __name__ == "__main__":
    main()
