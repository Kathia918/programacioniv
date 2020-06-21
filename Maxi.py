#parcial_III
from facebook_scraper import get_posts
import csv

face = csv.writer(open('Maxi.csv','w'))
face.writerow(['POST_ID','TEXTO','LIKES','IMAGE'])

for post in get_posts('ferremaxi ', pages=7, ):
    #print(post.keys())
    print(post['post_id'], post['text'], post['likes'], post['image'], sep="-")
    try:
        face.writerow([post['post_id'], post['text'], post['likes'], post['image']])
    except:
        None