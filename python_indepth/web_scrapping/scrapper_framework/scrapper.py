from scrapper_utils import (
    setup_chrome_driver,
    scrapper_pipeline,
    extract_content
)

import os
from lxml import html

def scrape_data() -> None:
   # Create a chrome driver 
    driver = setup_chrome_driver()

    base_url = 'https://www.dnb.com'

    steps_initial = {
    "get": f"{base_url}/business-directory/company-information.manufacturing.in.tamil_nadu.sriperumbudur.html",
    "click": '/html/body/div[2]/div[2]/div/div[3]/div[3]/div/button[3]',
    "sleep": 2
    }

    driver = scrapper_pipeline(
        driver=driver,
        steps=steps_initial
    )

    for page_number in range(1,5):
        
        current_steps = {
            "save": f"page_source_{page_number}.html",
            "extract_and_save":{
                "filename" : f"page_{page_number}.json",
                "xpaths" : {
                "company_names":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/text()", 
                "company_links":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/@href" 
            } 
            },
            "click": "//ul[@class='integratedSearchPaginationPagination']/li[@class='next']/a",
            "sleep": 3
        }

        driver = scrapper_pipeline(
            driver=driver,
            steps=current_steps
        )

    driver.quit() 

def scrape_individual_companies() -> None:
    driver = setup_chrome_driver()

    base_url = 'https://www.dnb.com'

    steps_initial = {
    "get": f"{base_url}/business-directory/company-profiles.spstech_engineering_private_limited.6c80648b5dabfd11232a67d26b0f8172.html",
    "sleep": 300,
    "click": '/html/body/div[2]/div[2]/div/div[3]/div[3]/div/button[3]',
    "sleep": 2,
    "save": "single_company.html"
    }

    driver = scrapper_pipeline(
        driver=driver,
        steps=steps_initial
    )

def extract_data() -> None:

    html_files = {}    
    directory = "./data/html"
    for filename in os.listdir(directory):
        filepath = os.path.join(directory,filename)

        with open(file=filepath,mode='r',encoding='utf-8') as file:
            tree = html.parse(file)
            # html_content = file.read()
            html_files[filename] = tree
    
    first_page = html_files['page_source_1.html']

    xpaths = {
        "company_names":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/text()", 
        "company_links":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/@href" 
    }

    extract_and_save = {
        "filename" : "page1.json",
        "xpaths" : {
        "company_names":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/text()", 
        "company_links":"//div[@id='companyResults']//div[@class='col-md-12 data']//div[@class='col-md-6']/a/@href" 
    } 
    }

    out = extract_content(tree=first_page,xpaths=xpaths)

    print(out)


if __name__ == '__main__':
    
    scrape_data()
    #scrape_individual_companies()
