import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://cutm.icloudems.com/corecampus/student/attendance/myattendance.php?month=12&admno=&acadyear=2021-2022&proctor=proctor').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

nav = soup.nav

for url in nav.find_all("a"):
    print(url.get("href"))

body = soup.body
for paragraph in body.find_all("p"):
    print(paragraph.text)

for div in soup.find_all("div", class_="body"):
    print(div.text)
