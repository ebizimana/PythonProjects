from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movie_names = []
movie_ranks = []

for movie in movie_tags:
    name = movie.getText().split()[1:]
    name = ' '.join(name)
    try:
        rank = int(movie.getText().split(")")[0])
    except ValueError:
        rank = int(movie.getText().split(":")[0])

    movie_names.append(name)
    movie_ranks.append(rank)


movies = {movie_ranks[index]: movie_names[index] for index in range(len(movie_ranks))}
movies = dict(sorted(movies.items()))

with open("movies.txt", "w") as file:
    for rank, name in movies.items():
        file.write(f"{rank}) {name}\n")
