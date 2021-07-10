import requests
import sys

"""
Print all Subscribie page urls to standard out
- subscribie pages endpoint
- ghost blog pages (api key needed- find by logging into teh ghost blog, Integrations -> api)  # noqa
- wordpress pages endpoint
- wordpress posts endpoint

Usage:
. venv/bin/activate && python3 app.py <ghost-api-key>
"""

links = []

wordpress_pages = requests.get(
    "https://subscriptionwebsitebuilder.co.uk/p/wp-json/wp/v2/pages"
)

pages = wordpress_pages.json()
for page in pages:
    links.append(page["link"])


worpress_posts = requests.get(
    "https://subscriptionwebsitebuilder.co.uk/p/wp-json/wp/v2/posts"
)

posts = worpress_posts.json()
for post in posts:
    links.append(post["link"])

subscribie_pages = requests.get(
    "https://subscriptionwebsitebuilder.co.uk/api/v1/pages"
)  # noqa: E501

pages = subscribie_pages.json()
for page in pages:
    links.append(page["url"])

api_key = sys.argv[1]
ghost_posts = requests.get(
    f"https://subscriptionwebsitebuilder.co.uk/blog/ghost/api/v3/content/posts/?key={api_key}&limit=1000"  # noqa: E501
)
posts = ghost_posts.json()["posts"]
for post in posts:
    links.append(post["url"])

for link in links:
    print(link)
