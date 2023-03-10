import csv
from functools import lru_cache
from typing import Dict, List


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as file:
            jobs = csv.DictReader(file)
            jobs_list = []
            for job in jobs:
                jobs_list.append(job)
    except FileNotFoundError:
        print("Arquivo não encontrado")
    else:
        return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    jobs_list_types = []
    for job in jobs:
        jobs_list_types.append(job["job_type"])
    return list(set(jobs_list_types))


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
