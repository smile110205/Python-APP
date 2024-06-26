from flask import Flask, render_template, jsonify, request

from database import load_jobs_from_db, load_job_from_db, add_application_to_db

# from sqlalchemy import text

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found", 404
  return render_template('jobpage.html', job=job)
  # return jsonify(job)


@app.route("/api/job/<id>")
def show_job_jsob(id):
  job = load_job_from_db(id)
  return jsonify(job)


@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
  data = request.form
  #  return jsonify(data)
  job = load_job_from_db(id)
  add_application_to_db(id, data)

  return render_template('application_submitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(port=5000, debug=True)
