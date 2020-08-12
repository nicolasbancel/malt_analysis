# Malt - Freelances Stats Analysis

[![N|Solid](https://news.malt.com/wp-content/uploads/2018/03/malt_logo_png.png)](https://www.malt.fr/)

This tool parses the Malt website and extracts, for a set of search keywords, all the information related to the freelances that show up in the results pages. There are indeed multiple "inputs" to the tool:
- Your Malt credentials
- The inputs of your search (Keyword + Location)
- Your name (for analysis about where you stand compared to other freelancers)

## Prerequisites
- Have git
- Have Python 3
- Have pip
installed on your laptop

## How to use it
- Clone the repository on your laptop
  - SSH method
```$ git clone git@github.com:nicolasbancel/malt_analysis.git```
  - HTTPS method
```$ git clone https://github.com/nicolasbancel/malt_analysis.git```
- In the malt_analysis repository you just downloaded, install the libraries needed for the script to run, executing:
```$ pip install -r requirements.txt```
- Execute the *main.py* script, with the following command line arguments:
  - **MALT_USERNAME** : your malt username, delimited with single quotes (ex: 'abc@gmail.com')
  - **MALT_PASSWORD** : your malt password, delimited with single quotes (ex: 'password123!')
  - **MALT_SEARCH_KEYWORDS** : the list of keywords you'd like to search in Malt (eg : you'd like to understand where you end up in the search results for 3 distinct keywords : 'Data Scientist' / 'Machine Learning' / 'Data Engineer'). Isolated with single quotes, NOT comma separated: just leave a space between each term. (ex: 'Data Scientist' 'Machine Learning' 'Data Engineer')
  - **MALT_SEARCH_LOCATION** : the area you'd like to search (ex: 'Paris, France')
  - **MALT_FULL_NAME** : the full name displayed on your personal Malt profile (ex: 'Zinedine Zidane')
- Actual example:
```$ python main.py --MALT_USERNAME 'abc@gmail.com' --MALT_PASSWORD 'password123!' --MALT_SEARCH_KEYWORDS 'Data Scientist' 'Machine Learning' 'Data Engineer' --MALT_SEARCH_LOCATION 'Paris, France' --MALT_FULL_NAME 'Zinedine Zidane'```

## What is the output ?
- 2 csv files :
  - **One csv with the full list of all the freelances that correspond to each search** (in the example above, there will be 3 searches: 1 with the ['Data Scientist' // 'Paris, France'] combination, 1 with the ['Machine Learning' // 'Paris, France'] combination, and 1 with the ['Data Engineer' // 'Paris, France'] combination). And their attributes (TJM / Num missions / Rating / Num recommandations / Title / Ranking in the search / Malt badge)
  - **One csv with the list of skills per freelance**, and whether or not those skills are certified by Malt
- _Coming up soon_ : a PDF that provides some stats around the freelances characteristics for each of your search (distributions of TJM / what characterizes a freelance who ends up in the first result pages etc)

## What is the process of the script ?
- Initiates a Chrome browser
- Reaches the Malt login page, and fills in the fields with the --MALT_USERNAME and --MALT_PASSWORD you provided
![Alt text](https://github.com/nicolasbancel/malt_analysis/blob/master/img/login_malt.png "Login Page - Malt")
- Once logged in, searches for the first keyword / location combination (and iterates)
![Alt text](https://github.com/nicolasbancel/malt_analysis/blob/master/img/search_malt.png "Login Page - Malt")
- Once on the result first page, parses each page with results
- Stores all the data into two dataframes (_freelance_info_ and _freelance_skills_), exported into 2 CSVs:
  - **freelance_info_YYYYMMDD.csv**
  - **freelance_skills_YYYYMMDD.csv** (YYYYMMDD being the day you run the script)
