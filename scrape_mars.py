from splinter import Browser
import os 
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=True)

def scrapping_mars_db():
    browser = init_browser():
    
    
    #NASA Mars News
    nasa_mars_news = 'https://redplanetscience.com/'
    browser.visit(nasa_mars_news)
    nasa_mars_news_html = browser.html
    nasa_mards_soup = bs(nasa_mars_news_html,'html.parser')
    
    mars_news_title = nasa_mards_soup.find('div',class_='content_title').text
    news_p = nasa_mards_soup.find('div', class_='article_teaser_body').text
    
    #PL Mars Space Images - Featured Image
    primary_url = "https://spaceimages-mars.com"
    browser.visit(primary_url)
    image_html = browser.html
    soup_mars = bs(image_html, 'html.parser')
    image = soup_mars.find('img', class_ = 'headerimage')
    src = image["src"]
    featured_image_url = "https://spaceimages-mars.com/" + src
    
    #Mars Facts
    url_mars_facts = 'https://galaxyfacts-mars.com'
    table_1 = pd.read_html(url_mars_facts)
    table_1_html = table_1_df.to_html()
    table_1_html = table_1_html.replace('\n', '')
    
    
    #Mars Hemispheres
    hem_url = "https://marshemispheres.com/"
    browser.visit(hem_url)
    html = browser.html
    m_soup = bs(html, 'html.parser')
    main_url = soup.find_all('div', class_='item')
    titles = []
    hemisphere_images_urls = []  
    for each in main_url:
    title = each.find('h3').text
    url = each.find('a')['href']
    hem_img_url = hem_url+url
    browser.visit(hem_img_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_img_original = soup.find('div',class_='downloads')
    hemisphere_img_url=hemisphere_img_original.find('a')['href']
    img_data = dict({'title':title, 'img_url': hemisphere_img_url})
    hemisphere_img_urls.append(img_data)
    
    
    
    
    
    
    full_mars_data = {
        "News" : Nasa_Mars_News,
        "Image" : Nasa_Mars_Image,
        "Facts" : Nasa_Mars_Facts,
        "Hemispheres" : Nasa_Mars_Hemispheres         
        
    }
    
    
    return scraped_mars_data 





    
    
    
    
    
    
    
    
    



    
    
    

