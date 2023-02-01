class book_Data():
    def __init__(self, soup):
        self.soup = soup

    def get_title(self):
        title = self.soup.find('h1', class_='Text Text__title1').text
        return title

    def get_rating(self):
        try:
            rating = self.soup.find(class_='RatingStatistics__rating').text
            return rating
        except:
            return "rating not found"

    def ratings_count(self):
        try:
            ratings_count = self.soup.find('span', attrs={'data-testid': "ratingsCount"}).text.split()[0]
            return ratings_count
        except:
            return 'ratings count not found'

    def get_genres(self):
        all_ul = self.soup.find_all('ul', class_='CollapsableList')
        for genre in all_ul:
            g = genre.find_all('span', class_='Button__labelItem')
            try:
                all_genres = [g.text for g in g if g.text != '...more']
                return all_genres
            except:
                return 'Could not find genres'

    def get_author(self):
        try:
            all_authors = self.soup.find_all(class_='ContributorLink__name')
            authors = [author.text for author in all_authors[:-1]]
            return authors
        except:
            return 'author not found'

    def get_year(self):
        try:
            year = self.soup.find('p', attrs={'data-testid': "publicationInfo"}).text[-4:]
            return year
        except:
            return 'year published not found'

    def book_cover(self):
        try:
            cover = self.soup.find('img', class_='ResponsiveImage').get('src')
            return cover
        except:
            return 'cover not found'

    def rating_distribution(self):
        try:
            all_ratings = self.soup.find_all('div', class_='RatingsHistogram__labelTotal')
            ratings = [rating.text.split(')')[0].split('(')[1] for rating in all_ratings]
            ratings_dict = {'5 star': ratings[0],
                            '4 star': ratings[1],
                            '3 star': ratings[2],
                            '2 star': ratings[3],
                            '1 star': ratings[4]
                            }
            return ratings_dict
        except:
            return 'ratings not found'
