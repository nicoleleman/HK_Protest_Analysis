import csv
import requests

after = ''
with open('hk_protest_articles.csv', 'w') as f:
    fieldnames = ['socialHeadline', 'headline', 'urlAlias', 'updatedDate']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(10):
        url = 'https://apigw.scmp.com/content-delivery/v1?operationName=gettopicbyentityuuid&variables={"latestContentsLimit":50,"latestOpinionsLimit":50,"entityUuid":"21363753-95b4-43cc-bf62-3fd61ff77877","articleTypeId":"012d7708-2959-4b2b-9031-23e3d025a08d","applicationIds":["2695b2c9-96ef-4fe4-96f8-ba20d0a020b3"],"after":"'+after+'"}&extensions={"persistedQuery":{"version":1,"sha256Hash":"e1586e5b5b2f1f63a3d84ec54864eab377d6291c88270911bbc2a76e26addab9"}}'
        print('>>>>', i, after)
        headers = {'apikey': 'MyYvyg8M9RTaevVlcIRhN5yRIqqVssNY'}
        resp = requests.get(url, headers=headers)
        data = resp.json()['data']
        page_info = data['topic']['latestContentsWithCursor']['pageInfo']
        items = data['topic']['latestContentsWithCursor']['items']
        after = str(page_info['endCursor'])

        for item in items:
            writer.writerow({'socialHeadline':  item['socialHeadline'], 'headline': item['headline'], 'urlAlias': item['urlAlias'], 'updatedDate': item['updatedDate']})



