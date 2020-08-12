import argparse

# msg = "Provide your Malt username and your Malt password, so the script can login to your account"

# class custom_parser(argparse.ArgumentParser):
#     def __init__(self, msg):
#         msg = "Provide your Malt username and your Malt password, so the script can login to your account"
#         argparse.ArgumentParser(msg)
#         #self.description = msg


# Initialize parser
msg = "Provide your Malt username and your Malt password, so the script can login to your account"
parser = argparse.ArgumentParser(description = msg)
# parser.add_argument('MALT_USERNAME', help='Your Malt username (should be your email address)', type=str, required=True)
# parser.add_argument('MALT_PASSWORD', help='Your Malt password', type=str, required=True)
# ,'--malt_username'
# ,'--malt_password'


parser.add_argument('-u','--MALT_USERNAME', metavar='',help='Your Malt username (should be your email address)', type=str, required=True)
parser.add_argument('-pwd','--MALT_PASSWORD', metavar='', help='Your Malt password', type=str, required=True)
parser.add_argument('-name','--YOUR_MALT_FULL_NAME', metavar='', help='The full name that identifies you on your Malt profile', type=str, required=True)
parser.add_argument('-k','--MALT_SEARCH_KEYWORDS', metavar='', help='The list of keywords you want to search in Malt', type=list, required=True)
parser.add_argument('-l','--MALT_SEARCH_LOCATION', metavar='', help='The location you want to search in Malt', type=str, required=True)
args = parser.parse_args()

MALT_USERNAME = args.MALT_USERNAME
MALT_PASSWORD = args.MALT_PASSWORD
MALT_FULL_NAME = args.YOUR_MALT_FULL_NAME
MALT_SEARCH_KEYWORDS = args.MALT_SEARCH_KEYWORDS
MALT_SEARCH_LOCATION = args.MALT_SEARCH_LOCATION
