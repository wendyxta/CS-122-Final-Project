from opensky_api import OpenSkyApi, TokenManager
import time

class DataCollector:
    def __init__(self):
        try: # use credentials if they exist
            tm = TokenManager.from_json_file("credentials.json")
            self.api = OpenSkyApi(token_manager=tm)
        except:
            self.api = OpenSkyApi()

        self.hourly_flights = {} # store number of flights for each hour

        self.cur_time = int(time.time()) # get current time RIGHT NOW in seconds
        self.start_time = self.cur_time - (3600 * 24 * 7) # go back 7 days from now in seconds
        self.step = 1 * 3600 # size of each chunk of data (1 hour in seconds)
    
    def get_data(self):
        pass
