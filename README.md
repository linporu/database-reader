# Database Reader

This program provides functionality to read a CSV file, convert its encoding, store the data in a SQLite database, execute SQL commands, and export data back to a CSV file. It is designed to handle Chinese characters correctly.

## Features

1. Reads a CSV file and stores it in a SQLite database.
2. Converts encoding from ISO-8859-1 to UTF-8 to support Chinese characters.
3. Provides status updates during the reading and conversion processes.
4. Allows users to execute arbitrary SQLite commands and returns the results.
5. Exports specified data back to a CSV file.
6. Includes detailed comments for easy understanding and maintenance of the code.

## Requirements

- Python 3.x
- pandas
- sqlite3

## Installation

To set up the project and install the required dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install pandas
   ```

4. **Ensure you have SQLite installed** (it comes pre-installed with Python).

Now you are ready to run the program!

## Usage

1. Replace the `input_file` variable in the `main()` function with the path to your ISO-8859-1 encoded CSV file.
2. Run the script. It will convert the file to UTF-8, read it into the database, and execute a sample SQL command.
3. You can modify the SQL command in the `execute_sql_command` function to retrieve different data.
4. The output CSV file will be saved as `db_output.csv`.

## Example

To run the program, execute the following command in your terminal:

```
bash
python db-reader.py
```


## License

This project is licensed under the MIT License.
