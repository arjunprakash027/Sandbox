from scrapper_utils import (
    setup_chrome_driver,
    scrapper_pipeline,
    extract_content
)

import os
import json
from lxml import html
import pandas as pd

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
                "filename" : f"company_names_and_urls/page_{page_number}.json",
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

    directory = "./data/json/company_names_and_urls"

    all_links = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory,filename)

        with open(file=filepath,mode='r',encoding='utf-8') as file:
            js_file = json.load(file)
            all_links.extend(js_file['company_links'])
            
    for individual_company in all_links:
        company_name = individual_company.split("/")[2].split(".")[1]

        steps = {
        "get": f"{base_url}{individual_company}",
        "sleep": 1,
        "click": "//button[@id='truste-consent-required']",
        #"save": "single_company.html",
        "extract_and_save": {
            "filename": f"company_details/{company_name}.json",
            "xpaths": {
                "principal name":"//span[@name='key_principal']/span[1]/text()",
                "industry":"//span[@name='industry_links']//a/text()",
                "address": "//span[@name='company_address']//a/text()",
                "address_url": "//span[@name='company_address']//a/@href",
                "company_website": "//span[@name='company_website']//a/@href"
            }
        },
        }

        driver = scrapper_pipeline(
            driver=driver,
            steps=steps
        )

def combine_data() -> None:
    directory = "./data/json/company_names_and_urls"

    all_links = []
    all_companies = []
    all_principles = []
    all_industries = []
    all_addresses = []
    all_addresses_url = []
    all_company_website = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory,filename)

        with open(file=filepath,mode='r',encoding='utf-8') as file:
            js_file = json.load(file)
            all_links.extend(js_file['company_links'])
            all_companies.extend(js_file['company_names'])


    for individual_company in all_links:
        company_name = individual_company.split("/")[2].split(".")[1] 
        json_path = f"./data/json/company_details/{company_name}.json"

        with open(file=json_path,mode='r',encoding='utf-8') as f:
            print(individual_company)
            data_file = json.load(f)
            principal = data_file['principal name']
            industry = data_file['industry']
            address = data_file['address']
            address_url = data_file['address_url']
            company_website = data_file['company_website']

            if principal:
                all_principles.append(principal[0])
            else:
                all_principles.append("")

            if industry:
                all_industries.append(f"{industry[0]},{industry[1]}")
            else:
                all_industries.append("")
            
            if address:
                all_addresses.append(address[0])
            else:
                all_addresses.append("")

            if address_url:
                all_addresses_url.append(address_url[0])
            else:
                all_addresses_url.append("")
            
            if company_website:
                all_company_website.append(company_website[0])
            else:
                all_company_website.append("")

    df = pd.DataFrame(
        {
            "companies":all_companies,
            "links":all_links,
            "principal": all_principles,
            "industry": all_industries,
            "address": all_addresses,
            "address_url": all_addresses_url,
            "company_website": all_company_website
        }
    )

    df.to_csv("final.csv")


if __name__ == '__main__':
    
    #scrape_data()
    #scrape_individual_companies()
    combine_data()
