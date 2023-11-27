"""
docstring
"""
import os
import argparse

parser = argparse.ArgumentParser(
    prog="mocking",
    description="CLI for the mocker tabular data mocking library",
)
parser.add_argument("filename")


def find_file(file_name):
    """
    Finds file_name in "definitions/:
    """
    # Get the current working directory
    current_directory = os.getcwd()
    subdirectory = "definitions"
    file_path = os.path.join(current_directory, subdirectory, file_name)
    if os.path.isfile(file_path):
        return file_path
    else:
        return None


def main():
    """Entrypoint"""
    args = parser.parse_args()
    filepath = find_file(args.filename)
    if filepath is not None:
        with open(filepath, "r", encoding="utf8") as text:
            names = [line.rstrip() for line in text]
    else:
        raise ValueError(f"filepath {filepath} not found")
    print(names)


if __name__ == "__main__":
    main()
