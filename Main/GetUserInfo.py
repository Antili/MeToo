import urllib2

import shutil
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup
import os
import requests

geolocator = Nominatim()
URL_INIT = 'https://twitter.com/'
rootdir = '/media/D/Tweets/'



def parse_url(tweet_user):
    url = URL_INIT + tweet_user.strip('@')
    return url


def get_image(url, path):
    with open(path, 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print response
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)


for x in os.listdir(rootdir):
    print x
    folder = rootdir + x + '/'
    f = open(folder + 'User.txt', 'r')
    if os.path.exists(folder + 'Pics'):
        shutil.rmtree(folder + 'Pics')
    os.makedirs(folder + 'Pics')


    file_PI = open(folder + 'NumPic.txt', 'w')
    file_BI = open(folder + 'Bio.txt', 'w')
    file_JD = open(folder + 'JoinDate.txt', 'w')
    file_NL = open(folder + 'TotalLikes.txt', 'w')
    file_NFR = open(folder + 'TotalFollowers.txt', 'w')
    file_NFG = open(folder + 'TotalFollowings.txt', 'w')
    file_NT = open(folder + 'TotalTweets.txt', 'w')
    file_L = open(folder + 'Location.txt', 'w')

    count = 0
    for user in f:
        url = parse_url(user)
        try:
            response = urllib2.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html)
        except:
            location = None
            image_url = None
            num_tweets = None
            num_followings = None
            num_followers = None
            num_likes = None
            num_pic = None
            bio = None
            join_date = None

        try:
            location = soup.find('span', 'ProfileHeaderCard-locationText').text.encode('utf8').strip('\n').strip()
        except:
            print count, x, 'location', url
            location = None

        try:
            image_url = soup.find('img', 'avatar js-action-profile-avatar').attrs['src'].replace('bigger', "400x400")
            full_file_name = folder + 'Pics/' + str(count) + '.jpg'
            get_image(image_url, full_file_name)
        except:
            print count, x, 'image', url
            image_url = None

        try:
            num_tweets = soup.find('a', 'ProfileNav-stat ProfileNav-stat--link '
                                        'u-borderUserColor u-textCenter js-tooltip js-nav') \
                .attrs['title'].replace("Tweets", "").replace(",", "")
        except:
            print count, x, 'Number of tweets', url
            num_tweets = None

        try:
            num_followings = soup.find('li', 'ProfileNav-item ProfileNav-item--following').contents[1] \
                .attrs['title'].replace("Following", "").replace(",", "")
        except:
            print count, x, 'Number of followings', url
            num_followings = None

        try:
            num_followers = soup.find('li', 'ProfileNav-item ProfileNav-item--followers').contents[1] \
                .attrs['title'].replace("Followers", "").replace(",", "")
        except:
            print count, x,  'Number of follower', url
            num_followers = None

        try:
            num_likes = soup.find('li', 'ProfileNav-item ProfileNav-item--favorites').contents[1] \
                .attrs['title'].replace("Likes", "").replace(",", "")
        except:
            print count, x,  'Number of likes', url
            num_likes = None

        try:
            join_date = soup.find('div', 'ProfileHeaderCard-joinDate').text.encode('utf8').strip('\n').strip() \
                .replace("Joined", "")
        except:
            print count, x, 'Join date', url
            join_date = None

        try:
            bio = soup.find('p', 'ProfileHeaderCard-bio u-dir').text.encode('utf8')
        except:
            print count, x, 'Bio', url
            Bio = None

        try:
            num_pic = soup.find('a', 'PhotoRail-headingWithCount js-nav').text.encode('utf8').strip('\n').strip() \
                .replace("Photos", "").replace("videos", "").replace("and", "")
        except:
            print count, x, 'Number of pictures', url
            num_pic = None



        file_PI.write('%s\n' % num_pic)
        file_BI.write('%s\n' % bio)
        file_JD.write('%s\n' % join_date)
        file_NL.write('%s\n' % num_likes)
        file_NFR.write('%s\n' % num_followers)
        file_NFG.write('%s\n' % num_followings)
        file_NT.write('%s\n' % num_tweets)
        file_L.write('%s\n' % location)

        count += 1

    file_PI.close()
    file_BI.close()
    file_JD.close()
    file_NL.close()
    file_NFR.close()
    file_NFG.close()
    file_NT.close()
    file_L.close()
