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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
