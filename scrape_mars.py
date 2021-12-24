## Step 2 - MongoDB and Flask Application

##Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

#* Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

#* Next, create a route called `/scrape` that will import your `scrape_mars.py` script and #call your `scrape` function.

#  * Store the return value in Mongo as a Python dictionary.

#* Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.

#* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.


from splinter import Browser
import os 
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=True)

def scrapping():
    browser = init_browser():
    
    
    #NASA Mars News
    nasa_mars_news = 'https://redplanetscience.com/'
    browser.visit(nasa_mars_news)
    nasa_mars_news_html = browser.html
    nasa_mards_soup = bs(nasa_mars_news_html,'html.parser')
    
    mars_news_title = nasa_mards_soup.find('div',class_='content_title').text
    news_p = nasa_mards_soup.find('div', class_='article_teaser_body').text
    
    #PL Mars Space Images - Featured Image
    mars_space_website = 'https://spaceimages-mars.com'
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars1.jpg'
    browser.visit(featured_image_url)
    mars_html_image = browser.html
    mars_soup = bs(mars_html_image, 'html.parser')
    featured_image = mars_soup.find('div', class_ = 'carousel_items')
    link = featured_image.article['style']
    
    
    #Mars Facts
    url_mars_facts = 'https://galaxyfacts-mars.com'
    table_1 = pd.read_html(url_mars_facts)
    table_1_html = table_1_df.to_html()
    table_1_html = table_1_html.replace('\n', '')
    
    
    #Mars Hemispheres
    mars_hemispheres = 'https://marshemispheres.com'
    browser.visit(mars_hemispheres)
    mars_hemispheres_html = browser.html
    hemis_soup = bs(mars_hemispheres_html,'html.parser')
    
    
    full_mars_data = {
        "News" : Nasa_Mars_News,
        "Image" : Nasa_Mars_Image,
        "Facts" : Nasa_Mars_Facts,
        "Hemispheres" : Nasa_Mars_Hemispheres         
        
    }
    
    
    return full_mars_data 





    
    
    
    
    
    
    
    
    



    
    
    

