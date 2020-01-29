import email
import csv

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:route>')
def render_page(route='index.html'):
    return render_template(route)

def write_to_file(data):
    with open("database.txt", 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)

            return redirect('thankyou.html')
        except:
            return 'dit not save to database'
    else:
        return 'form not submitted oups!!'