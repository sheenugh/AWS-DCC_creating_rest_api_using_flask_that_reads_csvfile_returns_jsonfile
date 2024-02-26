from flask import Flask, jsonify
import csv

app = Flask(__name__)

csv_file = 'programming_languages.csv'

def read_csv():
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]
    return data

@app.route('/', methods=['GET'])
def get_langs():
    data = read_csv()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)