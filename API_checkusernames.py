from bs4 import BeautifulSoup
import requests
from threading import Thread

def thread_search(service, username, results, i):
    while True:
        try:
            req = requests.get('http://checkusernames.com/usercheckv2.php?target=' + service + '&username=' + username, headers={'X-Requested-With': 'XMLHttpRequest'})
            if (req.content.split('|')[0] == "2"): # found
                results[i] = service
            break
        except Exception, e:
            # print e
            pass

class CheckUsernames(object):

    def __init__(self):
        self.services = []
        req = requests.get('http://checkusernames.com/')
        soup = BeautifulSoup(req.content)
        services = soup.findAll('li', attrs={'class': 'socialdeets'})
        for service in services:
            self.services.append(service['id'].replace(' ', ''))

    def search(self, username):
        threads = [None] * len(self.services)
        results = [None] * len(self.services)

        for i in range(len(self.services)):
            threads[i] = Thread(target=thread_search, args=(self.services[i], username, results, i))
            threads[i].start()

        # do some other stuff
        for i in range(len(threads)):
            threads[i].join()

        return [x for x in results if x is not None]