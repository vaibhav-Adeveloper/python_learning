from bs4 import BeautifulSoup
import requests

request_object = requests.get("https://realpython.com/python-youtube-channels/")
# website - https://coreyms.com
html_source_code = request_object.text

soup = BeautifulSoup(html_source_code, 'lxml')
# print(soup.prettify())

# code for one section

# section = soup.find('section')
# print(section.prettify())
# yt_channel_name = section.h2.a.text
# summary = section.find('blockquote').p.text
# website_link = section.find('ul').li.a['href']
# ul_tag = section.find('ul')
# website_link = ul_tag.find_all('li')[0].a.get('href', "no link like this")
# twitter_link = ul_tag.find_all('li')[1].a.get('href', "no link like this")
# yt_link = ul_tag.find_all('li')[2].a.get('href', "no link like this")

# print(yt_channel_name)
# print(summary)
# print(website_link)
# print(twitter_link)
# print(yt_link)

# now one problem on looping is that not all youtubers have thier own website,
# so to avoid the cracking of our scrapping, we will put the website code in try-except block, to avoid crack.


# code generalised for all section
print("All famous python yt channels: \n")

for section in soup.find_all('section'):
    if(section.h2.a.text != "Chris Hawkes"):
        yt_channel_name = section.h2.a.text
        summary = section.find('blockquote').p.text
        ul_tag = section.find('ul')
        website_link = ul_tag.find_all('li')[0].a.get('href', "no link like this")
        twitter_link = ul_tag.find_all('li')[1].a.get('href', "no link like this")
        yt_link = ul_tag.find_all('li')[2].a.get('href', "no link like this")
        print(f"Youtube channel name: {yt_channel_name}")
        print(f"summary: {summary}")
        print(f"Website link: {website_link}")
        print(f"Twitter link: {twitter_link}")
        print(f"Youtube link: {yt_link}")
        print()