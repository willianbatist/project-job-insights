from src.jobs import read


def get_unique_job_types(path):
    jobss = read(path)
    jobs_title = []
    valores = []
    obj = {}
    for row in jobss:
        if row['job_type'] != '':
            jobs_title.append(row['job_type'])

    for dado in jobs_title:
        if dado not in valores:
            obj[dado] = jobs_title.count(dado)
    return obj


def filter_by_job_type(jobs, job_type):
    jobs_title = []

    for row in jobs:
        if row['job_type'] == job_type:
            jobs_title.append(row)

    return jobs_title


def get_unique_industries(path):
    jobss = read(path)
    industries = []
    valores = []
    obj = {}
    for row in jobss:
        if row['industry'] != '':
            industries.append(row['industry'])

    for dado in industries:
        if dado not in valores:
            obj[dado] = industries.count(dado)
    return obj


def filter_by_industry(jobs, industry):
    filter = []

    for row in jobs:
        if row['industry'] == industry:
            filter.append(row)

    return filter


def get_max_salary(path):
    jobss = read(path)
    salaries = []
    for row in jobss:
        if row['max_salary'] != '' and row['max_salary'].isnumeric():
            salaries.append(int(row['max_salary']))

    max_salary = max(salaries)
    return max_salary


def get_min_salary(path):
    jobss = read(path)
    salaries = []
    for row in jobss:
        if row['min_salary'] != '' and row['min_salary'].isnumeric():
            salaries.append(int(row['min_salary']))

    min_salary = min(salaries)
    return min_salary


def matches_salary_range(job, salary):
    try:
        max = job["max_salary"]
        min = job["min_salary"]
    except KeyError:
        raise ValueError()
    if (type(max) != int or type(salary) != int or max < min):
        raise ValueError()
    if int(min) <= int(salary) and int(salary) <= int(max):
        return True
    return False


def filter_by_salary_range(jobs, salary):
    filter_jobs = []
    for row in jobs:
        max = row["max_salary"]
        min = row["min_salary"]
        if (type(max) == int and type(salary) == int and max > min):
            if min <= salary <= max:
                filter_jobs.append(row)
    return filter_jobs
