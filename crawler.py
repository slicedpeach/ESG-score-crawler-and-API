import requests
import threading
from csv import DictWriter

MAX_LIMIT = 100
PAGE_URL = "https://www.refinitiv.com/en/sustainable-finance/esg-scores"
request = requests.Session()
request.headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

res = request.get(PAGE_URL)
res.raise_for_status()


def load_page():
    """load website"""

    return


def get_all_company_records():
    """get all companies in the refinitiv search database"""
    search_suggestions_url = "https://www.refinitiv.com/bin/esg/esgsearchsuggestions"
    res = request.get(search_suggestions_url)
    res.raise_for_status()

    company_json_records = res.json()
    companies = {}
    for record in company_json_records:
        comp_name = record["companyName"].lower()
        comp_ricCode = record["ricCode"]
        companies[comp_name] = comp_ricCode
    return companies


def search(searched_keyword, companies):
    """returns list of company ric codes found"""
    found_counter = 0
    found_company_rics = []
    for compname in list(companies.keys()):
        if searched_keyword in compname:
            found_counter += 1
            found_company_rics.append(companies[compname])
            
        if(found_counter >= MAX_LIMIT):
            break
    return found_company_rics


def get_all_esg_scores(company_ric):
    query = "https://www.refinitiv.com/bin/esg/esgsearchresult?ricCode="+company_ric
    res = request.get(PAGE_URL)
    res.raise_for_status()
    res = request.get(query)
    res.raise_for_status()
    all_esg_scores = res.json()
    return all_esg_scores


def get_desired_esg_scores(company_ric, company_records):
    print(company_ric)
    all_esg_scores = get_all_esg_scores(company_ric)
    company_rank = all_esg_scores["industryComparison"]["rank"]
    total_industries = all_esg_scores["industryComparison"]["totalIndustries"]
    esgScore = all_esg_scores["esgScore"]["TR.TRESG"]["score"]
    environmental_esgScore = all_esg_scores["esgScore"]["TR.EnvironmentPillar"]["score"]
    social_esgScore = all_esg_scores["esgScore"]["TR.SocialPillar"]["score"]
    governance_esgScore = all_esg_scores["esgScore"]["TR.GovernancePillar"]["score"]

    scraped_esg_scores = {}
    company_name_index = list(company_records.values()).index(company_ric)
    company_name = list(company_records.keys())[company_name_index]
    scraped_esg_scores["name"] = company_name
    scraped_esg_scores["ric"] = company_ric
    scraped_esg_scores["rank"] = f"{company_rank} / {total_industries}"
    scraped_esg_scores["esg"] = esgScore
    scraped_esg_scores["environmental"] = environmental_esgScore
    scraped_esg_scores["social"] = social_esgScore
    scraped_esg_scores["governance"] = governance_esgScore

    esgscores.append(scraped_esg_scores)


company_records = get_all_company_records()
keyword = input("enter keyword: ")
esgscores = []
found_rics = search(keyword, company_records)
thread_list = []
print("getting esg scores...")
for ric in found_rics:
    thread = threading.Thread(
        target=get_desired_esg_scores, args=(ric, company_records))
    thread_list.append(thread)
for thread in thread_list:
    thread.start()
for thread in thread_list:
    thread.join()

keys = esgscores[0].keys()
csvfile = open("esgscores.csv", "w")
dict_writer = DictWriter(csvfile,keys)
dict_writer.writeheader()
dict_writer.writerows(esgscores)
csvfile.close()
print("esg scores exported to csv file! you can load the csv file into the API by running 'python manage.py load_csv'.")
