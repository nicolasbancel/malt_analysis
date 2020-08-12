############################
# Testing :
#
############################


############################
# External libraries
############################

import urllib.parse
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

import argparse

############################
# Local libraries
############################

from custom_driver import *
import data_cleaning as dc
import html_parser as hp

############################
# Variables
############################

MALT_URL = 'https://www.malt.fr/'
EXECUTION_TIME = datetime.now().strftime('%Y-%m-%d %H:%M')
EXECUTION_DAY = datetime.now().strftime('%Y%m%d')
# del freelance_info
# del skills_df

try:
    freelance_info.shape
except NameError:
    freelance_info = pd.DataFrame(columns=['ranking',
                                           'page_number',
                                            'full_name',
                                            'location',
                                            'freelance_url',
                                            'rating',
                                            'num_missions',
                                            'num_recos',
                                            'tjm',
                                            'badge',
                                            'title',
                                            'dispo',
                                            'dispo_details',
                                          'search_keyword',
                                          'search_location',
                                          'execution_time'])

try:
    skills_df.shape
except NameError:
    skills_df = pd.DataFrame(columns=['full_name',
                                  'skill',
                                  'skill_ranking',
                                 'skill_certified',
                                 'skill_comment',
                                  'search_keyword',
                                  'search_location',
                                  'execution_time'])


############################
# Extracting information
############################

msg = "Provide your Malt username and your Malt password, so the script can login to your account"
parser = argparse.ArgumentParser(description = msg)
parser.add_argument('-u','--MALT_USERNAME', metavar='',help='Your Malt username (should be your email address)', type=str, required=True)
parser.add_argument('-pwd','--MALT_PASSWORD', metavar='', help='Your Malt password', type=str, required=True)
parser.add_argument('-name','--MALT_FULL_NAME', metavar='', help='The full name that identifies you on your Malt profile', type=str, required=True)
parser.add_argument('-k','--MALT_SEARCH_KEYWORDS', metavar='', help='The list of keywords you want to search in Malt', type=str, required=True, nargs='+')
parser.add_argument('-l','--MALT_SEARCH_LOCATION', metavar='', help='The location you want to search in Malt', type=str, required=True)
args = parser.parse_args()

MALT_USERNAME = args.MALT_USERNAME
MALT_PASSWORD = args.MALT_PASSWORD
MALT_FULL_NAME = args.MALT_FULL_NAME
MALT_SEARCH_KEYWORDS = args.MALT_SEARCH_KEYWORDS
#print(args.MALT_SEARCH_KEYWORDS)
MALT_SEARCH_LOCATION = args.MALT_SEARCH_LOCATION


# MALT_USERNAME='nicolas.bancel@gmail.com'
# MALT_PASSWORD='Janson0668040115!'
# MALT_SEARCH_KEYWORDS = ['Data Scientist', 'Data Engineer']
# MALT_SEARCH_LOCATION = 'Paris, France'

# https://stackoverflow.com/questions/9398065/python-argh-argparse-how-can-i-pass-a-list-as-a-command-line-argument
# python main.py --MALT_USERNAME 'nicolas.bancel@gmail.com' --MALT_PASSWORD 'Janson0668040115!' --MALT_SEARCH_KEYWORDS 'Data Scientist' 'Data Engineer' --MALT_SEARCH_LOCATION 'Paris, France' --MALT_FULL_NAME 'Nicolas Bancel'
#python main.py --MALT_USERNAME 'nicolas.bancel@gmail.com' --MALT_PASSWORD 'Janson0668040115!' --MALT_SEARCH_KEYWORDS "['Data Scientist','Data Engineer']" --MALT_SEARCH_LOCATION 'Paris, France' --MALT_FULL_NAME 'Nicolas Bancel'

if __name__ == '__main__':
    print(MALT_USERNAME)
    print(MALT_PASSWORD)
    print(MALT_FULL_NAME)
    print(MALT_SEARCH_KEYWORDS)
    print(MALT_SEARCH_LOCATION)

    malt_driver = Custom_Webdriver(MALT_URL = MALT_URL,MALT_USERNAME=MALT_USERNAME,MALT_PASSWORD=MALT_PASSWORD)
    malt_driver.generate_browser()
    malt_driver.login()

    for MALT_SEARCH_KEYWORD in MALT_SEARCH_KEYWORDS:

        skills_df_specific_search = pd.DataFrame(columns = skills_df.columns)
        freelance_info_specific_search = pd.DataFrame(columns = freelance_info.columns)

        malt_driver.search(MALT_SEARCH_KEYWORD, MALT_SEARCH_LOCATION)
        time.sleep(10)
        ## STARTING TO PARSE
        print('About to parse pages for keyword : {}'.format(MALT_SEARCH_KEYWORD))

        # Number of pages for the search
        num_pages = malt_driver.getting_num_pages()
        print('Number of pages : {}'.format(num_pages))

        # Make it start at 1 // Not at 0 (otherwise it's doubling it)
        #for page_number in range(1,3):
        #for page_number in range(3,4):

        #for page_number in range(1,num_pages+1):
        for page_number in range(1,2):
            print('Parsing page number {}'.format(page_number))
            url = malt_driver.generate_paged_url_and_go(page_number)
            print('About to parse URL {}'.format(url))
            #freelance_list, url = malt_driver.getting_freelance_list()
            freelance_list = malt_driver.getting_freelance_list()

            for index, freelance in enumerate(freelance_list):
                ##### FREELANCE ATTRIBUTES #####
                dict_freelance, full_name = hp.freelance_attributes(freelance, index, page_number)
                freelance_info_specific_search = freelance_info_specific_search.append(dict_freelance, ignore_index=True)
                ##### FREELANCE SKILLS ATTRIBUTES #####
                skills = freelance.find_all('span','malt-tag')
                skill_number = 1

                for skill in skills:
                    if skill.text.strip().startswith('+') is False:
                        dict_skills = hp.freelance_skills(skill, full_name, skill_number)
                        skills_df_specific_search = skills_df_specific_search.append(dict_skills, ignore_index=True)
                        skill_number += 1

        freelance_info_specific_search['search_keyword'] = MALT_SEARCH_KEYWORD
        freelance_info_specific_search['search_location'] = MALT_SEARCH_LOCATION
        freelance_info_specific_search['execution_time'] = EXECUTION_TIME

        skills_df_specific_search['search_keyword'] = MALT_SEARCH_KEYWORD
        skills_df_specific_search['search_location'] = MALT_SEARCH_LOCATION
        skills_df_specific_search['execution_time'] = EXECUTION_TIME

        ##### APPENDING TO FINAL DATAFRAME #####

        freelance_info = freelance_info.append(freelance_info_specific_search)
        skills_df = skills_df.append(skills_df_specific_search)

    dc.refactoring_data(freelance_info)
    freelance_info.to_csv(f'freelance_info_{EXECUTION_DAY}.csv')
    skills_df.to_csv(f'freelance_skills_{EXECUTION_DAY}.csv')
