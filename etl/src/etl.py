import pandas as pd
import os

def etl_pipeline(source, data_target_filename, metadata_target_filename):
    try:
        with open(source) as file_data:
            filename = os.path.split(source)
            print("Reading: " + filename[1])
            
            # Metadata
            # Seperate the metadata out into seperate files. Metadata files use tabs, : and ; to seperate, so the Python engine is used to figure it out
            metadata = file_data.readlines()[0:15]
            df_metadata = pd.read_csv(pd.io.common.StringIO('\n'.join(metadata)), sep=None, engine='python', names=['Key', 'Value'])
            
            df_metadata = transform_metadata(df_metadata)
            
            df_metadata.to_parquet(metadata_target_filename)
            
            # Data
            # Extract and load for the data
            df = pd.read_csv(source, skiprows=15, sep=';')
            
            df = transform_data(df)
            
            df.to_parquet(data_target_filename)
            
            print("Finished reading: " + filename[1])
    except pd.errors.ParserError as e:
        print(f"Error processing {source}: {e}")

def transform_metadata(df: pd.DataFrame) -> pd.DataFrame:
    # Remove : from key
    df['Key'] = df['Key'].str.replace(':', '')
    
    # Drop datum column
    df = df[df['Key'] != 'Datum']
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df.drop(columns= "Quality", inplace= True)
    return df