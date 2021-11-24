import requests
from bs4 import BeautifulSoup

class constructors():

    year = 1986
    base_url = f"http://ergast.com/api/f1/{year}"

    def constructors_func(self):
        Constructors = f"{self.base_url}/constructors"
        site = requests.get(Constructors)
        siteSRC = site.content
        # print(siteSRC)

        ## API DATA PULL ##
        soup = BeautifulSoup(siteSRC, 'html.parser')
        teams = soup.find_all('name')

        ## BULK ADD CONSTRUCTORS ##
        val = []
        for team in teams:
            val.append(tuple(team))
        return val


## TESTING YEARS INPUT ##

# year = 2021
# Constructors = f"http://ergast.com/api/f1/{year}/constructors"

# site = requests.get(Constructors)
# siteSRC = site.content

# soup = BeautifulSoup(siteSRC, 'html.parser')
# print(soup.find_all('name'))
# soup = BeautifulSoup(siteSRC, 'html.parser')
# for year in soup.find_all('constructortable'):
#     print(year['season'])

class drivers:

    def driver_names(self):
        year = 1986
        Constructors = f"http://ergast.com/api/f1/{year}/drivers"

        site = requests.get(Constructors)
        siteSRC = site.content
        soup = BeautifulSoup(siteSRC, 'html.parser')

        given_name  = (soup.find_all('givenname'))
        family_name = (soup.find_all('familyname'))

        firstname = []
        for name in given_name:
            firstname.append(tuple(name))
            return firstname

        surname = []
        for name in family_name:
            surname.append(tuple(name))
            return surname
