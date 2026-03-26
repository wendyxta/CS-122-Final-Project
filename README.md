# CS-122-Final-Project

Project Title: Flight Analyzer

Authors: Taanyaa Haridass Prasad, Wendy Ta  

Project Description (5 Sentences):
We are planning to examine data from the OpenSky Network API (https://openskynetwork.github.io/opensky-api/python.html#). We will look at flight data from various airlines in various states and compare the volume of flights. We will also track departures and arrivals to see how often they are delayed. We will model this data using bar graphs to display different months and airports. This data will help use determine the most optimal time of year to travel by plane. 

Project Outline/Plan:

- Interface Plan: We plan to use Graphic User Interface (GUI) generated with Python’s Tkinter library. We plan on having some buttons and dropdowns to display different types of data visualizations as well as have some output screens to display the graphs and data.

- Data Collection and Storage Plan (written by Author #1):
  - Collection:
    - We plan to use methods from the API such as `get_arrivals_by_airport()` and `get_departures_by_airport()` to get the total flights per airport and calculate the number of delays that occur. We will also use `get_flights_from_interval()` to get the total flights during a daily/monthly time period, and `get_states()` to get more details about the geographic positioning of an aircraft
  - Storage Plan:
    - We will parse the JSON data from the API and store it in a CSV spreadsheet
    - We will then extract the data that we want to examine such as the specific airports and arrival times that we want to look at and use them to visualize them. 

- Data Analysis and Visualization Plan (written by Author #2):
  - Analysis:
    - We plan to use Python's libraries such as pandas, numpy, matplotlib, and seaborn to analyze the flight data. 
    - Using the graphs that we visualized, we plan to identify spikes on line graph trendlines or longer bars on a bar graph. This would indicate more flights occuring, and a less optimal time for traveling.
  - Visualization:
    - Bar charts to compare the number of flights across airports and months.
    - Line graphs to show trends in arrivals and departures.
    - Map visualizations to show real time positions of aircraft.
  

