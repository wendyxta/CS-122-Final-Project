from flask import *
from data import DataCollector

app = Flask(__name__)

@app.route("/", methods=["GET"])

def flight_data():
    return render_template("home_page.html")

@app.route("/collect", methods=["POST"])
def generate_data():
    collector = DataCollector()
    collector.get_data()
    collector.create_csv()

    return redirect(url_for("flight_data"))

if __name__ == "__main__":
    app.run(debug=True)