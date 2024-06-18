# City Hospitals and Clinics

## Description
Main data stored in `data/med_institutions_rate.csv` where column Med-institution is about number of med institutions in this region, column Med-institution-rate is number of med intitutions for 10000 people defined by standarts of [WHO](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/3120)

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```shell
    $ git clone https://github.com/open-data-kazakhstan/city-hospitals-and-clinics.git
    ```

2. Create and activate a virtual environment:
    ```bash
    pip install venv
    python -m venv /path/to/localrepo
    cd /path/to/localrepo
    Scripts/activate  # For Windows users
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the project:
    ```bash
    python scripts/main.py
    ```

## Data

Medical institution data is sourced from [gender.stat.gov.kz](https://gender.stat.gov.kz/page/frontend/detail?id=68&slug=-55&cat_id=3&lang=ru):

- `archive/source.xls`: Raw data of medical institutions by region from 2000 to 2022.
- `data/med_institutions.csv`: Cleaned version containing data only for 2022 and translated to English.
- `archive/city_population.csv`: Data that was taken from repository [city-population](https://github.com/open-data-kazakhstan/city-population)

## Scripts

- `package.py`: Used to create or update the datapackage.json file containing metadata about the dataset.
- `transform.py`: Used to convert the source.xls file to a CSV format for easier processing.

## License

This dataset is licensed under the Open Data Commons [Public Domain and Dedication License][pddl].

[pddl]: https://www.opendatacommons.org/licenses/pddl/1-0/

