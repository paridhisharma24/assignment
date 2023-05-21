from flask import Flask, request
from connect import create_app, db
from utils.gen_report import generate_report
from utils.get_report import get_report

app = Flask(__name__)

app = create_app()
db.create_all(app=create_app())


@app.route('/trigger_report')
def trigger_report():
    report_id = generate_report()
    return report_id


@app.route('/get_report')
def report():
    report_id = request.args.get('report_id')
    new_report = get_report(report_id)
    # print(new_report)
    return new_report


if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)

   