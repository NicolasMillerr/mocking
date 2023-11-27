"""
docstring
"""
import os
import argparse
import yaml
from icecream import ic
from mocking.builder.generators import make_string

from builder.builder import Builder

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
        with open(filepath, "r") as file:
            config = yaml.safe_load(file)
    else:
        raise ValueError(f"filepath {filepath} not found")
    print(config)

    df_builder = Builder()
    df_builder.parse_config(config)
    df = df_builder.make_df()
    ic(df.head())


if __name__ == "__main__":
    main()
