import csv
import requests
from datetime import datetime

# The variable after stores the endCursor of the previous page
after = ''

with open('scmp_articles.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['socialHeadline', 'headline', 'urlAlias', 'updatedDate'])

    # This for loop gets the site content using an api call
    for i in range(10):
        url = 'https://apigw.scmp.com/content-delivery/v1?operationName=gettopicbyentityuuid&variables={"latestContentsLimit":50,"latestOpinionsLimit":50,"entityUuid":"21363753-95b4-43cc-bf62-3fd61ff77877","articleTypeId":"012d7708-2959-4b2b-9031-23e3d025a08d","applicationIds":["2695b2c9-96ef-4fe4-96f8-ba20d0a020b3"],"after":"'+after+'"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"e1586e5b5b2f1f63a3d84ec54864eab377d6291c88270911bbc2a76e26addab9"}}'

        print('>>>>', i, after)
        headers = {'apikey': 'MyYvyg8M9RTaevVlcIRhN5yRIqqVssNY'}
        resp = requests.get(url, headers=headers)
        data = resp.json()['data']
        page_info = data['topic']['latestContentsWithCursor']['pageInfo']
        items = data['topic']['latestContentsWithCursor']['items']
        # assigns the endcursor for each section to the variable after
        after = str(page_info['endCursor'])

        try:
            for item in items:
                # unix timestamp included the millisecond so divide by 1000 is required
                converted_date = datetime.utcfromtimestamp(item['updatedDate']/1000).strftime('%Y-%m-%d %H:%M:%S')
                social_headline = '"' + item['socialHeadline'] + '"'
                headline = '"' + item['headline'] + '"'
                new_url = 'https://scmp.com/print' + str(item['urlAlias'])
                writer.writerows([social_headline, headline, new_url, converted_date])
        except Exception as e:
            writer.writerows(['', '', '', ''])
