from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "title": "APTEXDIX Consult",
        "header_title": "APTEXDIX Consult",
        "header_subtitle": "Innovative Ideas For You",
        "logo_url": url_for('static', filename='logo.jpg'),
        "hero_title": "Welcome to APTEXDIX Consult",
        "hero_description": (
            "We provide top-notch services in data analysis, research, consulting, and more, helping individuals and organizations achieve their goals."
        ),
        "services": [
            {"icon": "fas fa-flask", "title": "Research and Development", "description": "Comprehensive support for research projects."},
            {"icon": "fas fa-database", "title": "Data Collection", "description": "Expert guidance on data collection methods."},
            {"icon": "fas fa-chart-line", "title": "Data Analysis", "description": "Advanced analytical techniques to uncover insights."},
            {"icon": "fas fa-file-alt", "title": "Report Writing", "description": "Professionally written and formatted reports."},
            {"icon": "fas fa-calculator", "title": "Statistical Modelling", "description": "Development of models for complex problems."},
            {"icon": "fas fa-chart-pie", "title": "Business Analytics", "description": "Turning raw data into actionable insights."},
        ],
        "director_image_url": url_for('static', filename='pics me.jpg'),
        "director_name": "Taiwo Ayeni",
        "director_title": "Director, APTEXDIX Consult",
        "director_qualifications": (
            "MPS Analytics (Statistical Modelling), Northeastern University, Toronto, Canada.<br>"
            "B.Sc., M.Sc., Statistics, Ekiti State University, Nigeria."
        ),
        "phone_1": "+2348167610344",
        "phone_2": "+16472422347",
        "email": "aptexdixconsult@gmail.com",
        "social_links": {
            "linkedin": "https://www.linkedin.com/in/taiwo-ayeni-a0b020171",
        },
        "year": 2024,
        "footer_text": "APTEXDIX Consult. All Rights Reserved.",
    }
    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(debug=True)