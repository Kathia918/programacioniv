#parcial_III
from facebook_scraper import get_posts
import csv

face = csv.writer(open('ugbstore.csv','w'))
face.writerow(['POST_ID','TEXTO','LIKES'])

for post in get_posts('ugbstoreoficial', pages=5, ):
    #print(post.keys())
    print(post['post_id'], post['text'], post['likes'])
    try:
        face.writerow([post['post_id'], post['text'], post['likes']])
    except:
        None
