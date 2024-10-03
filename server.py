import datetime as dt

from flask import Flask, render_template

from api import Api

app = Flask(__name__)

data_api = Api()


def dynamic_page(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result

    return wrapper


@app.route('/')
@app.route('/<name>')
@dynamic_page
def manager(name=None):
    if name is None:
        year = dt.datetime.now().year  # Changed to return just the year
        return render_template("index.html", year=year)
    else:
        gender_info = data_api.get_gender(name)
        age_info = data_api.get_age(name)

        # Check if gender_info or age_info is None and handle it
        if gender_info is None or age_info is None:
            return render_template("error.html", message="Error fetching data. Please try again.")

        return render_template("info.html", gender_info=gender_info, age_info=age_info)


if __name__ == "__main__":
    app.run(debug=True)
