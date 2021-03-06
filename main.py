import argparse

from packages.acquire import getting_data
from packages.wrangle import cleaning_data
from packages.analize import enriching_data
from packages.report import plotting_data

file_name = "CristopherRL.db"

def main():

    raw_data = getting_data(file_name)
    proc_data = cleaning_data(raw_data)
    table,top = enriching_data(proc_data)
    plotting_data(table,top)

if __name__ == "__main__":
    main()
