import requests
from bs4 import BeautifulSoup

class year:
	def __init__(self, year) -> None:
		self.year = year
		self.base_url = f"http://ergast.com/api/f1/{self.year}"

class constructors(year):

	def constructors_func(self):
		constructors = f"{self.base_url}/constructors"
		site = requests.get(constructors)
		siteSRC = site.content

		soup = BeautifulSoup(siteSRC, 'html.parser')
		teams = soup.find_all('name')

		## BULK GET CONSTRUCTORS ##
		val = []
		for team in teams:
			val.append(tuple(team))
		return val

class drivers(year):

	def driver_names(self):
		drivers = f"{self.base_url}/drivers"
		site = requests.get(drivers)
		siteSRC = site.content
		soup = BeautifulSoup(siteSRC, 'html.parser')

		given_name  = (soup.find_all('givenname'))
		family_name = (soup.find_all('familyname'))

		## BULK GET DRIVERS ##
		firstname = []
		for name in given_name:
			firstname.append(name.text)

		surname = []
		for name in family_name:
			surname.append(name.text)

		formatnames = zip(firstname, surname)
		return list(formatnames)
