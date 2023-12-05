import os
import argparse
from concurrent.futures import ProcessPoolExecutor
import src.etl as etl

def spawn_etl_pipeline(csv_folder, parquet_folder, num_processes):
    csv_folder = os.path.abspath(csv_folder)
    parquet_folder = os.path.abspath(parquet_folder)
    
    if not os.path.exists(parquet_folder):
        os.makedirs(parquet_folder)
    
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        conversion_tasks = [
            executor.submit(
                etl.etl_pipeline,
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

    spawn_etl_pipeline(args.input_csv_folder, args.output_parquet_folder, args.num_processes)

if __name__ == "__main__":
    main()