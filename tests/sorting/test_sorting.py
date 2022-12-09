from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs_list = [
        {
            "title": "Maquinista",
            "max_salary": "2000",
            "min_salary": "1800",
            "date_posted": "2021-11-29",
        },
        {
            "title": "Motorista",
            "max_salary": "1900",
            "min_salary": "1500",
            "date_posted": "2021-12-29",
        },
        {
            "title": "Ux Designer",
            "max_salary": "2500",
            "min_salary": "1800",
            "date_posted": "2021-10-29",
        },
        {
            "title": "Gerente Comercial",
            "max_salary": "3500",
            "min_salary": "2950",
            "date_posted": "2021-09-29",
        },
    ]
    sort_by(jobs_list, "max_salary")
    assert jobs_list == [
        {
            "title": "Gerente Comercial",
            "max_salary": "3500",
            "min_salary": "2950",
            "date_posted": "2021-09-29",
        },
        {
            "title": "Ux Designer",
            "max_salary": "2500",
            "min_salary": "1800",
            "date_posted": "2021-10-29",
        },
        {
            "title": "Maquinista",
            "max_salary": "2000",
            "min_salary": "1800",
            "date_posted": "2021-11-29",
        },
        {
            "title": "Motorista",
            "max_salary": "1900",
            "min_salary": "1500",
            "date_posted": "2021-12-29",
        },
    ]
