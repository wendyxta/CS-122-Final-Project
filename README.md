# CS-122-Final-Project

Project Title: Flight Analyzer

Authors: Taanyaa Haridass Prasad, Wendy Ta  

Project Description (5 Sentences):
We are planning to examine data from the OpenSky Network API (https://openskynetwork.github.io/opensky-api/python.html#). We will look at flight data from various airlines in various states and compare the volume of flights. We will also track departures and arrivals to see how often they are delayed. We will model this data using bar graphs to display different months and airports. This data will help use determine the most optimal time of year to travel by airplane. 

Project Outline/Plan:

- Interface Plan: We plan to use Graphic User Interface (GUI) generated with Python’s Tkinter library. We plan on having some buttons and dropdowns to display different types of data visualizations as well as have some output screens to display the graphs and data.

- Data Collection and Storage Plan (written by Author #1): We plan to use methods from the API usch as `get_arrivals_by_airport()`, `get_departures_by_airport()`, `get_flights_from_interval()`, and `get_states()`. We will then parse the JSON data from the API and store it in a csv spreadsheet. We will then extract the data that we want to examine such as the specific airports and arrival times that we want to look at and use them to visualize them. 

- Data Analysis and Visualization Plan (written by Author #2):
  - Analysis: We plan to use Python's libraries such as pandas and numpy to analyze the flight data. Using `get_arrivals_by_ariport()`, we will calculate total flights per airport. Additionally, `get_departures_by_airport()`, `get_flights_from_interval()`, will help us determine the number of departures and arrivals per day / month as well as any delays in flights that occur.
  - Visualization: We plan on using libraries such as matplotlib and seaborn for visualizing the data.
    - Bar charts to compare the number of flights across airports and months.
    - Line graphs to show trends in arrivals and departures.
    - Map visualizations to show real time positions of aircraft.
