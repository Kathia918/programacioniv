#parcial_III
from facebook_scraper import get_posts
import csv

face = csv.writer(open('Biblioteca.csv','w'))
face.writerow(['POST_ID','TEXTO','LIKES'])

for post in get_posts('Bibliotecaugb ', pages=10, ):
    #print(post.keys())
    print(post['post_id'], post['text'], post['likes'])
    try:
        face.writerow([post['post_id'], post['text'], post['likes']])
    except:
        None
