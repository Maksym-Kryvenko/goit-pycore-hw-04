import pathlib

def total_salary(path: str) -> tuple[int, int]:
    """
    Calculate total sum and average salary from a file.
    :param path: Path to the salary file.
    :return: A tuple containing total sum and average salary.
    """
    path = pathlib.Path(path)

    try:
        with path.open("r", encoding="utf-8") as fin:
            salaries = [float(line.split(",")[1].strip()) for line in fin.readlines() if len(line.split(",")) == 2]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0
    if not salaries:
        return 0, 0
    return sum(salaries), sum(salaries)/len(salaries)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total:.0f}, Середня заробітна плата: {average:.0f}")
