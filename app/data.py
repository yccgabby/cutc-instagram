from instapy import InstaPy, smart_run
import traceback
import glob
import os
from datetime import date
import json


class Profile:
    
    def populate(self):

        profile_details = []
        with open('./data/profile.txt','r') as f:
            profile_details = f.readlines()
        try:
            session = InstaPy(username=str(profile_details[0]),password=str(profile_details[1]),headless_browser=True,want_check_browser=False)
            session.login()
            self.followers = session.grab_followers(username=str(profile_details[0]), amount="full")
            self.following = session.grab_following(username=str(profile_details[0]), amount="full")
            self.unfollowers = session.pick_unfollowers(username=str(profile_details[0]), compare_by="month", compare_track="first", live_match=True, store_locally=True, print_out=True)
            self.not_following_back = session.pick_nonfollowers(username=str(profile_details[0]), live_match=True, store_locally=True)
            self.fans = session.pick_fans(username=str(profile_details[0]), live_match=True, store_locally=True)
            session.end(threaded_session=True)
        except:
            print(traceback.format_exc())

    def __init__(self):
        self.followers = []
        self.following = []
        self.unfollowers = []
        self.not_following_back = []
        self.fans = []
        self.populate() 