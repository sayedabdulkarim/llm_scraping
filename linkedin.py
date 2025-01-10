import requests

# response = requests.get('https://gist.githubusercontent.com/sayedabdulkarim/ab7e4d0dd357f3e63ee20ccf2502df59/raw/cfdc6870b0641247d0f43b1788bd56eb3a649b94/sayed_abdul.json')

# print(response.json())

def scrape_linkedin_profile( linkedin_profile_url, mock):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/sayedabdulkarim/ab7e4d0dd357f3e63ee20ccf2502df59/raw/cfdc6870b0641247d0f43b1788bd56eb3a649b94/sayed_abdul.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json"
        response = requests.get(linkedin_profile_url, timeout=10)

    data =  response.json()

    return data