from mongo_data.repo.movie_repo import store_movies, get_all, find


def extract_data():
    with open('./raw_data/movie_titles_metadata.txt') as movie_data:
        lines = []

        for line in movie_data:
            line = line.strip()
            line_data = line.split(' +++$+++ ')
            line_dict = {
                'movie_id': line_data[0],
                'movie_title': line_data[1].title(),
                'movie_year': int(line_data[2]),
                'IMDB_rating': float(line_data[3]),
                'IMDB_votes': int(line_data[4]),
                'genres': line_data[5][1:-2].replace("'", "").split(', ')
            }
            lines.append(line_dict)

    store_movies(lines)


def main():
    #extract_data()

    all_movies = find(movie_year=1961)
    print(all_movies)


if __name__ == '__main__':
    main()
