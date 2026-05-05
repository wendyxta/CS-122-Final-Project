import pandas as pd
import matplotlib
matplotlib.use("Agg") # prevents matplotlib from opening GUI window and instead just saves graph to a file
import matplotlib.pyplot as plt

def load_data():
    try:
        df = pd.read_csv("static/SFO_flights.csv")
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
    df["date"] = pd.to_datetime(df["date"])
    daily = df.groupby("date")["flight counts"].sum()

    plt.figure(figsize=(10, 10))

    # plot the data as a bar chart
    daily.plot(kind="bar")

    axes_labels = []
    for day in daily.index:
        label = f"{day.strftime('%A')} \n {day.strftime('%m/%d/%y')}" # format to include weekday name and date 
        axes_labels.append(label)

    plt.title("Total Flights Per Day")
    plt.xlabel("Day of Week")
    plt.ylabel("Number of Flights")
    plt.xticks(range(len(axes_labels)), axes_labels, rotation=30)

    # label number of flights above each bar
    for i, value in enumerate(daily.values): # loop through each bar (i = pos, value = flight count)
        plt.text(
            i, # x pos
            value, # y pos
            str(value), # y value
            ha = "center", # center text over bar
            va = "bottom" # place text just above bar
        )

    # save the figure as an image in the static folder for Flask
    plt.savefig("static/day_plot.png")

    # close the figure to free memory
    plt.close()

def plot_flights_per_hour(df):
    # group data by hour and add up all flight counts for that hour
    hourly = df.groupby("hour")["flight counts"].sum()

    # ensure hours are ordered for plotting
    hourly = hourly.sort_index()

    plt.figure(figsize=(12, 8))

    hourly.plot(kind="bar")

    axes_labels = []
    for hour in hourly.index:
        label = f"{hour:02}:00" # format hour into a timestamp (H:00)
        axes_labels.append(label)

    plt.title("Total Flights by Hour")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Flights")
    plt.xticks(range(len(axes_labels)), axes_labels, rotation=45)

    # label number of flights above each bar
    for i, value in enumerate(hourly.values):
        plt.text(
            i,
            value,
            str(value),
            ha = "center",
            va = "bottom"
        )

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

    plt.figure(figsize=(8, 8))

    plt.plot(hourly.index, hourly.values, marker="o")

    plt.title(f"Flights by Hour on {selected_date}")
    plt.xlabel("Hour of Day")
    plt.ylabel("Number of Flights")

    # make x axis show all hours from 0 - 23
    plt.xticks(range(24))
    
    plt.grid(linestyle='--', linewidth=0.5, alpha=0.4)

    # label number of flights above each bar
    for x, y in zip(hourly.index, hourly.values): # loop through pairs (x = hour, y = flight count)
        plt.annotate(
            str(y),
            xy = (x, y), # point on graph
            xytext = (-10, 5), # place text label -10 left, +5 units up from (x, y)
            textcoords = "offset points",
            ha = "center"
        )

    # save the figure as an image in the static folder for Flask
    plt.savefig("static/selected_day_plot.png")

    # close the figure to free memory
    plt.close()

def analyze_daily(df):
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()
    daily = df.groupby("weekday")["flight counts"].sum()

    min_day = daily.idxmin()
    min_val = daily.min()
    max_day = daily.idxmax()
    max_val = daily.max()

    return min_day, min_val, max_day, max_val

def analyze_hourly(df):
    hourly = df.groupby("hour")["flight counts"].sum()

    min_hr = hourly.idxmin()
    min_val = hourly.min()
    max_hr = hourly.idxmax()
    max_val = hourly.max()
    
    return min_hr, min_val, max_hr, max_val

def analyze_selected_day(df, selected_date):
    # convert selected date (string input) into proper date object
    selected_date = pd.to_datetime(selected_date).date()

    # filter dataset to only include rows from selected date
    day_data = df[df["date"] == selected_date]

    if day_data.empty:
        return None

    # group filtered data by hour and add up all flight counts for that hour
    hourly = day_data.groupby("hour")["flight counts"].sum()

    return {
        "best_hour": hourly.idxmin(),
        "worst_hour": hourly.idxmax(),
        "total_flights": hourly.sum()
    }