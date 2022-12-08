from typing import Dict, List

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    jobs_list_types = []
    for job in jobs:
        if job["industry"] != "":
            jobs_list_types.append(job["industry"])
    return list(set(jobs_list_types))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
