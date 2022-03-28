import argparse
from ast import arg, parse
from textwrap import indent
import requests
import json
from others import *

baseURL="https://graph.facebook.com/v12.0/"
id=""
path=""
token =""

parser = argparse.ArgumentParser(
    prog="quick-gapi",
    description="Take arguments within CLI"
    )

parser.add_argument("-i","--id", type=str, help="This is the page, profile, group or post ID" )
parser.add_argument("-t","--token", type=str, help="Token taken from the graph API tool provided by Facebook Graph API webpage")
parser.add_argument("-p","--path", type=str, help="API URL path to access it's features. For example: quick-gapi -p insights/...")
parser.add_argument(
    "-v",
    "--api-version",
    type=str,
    default="v12.0",
    help="Specify the GraphAPI version (DEFAULT= \"v12.0\")",
)

args = parser.parse_args()

if vars(args).get("token") == None or vars(args).get("id") == None :
    print("Please provide a token with -t or --token switch and object ID with -i or --id switch")
    print('exiting...')
    exit()



id = vars(args).get("id")

token = vars(args).get("token")

#eliminate first / within the path
if vars(args).get("path")[0] == '/':
   path = vars(args).get("path")[1:]
else:
    path = vars(args).get("path")

requestURL=baseURL + id + "/" + path + "?access_token=" + token

r = requests.get(requestURL)
data = r.text
parsed = json.loads(data)

print (json.dumps(parsed, indent=4 ))

#this is just some additioal in case path "posts" is used.
if path == "posts":
    prtid = query_yes_no("Do you want to print out the posts ID ?")
    if prtid == True:
        print("Printing all IDs: ")
        posts = parsed["data"]
        post_id = [None] * len(posts)
        for x in range(len(posts)):
            
            post_id[x]=(posts[x])["id"] 
            print(post_id[x])











