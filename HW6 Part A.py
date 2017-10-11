# Joseph Stempel

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

my_sum = 0

tags = soup('span')
for tag in tags:
    
    
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
   

    my_sum = my_sum + int(tag.contents[0])
    print(my_sum)