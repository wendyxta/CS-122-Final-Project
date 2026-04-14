from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def flight_data():
    return render_template("home_page.html")

if __name__== "__main__":
    app.run(debug=True)