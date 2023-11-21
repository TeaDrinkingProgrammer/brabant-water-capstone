# Manual preprocessing:
Remove the 2 extra columns on line 25316 (25-08-2018;01:46:15;5.22;180 (Verdacht), VF)

Module to convert CSV files to Parquet
1. Install Poetry
2. 
```sh
poetry install
```

3. 
```
poetry run python process_files.py /path/to/csv/folder /path/to/parquet/folder
```
