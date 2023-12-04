import os
import argparse
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

def convert_csv_to_parquet(csv_file, data_file, metadata_file):
    try:
        with open(csv_file) as file_data:
            filename = os.path.split(csv_file)
            print("Reading: " + filename[1])
            
            # Seperate the metadata out into seperate files. Metadata files use tabs, : and ; to seperate, so the Python engine is used to figure it out
            metadata = file_data.readlines()[0:15]
            df_metadata = pd.read_csv(pd.io.common.StringIO('\n'.join(metadata)), sep=None, engine='python', names=['Key', 'Value'])
            df_metadata.to_parquet(metadata_file)
            
            df = pd.read_csv(csv_file, skiprows=15, sep=';')
            df.to_parquet(data_file)
            
            print("Finished reading: " + filename[1])
    except pd.errors.ParserError as e:
        print(f"Error processing {csv_file}: {e}")

def convert_csv_folder_to_parquet(csv_folder, parquet_folder, num_processes):
    csv_folder = os.path.abspath(csv_folder)
    parquet_folder = os.path.abspath(parquet_folder)
    
    if not os.path.exists(parquet_folder):
        os.makedirs(parquet_folder)
    
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        conversion_tasks = [
            executor.submit(
                convert_csv_to_parquet,
                os.path.join(csv_folder, csv_file),
                os.path.join(parquet_folder, os.path.splitext(csv_file)[0] + '.parquet'),
                os.path.join(parquet_folder, os.path.splitext(csv_file)[0] + '.metadata.parquet')
            )
            for csv_file in csv_files
        ]

        for future in conversion_tasks:
            future.result()

def main():
    parser = argparse.ArgumentParser(description='Convert CSV files to Parquet in parallel.')
    parser.add_argument('input_csv_folder', type=str, help='Path to the input CSV folder')
    parser.add_argument('output_parquet_folder', type=str, help='Path to the output Parquet folder')
    parser.add_argument('--num_processes', type=int, default=os.cpu_count(), 
                        help='Number of processes to use for parallel conversion (default: number of CPU cores)')

    args = parser.parse_args()

    convert_csv_folder_to_parquet(args.input_csv_folder, args.output_parquet_folder, args.num_processes)

if __name__ == "__main__":
    main()