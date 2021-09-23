"""
This template is written by @timgrossmann

What does this quickstart script aim to do?
- This script is automatically executed every 6h on my server via cron
"""

import random
import getpass
from instapy import InstaPy
from instapy import smart_run

def get_tags_from_text_file(fname):
    data = open(fname).read()
    tags = [x.lower() for x in data.split()]
    return tags

# dont_likes = ['sex', 'nude', 'naked', 'pussy', 'hunt', 'gun', 'shoot']
# friends = ['list of friends I do not want to interact with']
# like_tag_list = ['vegan', 'veganfoodshare', 'veganfood', 'whatveganseat',
#                  'veganfoodie', 'veganism', 'govegan',
#                  'veganism', 'vegansofig', 'veganfoodshare', 'veganfit',
#                  'veggies']
# prevent posts that contain some plantbased meat from being skipped
# ignore_list = ['vegan', 'veggie', 'plantbased']
# accounts = ['accounts with similar content']
dont_likes = get_tags_from_text_file('dont_like_tags.txt')
friends = get_tags_from_text_file('skip_friend_usernames.txt')
like_tag_list = get_tags_from_text_file('like_tags.txt')
ignore_list = get_tags_from_text_file('always_like_tags.txt')
accounts = get_tags_from_text_file('similar_account_usernames.txt')
username = open('username.txt').read().strip()
password = open('password.txt').read().strip()
headless_browser = open('show_browser.txt').read().strip().lower() != 'yes'

insta_username = username or input('Enter your instagram username: ')
insta_password = password or getpass.getpass()


# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=headless_browser)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)

    session.unfollow_users(amount=random.randint(75, 150),
                           instapy_followed_enabled=True,
                           instapy_followed_param="all", style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)

    # """ Joining Engagement Pods...
    # """
    # photo_comments = ['Nice shot! @{}',
    #     'I love your profile! @{}',
    #     'Wonderful :thumbsup:',
    #     'Just incredible :open_mouth:',
    #     'What camera did you use @{}?',
    #     'Love your posts @{}',
    #     'Looks awesome @{}',
    #     'Getting inspired by you @{}',
    #     ':raised_hands: Yes!',
    #     'I can feel your passion @{} :muscle:']

    # session.set_do_comment(enabled = True, percentage = 95)
    # session.set_comments(photo_comments, media = 'Photo')
    # session.join_pods(topic='travel')
