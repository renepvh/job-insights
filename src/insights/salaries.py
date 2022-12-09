from typing import Dict, List, Union

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    return max(
        [
            int(job["max_salary"])
            for job in jobs
            if (job["max_salary"]).isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    jobs = read(path)
    return min(
        [
            int(job["min_salary"])
            for job in jobs
            if (job["min_salary"]).isdigit()
        ]
    )


def check_field(job: Dict, salary: Union[int, str]) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        return False
    if salary == str and not salary.isdigit():
        return False
    if int(job["min_salary"]) > int(job["max_salary"]):
        return False
    return True


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if not check_field(job, salary):
            raise ValueError
        return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])
    except TypeError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
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
    raise NotImplementedError
