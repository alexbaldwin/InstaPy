from instapy import InstaPy

import schedule
import time

insta_username = 'exposure'
insta_password = os.environ['EXPOSURE_PASSWORD']

def job():
    try:
        # if you want to run this script on a server,
        # simply add nogui=True to the InstaPy() constructor
        session = InstaPy(username=insta_username, password=insta_password, nogui=True)
        session.login()

        # set up all the settings
        session.set_upper_follower_count(limit = 5000)
        session.set_lower_follower_count(limit = 50)
        session.set_dont_include(['alexbaldwin', 'lukesbeard', 'exposure'])
        session.set_do_follow(enabled=True, percentage=90, times=1)

        session.unfollow_users(amount=200, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=60 )

        # do the actual liking
        session.like_by_tags(
                [
                    'toldwithexposure'
                ], amount=50)

        session.follow_user_followers(
                [
                    'vsco',
                    'adobespark',
                    'sonyalpha',
                    'unsplash',
                    'squarespace',
                    'natgeotravel',
                    'earthpix',
                    'lonelyplanet',
                    'bbc_travel',
                    'lightroom',
                    'canonusa'
                ], amount=20, random=False)

        # end the bot session
        session.end()
    except:
            import traceback
            print(traceback.format_exc())

schedule.every().day.at("10:08").do(job)
schedule.every().day.at("14:08").do(job)
schedule.every().day.at("18:08").do(job)
schedule.every().day.at("22:08").do(job)
schedule.every().day.at("02:08").do(job)
schedule.every().day.at("06:08").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
