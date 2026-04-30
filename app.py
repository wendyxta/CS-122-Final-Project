from flask import *
from data import DataCollector
from visualization import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/day-hour")
def day_hour():
    return render_template("day_hour_page.html")

@app.route("/day-analysis", methods=["GET", "POST"])
def day_analysis():
    df = load_data()
    min_day, min_day_val, max_day, max_day_val = analyze_daily(df)

    return render_template("day_hour_page.html", min_day=min_day, min_day_val=min_day_val, max_day=max_day, max_day_val=max_day_val)

@app.route("/hour-analysis", methods=["GET", "POST"])
def hour_analysis():
    df = load_data()
    min_hr, min_hr_val, max_hr, max_hr_val = analyze_hourly(df)

    return render_template("day_hour_page.html", min_hr=min_hr, min_hr_val=min_hr_val, max_hr=max_hr, max_hr_val=max_hr_val)

@app.route("/selected-day", methods=["GET", "POST"]) # GET -> open page, POST -> submit selected date
def selected_day():
    df = load_data() # load data
    dates = sorted(df["date"].unique()) # get unique dates from CSV

    show_graph = False

    if request.method == "POST": # if user submits form do actions below
        selected = request.form["date"] # get form data
        if selected: # only run if user actually selects a date
            plot_flights_for_selected_day(df, selected) 
            show_graph = True
            
    return render_template("selected_day_page.html", dates=dates, show_graph=show_graph)
    
@app.route("/collect", methods=["POST"])
def generate_data():
    collector = DataCollector()
    collector.get_data()
    collector.create_csv()

    return redirect(url_for("flight_data"))

if __name__ == "__main__":
    app.run(debug=True)