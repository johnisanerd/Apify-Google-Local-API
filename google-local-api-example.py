"""
Example: call the Google Local API Apify Actor from Python.

Returns the businesses Google shows in the local pack of its Search results for
a query and location, with rating, reviews, address, phone, hours, GPS
coordinates, and a stable place_id. One dataset item is returned per page.

This example fetches a single page so the first run is inexpensive; each page is
billed separately. Raise max_pages for deeper coverage.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
Set it in a .env file (see .env.example) or export APIFY_API_TOKEN.
"""

import os

from apify_client import ApifyClient
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN")
if not APIFY_API_TOKEN:
    raise SystemExit(
        "APIFY_API_TOKEN is not set. Copy .env.example to .env and add your key, "
        "or run: export APIFY_API_TOKEN=your_api_key_here"
    )

client = ApifyClient(APIFY_API_TOKEN)

run_input = {
    "q": "coffee",
    "location": "Austin, Texas, United States",
    "max_pages": 1,
}

print(f"Google Local search: {run_input['q']} in {run_input['location']}")
run = client.actor("johnvc/google-local-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not start. Check your API token and inputs.")

# One dataset item is returned per page; each holds a local_results list.
for page in client.dataset(run.default_dataset_id).iterate_items():
    businesses = page.get("local_results", [])
    print(f"\nPage {page.get('page_number', '?')}: {len(businesses)} local businesses\n")

    for biz in businesses:
        rating = biz.get("rating")
        reviews = biz.get("reviews")
        rating_str = f"{rating} ({reviews} reviews)" if rating is not None else "no rating"
        print(f"  {biz.get('position')}. {biz.get('title')}  [{biz.get('type') or ''}]")
        print(f"     {rating_str}")
        print(f"     {biz.get('address') or ''}")
        print(f"     place_id={biz.get('place_id')}")
        print()
