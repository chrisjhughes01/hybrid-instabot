# hybrid_instabot
Growth tool for manual Instagram interactions

### How to use:
1. In Chrome browser, use the "toggle device toolbar" and select an iPhone.
2. Go to Instagram.com
3. Find a post that you want to interact with the users who liked it.
4. Click on the likes, and scroll down as far as you'd like. The further you scroll down, the more usernames get added to the HTML.
5. Now copy the entire HTML of the page by "inspecting" the page, right click on the top <html> tag, select "edit as HTML", and copy all of the text.
6. Run get_usernames.py and copy the HTML into the terminal when prompted and press enter.
7. Now, run open_new_usernames.py

### How it works:
* get_usernames.py collects all usernames from the HTML and writes unprocessed username to new_usernames.csv

* open_usernames.py will open usernames from new_usernames.csv one at a time. After a username is opened, it is removed from new_usernames.csv and written to processed_usernames.csv
