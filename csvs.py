import pandas as pd
from io import StringIO
import json
from datetime import datetime
import time


with open(r"C:\Users\manoj\OneDrive\Desktop\explodata.csvs.json") as f:
    data = json.load(f)
    
df = pd.DataFrame(columns=['state','load_value'])

for entry in data:
    csv_data = pd.read_csv(StringIO(entry["csv_str"]),header = None,names=['state','load_value'])
    timestamp = entry.get("timestamp")
    csv_data['timestamp'] = timestamp
    
    df = df._append(csv_data, ignore_index=True)

# if 'timestamp' in df.columns:
#     df['timestamp'] = df['timestamp'].dt.strftime('%d %H:%M')
    
df = df.sort_values(by=['timestamp','state'])

state_data = {}
for state in df['state'].unique():
    state_data[state] = df[df['state'] == state][['load_value','timestamp']]
    
    
output_file = "csvfile.csv"
df.to_csv(output_file,index =False)

print('success!!')

