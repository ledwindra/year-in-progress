from datetime import date
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def year_in_progress():

    year = date.today().year
    total_day = (date.today() - date(year, 1, 1)).days + 1
    leap_year = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    if leap_year:
        progress = f'{total_day} / 366'
    else:
        progress = f'{total_day} / 365'

    return render_template(
        "index.html", 
        progress=progress, 
        year=year,
        leap_year=leap_year
    )
