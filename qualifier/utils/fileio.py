# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans):
    """
    Save qualifying loans as a csv to the directory where the
    app is running.

    Parameters
    ----------
    qualifying_loans : 'dict'
        A dictionary of qualifying loans.
    """
    # File name for the qualifying loans CSV.
    output_path = Path("qualifying_loans.csv")

    # Save the qualifying loans in the current working directory.
    with open(output_path, 'w', newline='') as csvfile:
        # Create the csv writer object.
        csvwriter = csv.writer(csvfile)

        # Write the qualifying loans to the CSV file.
        for loan in qualifying_loans:
            csvwriter.writerow(loan.values())
