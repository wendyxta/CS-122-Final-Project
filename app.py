from flask import *
from data import DataCollector
from visualization import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/graphs")
def graphs():
    return render_template("graphs_page.html")

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