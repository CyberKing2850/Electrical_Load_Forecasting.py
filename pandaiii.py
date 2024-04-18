import pandas as pd
import json
from datetime import datetime

file_path =  r"C:\Users\manoj\OneDrive\Desktop\explodata.csvs.json" 

def load_and_process_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    columns = ['State', 'Value', 'Timestamp', 'Datetime', 'Formatted Date']
    df = pd.DataFrame(columns=columns)

    for record in data:
        timestamp = record['timestamp']
        datetime_obj = datetime.fromtimestamp(timestamp)
        formatted_date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')  
        lines = record['csv_str'].strip().split('\n')
        for line in lines:
            state, value = line.split(',')
            df = df._append({
                'State': state, 
                'Value': int(value), 
                'Timestamp': timestamp, 
                'Datetime': datetime_obj, 
                'Formatted Date': formatted_date
            }, ignore_index=True)

    return df

df = load_and_process_data(file_path)

print(df.head())

output_file_path = r"C:\Users\manoj\OneDrive\Desktop\export_data.csv.txt"
df.to_csv(output_file_path, index=False)

print(f"Data exported to '{output_file_path}' successfully.")
