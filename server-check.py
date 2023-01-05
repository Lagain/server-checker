import requests

websites = [
    "https://www.twitter.com",
    "https://www.reddit.com",
    "https://store.steampowered.com"
]

statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}


# Loop through websites list and print status codes
for url in websites:
    try:
        webResponse = requests.get(url)
        print(url, statuses[webResponse.status_code])
    except:
        print(url, statuses[webResponse.status_code])
