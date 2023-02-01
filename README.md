# Goodreads_Scraper

These Python scripts can be used to scrape book metadata from Goodreads.

The motivation for developing this tool is because the Goodreads API is no longer available. Also, I wanted to improve on other Goodreads scrapers as I found these to work on the Goodreads id to be inputted by the user, requiring this to be manually looked up on the Goodreads site.

Instead, this tool uses the search bar on Goodreads to find the id, meaning that only key search terms (i.e. title/author name) are needed as an input. 

<br><br>

### Input

This script requires the search terms in a csv file. The search terms should include title and, preferably, be specific such as including author name.

<br><br>

### Output

This script outputs a JSON file for each book with the following information:

- book title
- book ID
- author name
- year the book was first published
- rating
- count of ratings
- rating distribution
- link to cover image
- link to book on Goodreads
