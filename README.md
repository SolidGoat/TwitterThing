# About TwitterThing
I'm not really sure what this is, hence the ambigious name. This is just a simple Python script to lookup Twitter handles and download Tweets. Maybe I'll add more features in the future.

I'm sure there are other more sophisticated scripts that do the same thing, but I wanted a simple project to practice Python. If you have recommendations on improvements, please let me know.

## Setup
1. Setup a Twitter Developer account

    *Instructions to come

2. Clone the repository
    ```console
    ~$ git clone https://github.com/SolidGoat/TwitterThing.git
    ```

3. Install dependencies
    * openpyxl
    * pandas
    * tabulate
    * tweepy

    (Optionally you can create a virtual environment first)
    ```console
    ~$ python -m venv ./venv
    ```
    ```console
    ~$ pip install -r requirements.txt
    ```

4. Create api_key.config file
    ```console
    ~$ python3 twitterthing.py --configure
    ```

## Usage
### Primary commands
Option | Description
-------|------------
search | Enters search mode
lookup | Enters lookup mode

### twitterthing.py search

Switch              | Description
--------------------|------------
--id                | Twitter ID, in numerical form
--username, -u      | Twitter username
--start             | The oldest or earliest timestamp from which the Tweets will be provided [YYYY-MM-DD]
--end               | The newest or most recent UTC timestamp from which the Tweets will be provided [YYYY-MM-DD]
--max               | Max Tweets to retrieve 1 - 100 [default: 10]<br>Max amount is currently 100 
--output, -o        | Name of output file [default: csv]
--format, -f        | Format of output file [csv \| xlsx]

### twitterthing.py lookup

Switch              | Description
--------------------|------------
--id                | Twitter ID, in numerical form
--username, -u      | Twitter username

### Optional commands
Switch              | Description
--------------------|------------
--configure         | Configure API key config file

### Examples
1. Configure API key file
    
    (these are fake keys)

    ```console
    ~$ python3 twitterthing.py lookup --configure

    Twitter Consumer Key: xvz1evFS4wEEPTGEFPHBog
    Twitter Consumer Secret: L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg
    Twitter Access Token: 622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl
    Twitter Access Token Secret: tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq
    Twitter Bearer Token: AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F
    ```

2. Look up user based on Twitter username
    ```console
    ~$ python3 twitterthing.py lookup --username twitter

    +--------+---------+----------+
    |   ID   |  Name   | Username |
    +--------+---------+----------+
    | 783214 | Twitter | Twitter  |
    +--------+---------+----------+
    0.1938 seconds
    ```

3. Look up user based on Twitter ID
    ```console
    ~$ python3 twitterthing.py lookup --id 783214

    +--------+---------+----------+
    |   ID   |  Name   | Username |
    +--------+---------+----------+
    | 783214 | Twitter | Twitter  |
    +--------+---------+----------+
    0.1938 seconds
    ```

4. Retrieve the 10 most recent Tweets
    ```console
    ~$ python3 twitterthing.py search --username twitter

    +--------+---------+----------+
    |   ID   |  Name   | Username |
    +--------+---------+----------+
    | 783214 | Twitter | Twitter  |
    +--------+---------+----------+
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Created             | Tweet ID            | Tweet                                                                                                                                        |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | 2022-06-30 17:52:17 | 1542566710594658312 | if you've ever stolen a Tweet say sorry                                                                                                      |
    | 2022-06-30 16:22:48 | 1542544188310437888 | RT @camerobradford: When two people who are dating both like one of my tweets, i like to picture them both laughing at it together while ho… |
    | 2022-06-23 20:37:17 | 1540071516527890433 | @Arkunir non, toujours pas                                                                                                                   |
    | 2022-06-23 19:48:13 | 1540059169771978754 | we would know                                                                                                                                |
    | 2022-06-23 19:46:10 | 1540058653155278849 | ratios build character                                                                                                                       |
    | 2022-06-21 21:14:00 | 1539355981854957568 | RT @pvrekhs: how do other people not constantly reply to their own tweets i always have extra info to add                                    |
    | 2022-05-18 16:08:50 | 1526957996747722753 | RT @TwitterSpaces: Twitter Spaces are real live audio convos you can join from your couch. or the dog park. or the bathtub. wherever you ar… |
    | 2022-04-01 17:50:07 | 1509951255388504066 | we are working on an edit button                                                                                                             |
    | 2022-03-30 17:10:59 | 1509216629695168512 | @McDonalds we ordered those 5 months ago… we want snack wraps now                                                                            |
    | 2022-03-30 16:42:16 | 1509209405937627143 | @lwtsphh he's defrosting for the single drop                                                                                                 |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

    Retrieved 10 most recent Tweets in 0.6986 seconds
    ```

5. Retrieve the 10 most recent Tweets and output to Excel
    ```console
    ~$ python3 twitterthing.py search --username twitter --output output.xlsx -f xlsx

    +--------+---------+----------+
    |   ID   |  Name   | Username |
    +--------+---------+----------+
    | 783214 | Twitter | Twitter  |
    +--------+---------+----------+
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Created             | Tweet ID            | Tweet                                                                                                                                        |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | 2022-06-30 17:52:17 | 1542566710594658312 | if you've ever stolen a Tweet say sorry                                                                                                      |
    | 2022-06-30 16:22:48 | 1542544188310437888 | RT @camerobradford: When two people who are dating both like one of my tweets, i like to picture them both laughing at it together while ho… |
    | 2022-06-23 20:37:17 | 1540071516527890433 | @Arkunir non, toujours pas                                                                                                                   |
    | 2022-06-23 19:48:13 | 1540059169771978754 | we would know                                                                                                                                |
    | 2022-06-23 19:46:10 | 1540058653155278849 | ratios build character                                                                                                                       |
    | 2022-06-21 21:14:00 | 1539355981854957568 | RT @pvrekhs: how do other people not constantly reply to their own tweets i always have extra info to add                                    |
    | 2022-05-18 16:08:50 | 1526957996747722753 | RT @TwitterSpaces: Twitter Spaces are real live audio convos you can join from your couch. or the dog park. or the bathtub. wherever you ar… |
    | 2022-04-01 17:50:07 | 1509951255388504066 | we are working on an edit button                                                                                                             |
    | 2022-03-30 17:10:59 | 1509216629695168512 | @McDonalds we ordered those 5 months ago… we want snack wraps now                                                                            |
    | 2022-03-30 16:42:16 | 1509209405937627143 | @lwtsphh he's defrosting for the single drop                                                                                                 |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

    Retrieved 10 most recent Tweets in 1.0073 seconds
    ```

6. Retrieve the 10 most recent Tweets between **2022-01-01** and **2022-07-22**
    ```console
    ~$ python3 twitterthing.py search --username twitter --start 2022-01-01 --end 2022-07-22

    +--------+---------+----------+
    |   ID   |  Name   | Username |
    +--------+---------+----------+
    | 783214 | Twitter | Twitter  |
    +--------+---------+----------+
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | Created             | Tweet ID            | Tweet                                                                                                                                        |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
    | 2022-06-30 17:52:17 | 1542566710594658312 | if you've ever stolen a Tweet say sorry                                                                                                      |
    | 2022-06-30 16:22:48 | 1542544188310437888 | RT @camerobradford: When two people who are dating both like one of my tweets, i like to picture them both laughing at it together while ho… |
    | 2022-06-23 20:37:17 | 1540071516527890433 | @Arkunir non, toujours pas                                                                                                                   |
    | 2022-06-23 19:48:13 | 1540059169771978754 | we would know                                                                                                                                |
    | 2022-06-23 19:46:10 | 1540058653155278849 | ratios build character                                                                                                                       |
    | 2022-06-21 21:14:00 | 1539355981854957568 | RT @pvrekhs: how do other people not constantly reply to their own tweets i always have extra info to add                                    |
    | 2022-05-18 16:08:50 | 1526957996747722753 | RT @TwitterSpaces: Twitter Spaces are real live audio convos you can join from your couch. or the dog park. or the bathtub. wherever you ar… |
    | 2022-04-01 17:50:07 | 1509951255388504066 | we are working on an edit button                                                                                                             |
    | 2022-03-30 17:10:59 | 1509216629695168512 | @McDonalds we ordered those 5 months ago… we want snack wraps now                                                                            |
    | 2022-03-30 16:42:16 | 1509209405937627143 | @lwtsphh he's defrosting for the single drop                                                                                                 |
    +---------------------+---------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

    Retrieved 10 most recent Tweets in 0.5063 seconds
    ```

## Planned Features
* [ ] Dump all Tweets
* [ ] Retrieve more than 100 Tweets
* [ ] No output
* [ ] Allow for different API config profiles
* [ ] Search by time
* [ ] Analyze results (maybe?)
