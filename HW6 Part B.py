# Joseph Stempel

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

my_count = int(input('Enter count - '))
my_position = (int(input('Enter position '))-1)


def find_my_position(url, my_position):
	print ('Retrieving: ' + str(url))
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	my_tags = soup.find_all('a')
	return my_tags[my_position].get('href')

for item in range(my_count):
	url = find_my_position(url, my_position)

final_html = urllib.request.urlopen(url, context=ctx).read()
final_soup = BeautifulSoup(final_html, 'html.parser')
print (final_soup.title.string.split(' ')[2])




