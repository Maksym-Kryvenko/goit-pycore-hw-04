import pathlib

def get_cats_info(path: str) -> list[dict[str, str | int]]:
    """
    Fetch cats information from a file.
    :param path: Path to the cats info file.
    :return: A list of dictionaries containing cats' information.
    """
    path = pathlib.Path(path)
    try:
        with path.open("r", encoding="utf-8") as fin:
            cats = []
            for line in fin.readlines():
                if len(line.strip().split(",")) != 3:
                    raise ValueError("Invalid line format, expected 3 values separated by commas.")
                id, name, age = line.strip().split(",")
                cats.append({"id": id, "name": name, "age": int(age)})
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    return cats

cats_info = get_cats_info("cats_file.txt")
print(cats_info)