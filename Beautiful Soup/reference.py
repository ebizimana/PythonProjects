from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# get the fist anchor tag
# print(soup.a)

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")