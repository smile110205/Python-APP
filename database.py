from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://sql6704924:Ygi1Siee32@sql6.freemysqlhosting.net/sql6704924?charset=utf8mb4"
)

# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs"))
#     result_all = result.all()
#     first_result = result_all[0]
#     column_names = result.keys()
#     first_result_dict = dict(zip(column_names, first_result))
#     print(first_result_dict)

# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
#   column_names = result.keys()

#   result_dicts = []

#   for row in result.all():
#     result_dicts.append(dict(zip(column_names, row)))
#   print(result_dicts)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()

    jobs = []

    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = []
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return row


# def add_application_to_db(job_id, data):
#     row = {
#         "job_id": job_id,
#         "full_name": data["full_name"],
#         "email": data["email"],
#         "linked_url": data["linked_url"],
#         "education": data["education"],
#         "work_experience": data["work_experience"],
#         "resume_url": data["resume_url"],
#     }
#     with engine.connect() as conn:
#         sql = text(
#             "INSERT INTO application(id,job_id,fullname,email,linkedin,education,experience,resumeurl) VALUES (:job_id,:fullname,:email,:linkedin,:education,:experience,:resumeurl)"
#         )
#         conn.execute(sql, row)
#         conn.commit()


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    # query = text(f"INSERT INTO applications (job_id, full_name, email, linked_url, education, work_experience, resume_url) VALUES(:{job_id},:{'full_name'},:{'email'},:{'linked_url'},:{'education'},:{'work_experience'},:{'resume_url'})")
    query = text(
        f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin_url']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')"
    )
    # query = text("INSERT INTO applications (job_id, full_name, email, linked_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linked_url, :education, :work_experience, :resume_url)")

    # conn.execute(query,job_id={'job_id'}, full_name=['full_name'], email=data['email'],linked_url=data['linked_url'], education= data['education'], work_experience = data['work_experience'], resume_url = data['resume_url'])

    conn.execute(query)
    conn.commit()
