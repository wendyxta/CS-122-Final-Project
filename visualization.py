import pandas as pd
import matplotlib
matplotlib.use("Agg") # prevents matplotlib from opening GUI window and instead just saves graph to a file
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("SFO_flights.csv")
        print("Using latest API data")
    except FileNotFoundError:
        df = pd.read_csv("backup_flights.csv")
        print("Using backup data")
    
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour

    return df

def plot_flights_per_day(df):
    # group data by date and add up all flight counts for that day
    daily = df.groupby("date")["flight counts"].sum()

    plt.figure(figsize=(10, 4))

    # plot the data as a bar chart
    daily.plot(kind="bar")

    plt.title("Flights Per Day")
    plt.xlabel("Date")
    plt.ylabel("Number of Flights")

    # save the figure as an image in the static folder for Flask
    plt.savefig("static/day_plot.png")

    # close the figure to free memory
    plt.close()

def plot_flights_per_hour(df):
    # group data by hour and add up all flight counts for that hour
    hourly = df.groupby("hour")["flight counts"].sum()

    # ensure hours are ordered for plotting
    hourly = hourly.sort_index()

    plt.figure(figsize=(10, 4))

    hourly.plot(kind="bar")

    plt.title("Total Flights by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Flights")

    # save the figure as an image in the static folder for Flask
    plt.savefig("static/hour_plot.png")

    # close the figure to free memory
    plt.close()

def plot_flights_for_selected_day(df, selected_date):  
    # convert selected date (string input) into proper date object
    selected_date = pd.to_datetime(selected_date).date()

    # filter dataset to only include rows from selected date
    day_data = df[df["date"] == selected_date]

    if day_data.empty:
        print("No data for selected date!")
        return

    # group filtered data by hour and add up all flight counts for that hour
    hourly = day_data.groupby("hour")["flight counts"].sum()

    plt.figure(figsize=(10, 4))

    plt.plot(hourly.index, hourly.values, marker="o")

    plt.title(f"Flights by Hour on {selected_date}")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Flights")

    # make x axis show all hours from 0 - 23
    plt.xticks(range(24))
    
    plt.grid(linestyle='--', linewidth=0.5, alpha=0.4)

    # save the figure as an image in the static folder for Flask
    plt.savefig("static/selected_day_plot.png")

    # close the figure to free memory
    plt.close()
 