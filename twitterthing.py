import argparse
import configparser
import openpyxl
import pandas as pd
import sys
import tweepy
from logging import config
from os import path
from tabulate import tabulate
from time import time

class Config:
    def check_api_keys(self):
        """Checks if config file exists.
        """

        if not path.exists("api_keys.config"):
            print("Config file is missing. Initialize config file with:\n")
            print("twitterthing.py --configure\n")
            SystemExit()
        else:
            return True

    def read_api_keys(self):
        """Reads config file and returns section options.
        """

        if self.check_api_keys():
            api_keys = configparser.ConfigParser(interpolation=None) # interpolation=None for special characters in keys and token strings

            try:
                api_keys.read("api_keys.config")

                consumer_key = api_keys["default"]["consumer_key"]
                consumer_secret = api_keys["default"]["consumer_secret"]
                access_token = api_keys["default"]["access_token"]
                access_token_secret = api_keys["default"]["access_token_secret"]
                bearer_token = api_keys["default"]["bearer_token"]

                return consumer_key, consumer_secret, access_token, access_token_secret, bearer_token

            except configparser.NoOptionError as e:
                print("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
                print("\nRerun: twitterthing.py --configure\n")
            except configparser.ParsingError as e:
                print("1Error Type : {}, Error Message : {}".format(type(e).__name__, e))
                print("\nRerun: twitterthing.py --configure\n")
            except configparser.InterpolationMissingOptionError as e:
                print("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
                print("\nRerun: twitterthing.py --configure\n")
            except Exception as e:
                print("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
                print("\nSomething went wrong. Reinitializing config file.\n")
        else:
            return False
            SystemExit()

    def configure_api_keys(self):
        """Determines if the config file
        needs to be reinitialized or updated.
        """

        if not path.exists("api_keys.config"):
            self.init_configure()
        elif not self.read_api_keys():
            self.init_configure()
        else:
            self.update_keys()

    def init_configure(self):
        """Used to reinitialize config file.
        Asks user for API key information.
        """

        api_keys = configparser.ConfigParser(interpolation=None) # interpolation=None for special characters in keys and token strings

        # Ask user for API key information
        consumer_key = input(f"Twitter Consumer Key: ")
        consumer_secret = input(f"Twitter Consumer Secret: ")
        access_token = input(f"Twitter Access Token: ") 
        access_token_secret = input(f"Twitter Access Token Secret: ") 
        bearer_token = input(f"Twitter Bearer Token: ")

        # Set config file options
        api_keys["default"] = {}
        api_keys["default"]["consumer_key"] = consumer_key
        api_keys["default"]["consumer_secret"] = consumer_secret
        api_keys["default"]["access_token"] = access_token
        api_keys["default"]["access_token_secret"] = access_token_secret
        api_keys["default"]["bearer_token"] = bearer_token

        # Write input to config file
        with open("api_keys.config", 'w') as config_file:
            api_keys.write(config_file)

    def update_keys(self):
        """Asks user for API key information.
        Prints API keys if they currently exist.
        Accepts values if none are give.
        """

        api_keys = configparser.ConfigParser(interpolation=None) # interpolation=None for special characters in keys and token strings
        api_keys.read("api_keys.config")

        consumer_key = input(f"Twitter Consumer Key [{api_keys['default']['consumer_key']}]: ") or api_keys['default']['consumer_key']
        consumer_secret = input(f"Twitter Consumer Secret [{api_keys['default']['consumer_secret']}]: ") or api_keys['default']['consumer_secret']
        access_token = input(f"Twitter Access Token [{api_keys['default']['access_token']}]: ") or api_keys['default']['access_token']
        access_token_secret = input(f"Twitter Access Token Secret [{api_keys['default']['access_token_secret']}]: ") or api_keys['default']['access_token_secret']
        bearer_token = input(f"Twitter Bearer Token [{api_keys['default']['bearer_token']}]: ") or api_keys['default']['bearer_token']

        # Set config file options
        api_keys["default"] = {}
        api_keys["default"]["consumer_key"] = consumer_key
        api_keys["default"]["consumer_secret"] = consumer_secret
        api_keys["default"]["access_token"] = access_token
        api_keys["default"]["access_token_secret"] = access_token_secret
        api_keys["default"]["bearer_token"] = bearer_token

        # Write input to config file
        with open("api_keys.config", 'w') as config_file:
            api_keys.write(config_file)

def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.epilog = """Examples of use:
    python3 twitterthing.py lookup --id 783214
    python3 twitterthing.py search --username twitter
    python3 twitterthing.py search --username twitter --start 2022-07-20 --end 2022-07-22
    """
    subparsers = parser.add_subparsers(help='primary commands', dest="command")

    # Lookup parsers
    lookup = subparsers.add_parser("lookup", help="gather info on Twitter user", formatter_class=argparse.RawTextHelpFormatter)
    lookup.epilog = """Examples of use:
    python3 twitterthing.py search --id 783214
    python3 twitterthing.py search --username twitter
    """
    lookup_group = lookup.add_mutually_exclusive_group()
    lookup_group.add_argument("--id", type=int, help="gwitter ID (int)")
    lookup_group.add_argument("--username", "-u", type=str, help="gwitter username")

    # Search parsers
    search = subparsers.add_parser("search", help="search through Tweets", formatter_class=argparse.RawTextHelpFormatter)
    search.epilog = """Examples of use:
    python3 twitterthing.py search --id 783214
    python3 twitterthing.py search --username twitter --start 2022-07-20 --end 2022-07-22
    """
    search_group = search.add_mutually_exclusive_group()
    search_group.add_argument("--id", type=int, help="twitter ID (int)")
    search_group.add_argument("--username", "-u", type=str, help="twitter username")
    search.add_argument("--start", type=str, help="start date [YYYY-MM-DD]")
    search.add_argument("--end", type=str, help="end date [YYYY-MM-DD]")
    search.add_argument("--max", type=str, default=10, help="max results [default: 10]")
    search.add_argument("--output", "-o", type=str, help="output file [default: csv]")
    search.add_argument("--format", "-f", choices=["csv", "xlsx"], type=str, help="format of output file [csv | xlsx]")

    # Optional arguments
    parser.add_argument("--configure", action="store_true", help="configure API key config file")

    # Show help if no arguments are provided
    return parser.parse_args(None if sys.argv[1:] else ["--help"])

class Twitter:
    def get_user_info(self, id_or_username):
        # Check if ID is an integer or string
        if isinstance(id_or_username, int):
            id = client.get_user(id=id_or_username)

            # Create dataframe of results
            df = pd.DataFrame(data=[id.data])
            df.columns = ["ID", "Name", "Username"]

            # Make table look pretty in the terminal
            table = tabulate(df, headers="keys", tablefmt = "pretty", showindex=False)
        else:
            username = client.get_user(username=id_or_username)
            #username = client.get_user(username=args.username, user_fields="public_metrics")

            # Create dataframe of results
            df = pd.DataFrame(data=[username.data])
            df.columns = ["ID", "Name", "Username"]

            # Make table look pretty in the terminal
            table = tabulate(df, headers="keys", tablefmt = "pretty", showindex=False)

        return table

    def search_tweets(self, id, max, **kwargs):
        # Client.get_users_tweets() specifically needs the Twitter ID, not username
        # Convert to ID, if string detected
        if isinstance(id, str):
            self.id = client.get_user(username=id).data["id"]
        else:
            self.id = id

        # If start and end arguments are provided
        # Else, just get the default 10 Tweets
        if kwargs:
            tweets = client.get_users_tweets(
                id=self.id, tweet_fields=["created_at"],
                max_results=max,
                start_time=kwargs["start"] + "T00:00:00Z",
                end_time=kwargs["end"] + "T00:00:00Z")
        else:
            tweets = client.get_users_tweets(id=self.id, max_results=max, tweet_fields=["created_at"])
        
        # Create dataframe of results
        df = pd.DataFrame(data=[tweet for tweet in tweets.data])
        df.columns = ["Created", "Tweet ID", "Tweet"]
        df["Created"] = df["Created"].dt.tz_localize(None) # Normalize date and time zone

        return df
            
if __name__ == "__main__":
    # Used for execution times
    start_time = time()

    # Import arguments
    args = get_args()

    # Initialize Config
    config = Config()

    if args.configure:
        config.configure_api_keys()

    if config.read_api_keys():
        # Get API keys
        consumer_key, consumer_secret, access_token, access_token_secret, bearer_token = config.read_api_keys()

        # Initialize Tweepy Client
        client = tweepy.Client(bearer_token, wait_on_rate_limit=True)
    
        # Intialize Twitter class
        twitter = Twitter()

        if args.command == "lookup":
            if args.username is not None or args.id is not None:
                if args.username:
                    print(twitter.get_user_info(args.username))
                elif args.id:
                    print(twitter.get_user_info(args.id))
            else:
                print("lookup requires --id or --username")
        elif args.command == "search":
            if args.username is not None or args.id is not None:
                if args.username:
                    if args.start is not None and args.end is not None:
                        tweets = twitter.search_tweets(args.username, start=args.start, end=args.end, max=args.max)
                        tweet_table = tabulate(tweets, headers="keys", tablefmt = "pretty", showindex=False, stralign="left")

                        print(twitter.get_user_info(args.username))
                        print(tweet_table)
                        print(f"\nRetrieved {len(tweets)} most recent Tweets in ", end="")
                    else:
                        tweets = twitter.search_tweets(args.username, max=args.max)
                        tweet_table = tabulate(tweets, headers="keys", tablefmt = "pretty", showindex=False, stralign="left")

                        print(twitter.get_user_info(args.username))
                        print(tweet_table)
                        print(f"\nRetrieved {len(tweets)} most recent Tweets in ", end="")
                elif args.id:
                    if args.start is not None and args.end is not None:
                        tweets = twitter.search_tweets(args.id, start=args.start, end=args.end, max=args.max)
                        tweet_table = tabulate(tweets, headers="keys", tablefmt = "pretty", showindex=False, stralign="left")

                        print(twitter.get_user_info(args.id))
                        print(tweet_table)
                        print(f"\nRetrieved {len(tweets)} most recent Tweets in ", end="")
                    else:
                        tweets = twitter.search_tweets(args.id, max=args.max)
                        tweet_table = tabulate(tweets, headers="keys", tablefmt = "pretty", showindex=False, stralign="left")

                        print(twitter.get_user_info(args.id))
                        print(tweet_table)
                        print(f"\nRetrieved {len(tweets)} most recent Tweets in ", end="")
                if args.output and args.format == "csv":
                    tweets.to_csv(args.output, index=False)
                elif args.output and args.format == "xlsx":
                    tweets.to_excel(args.output, index=False)
                else:
                    tweets.to_csv(args.output, index=False)
            else:
                print("search requires --id or --username")

            # Print execution time
            print(f"{round(time() - start_time, 4)} seconds\n")
    else:
        SystemExit()