import pandas as pd
import json
from datetime import datetime

# Set the correct file path (change the path as per your setup)
file_path =  r"C:\Users\manoj\OneDrive\Desktop\explodata.csvs.json" # Modify this path

# Function to load and process the JSON data
def load_and_process_data(file_path):
    # Load JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Create a DataFrame to hold the cleaned data
    columns = ['State', 'Value', 'Timestamp', 'Datetime', 'Formatted Date']
    df = pd.DataFrame(columns=columns)

    # Process each record
    for record in data:
        timestamp = record['timestamp']
        datetime_obj = datetime.fromtimestamp(timestamp)
        formatted_date = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')  # Human-readable format
        lines = record['csv_str'].strip().split('\n')
        for line in lines:
            state, value = line.split(',')
            # Append to DataFrame
            df = df._append({
                'State': state, 
                'Value': int(value), 
                'Timestamp': timestamp, 
                'Datetime': datetime_obj, 
                'Formatted Date': formatted_date
            }, ignore_index=True)

    return df

# Load the data
df = load_and_process_data(file_path)

# Display the DataFrame
print(df.head())

# Optionally, save the DataFrame to a CSV file
output_file_path = r"C:\Users\manoj\OneDrive\Desktop\export_data.csv.txt"
df.to_csv(output_file_path, index=False)

# Show that the file was successfully created and saved
print(f"Data exported to '{output_file_path}' successfully.")
