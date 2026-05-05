from opensky_api import OpenSkyApi, TokenManager
from datetime import datetime, timezone
import time, csv

class DataCollector:
    def __init__(self):
        try: # use credentials if they exist
            tm = TokenManager.from_json_file("credentials (2).json")
            self.api = OpenSkyApi(token_manager=tm)
        except:
            self.api = OpenSkyApi()

        self.hourly_flights = {} # store number of flights for each hour

        self.cur_time = int(time.time()) # get current time RIGHT NOW in seconds
        self.start_time = self.cur_time - (3600 * 24 * 7) # go back 7 days from now in seconds
        self.step = 1 * 3600 # size of each chunk of data (1 hour in seconds)

    def get_data(self):
        print("fetching data from api...")
        start = datetime.now()

        t = self.start_time # start pointer at beginning (7 days ago)

        while t < self.cur_time: # keep looping until we reach "now"
            next_t = min(t + self.step, self.cur_time) # move forward step hrs but do not go past the current time
            data = self.api.get_departures_by_airport("KSFO", t, next_t)
            # time.sleep(2) # go to sleep in between api calls to avoid the rate call per-minute limit

            time_label = datetime.fromtimestamp(t, tz=timezone.utc).strftime("%m-%d-%Y %H:%M")
            if data: # check if data was actually returned
                self.hourly_flights[time_label] = len(data)
            else: # otherwise number of flights = 0
                self.hourly_flights[time_label] = 0
                # print("No data returned for", time_label)
                # return

            t = next_t # move forward 

        print("time:", datetime.now() - start)
        print("data fetching complete!")

    def create_csv(self):
        print("writing data to csv file...")

        with open("SFO_flights.csv", "w", newline="") as f: # write data to SFO_flights.csv
            writer = csv.writer(f)

            header = ["timestamp", "flight counts"] # write the header
            writer.writerow(header)

            for hour, flights in self.hourly_flights.items(): # write each timestamp:number of flights entry
                writer.writerow([hour, flights])
                print(hour, flights)

        print("csv file created!")