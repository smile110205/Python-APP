from sqlalchemy import create_engine, text

engine = create_engine(
    "mysql+pymysql://sql6701490:VYUa9VsTrc@sql6.freemysqlhosting.net/sql6701490?charset=utf8mb4"
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


# def load_job_from_db(id):
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
#     row = result.fetchone()

#     return row._asdict([0])


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
