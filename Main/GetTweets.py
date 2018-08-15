from twitterscraper import query_tweets

import os
from datetime import timedelta, date, datetime
import datetime as dt


def main():
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    date1 = date(2018, 2, 9)
    date2 = date(2018, 2, 10)
    start_date = '2018-02-08'
    for single_date in daterange(date1, date2):
        end_date = single_date.strftime("%Y-%m-%d")
        tsd = start_date.split('-')
        ted = end_date.split('-')
        print start_date, end_date,

        list_of_tweets = query_tweets("MeToo", limit=None,
                                      begindate=dt.date(int(tsd[0]), int(tsd[1]), int(tsd[2])),
                                      enddate=dt.date(int(ted[0]), int(ted[1]), int(ted[2])), poolsize=20, lang='')


        print len(list_of_tweets)


        folder = './Tweets/' + start_date + '/'
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_NA = open(folder + 'Name.txt', 'w')
        file_ID = open(folder + 'ID.txt', 'w')
        file_US = open(folder + 'User.txt', 'w')
        file_RE = open(folder + 'Retweets.txt', 'w')
        file_TE = open(folder + 'Text.txt', 'w')
        file_LI = open(folder + 'Likes.txt', 'w')
        file_RP = open(folder + 'Replies.txt', 'w')
        file_DA = open(folder + 'date.txt', 'w')
        for i in range(0, len(list_of_tweets)):
            file_NA.write('%s\n' % list_of_tweets[i].fullname.encode("utf-8"))
            file_ID.write('%s\n' % list_of_tweets[i].id)
            file_US.write('%s\n' % list_of_tweets[i].user.encode("utf-8"))
            file_RE.write('%s\n' % list_of_tweets[i].retweets)
            file_TE.write('%s\n' % list_of_tweets[i].text.encode("utf-8"))
            file_LI.write('%s\n' % list_of_tweets[i].likes)
            file_RP.write('%s\n' % list_of_tweets[i].replies)
            file_DA.write('%s\n' % list_of_tweets[i].timestamp)

        file_NA.close()
        file_ID.close()
        file_US.close()
        file_RE.close()
        file_TE.close()
        file_LI.close()
        file_RP.close()
        file_DA.close()

        start_date = end_date


if __name__ == '__main__':
    main()
