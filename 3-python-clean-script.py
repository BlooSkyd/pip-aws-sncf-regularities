import pandas as pd
import os

# Loading dataset
file_path = 'Regularities_by_liaisons_Trains_France.csv'
df = pd.read_csv(file_path)

# Removing unnecessary coloumns
cols_to_drop = [
    'Average delay of late departing trains (min)',
    'Average delay of all departing trains (min)',
    'Comment (optional) delays at departure',
    'Average delay of late arriving trains (min)',
    'Average delay of all arriving trains (min)',
    'Comment (optional) delays on arrival',
    '% trains late due to external causes (weather, obstacles, suspicious packages, malevolence, social movements, etc.)',
    '% trains late due to railway infrastructure (maintenance, works)',
    '% trains late due to traffic management (rail line traffic, network interactions)',
    '% trains late due to rolling stock',
    '% trains late due to station management and reuse of material',
    '% trains late due to passenger traffic (affluence, PSH management, connections)',
    'Average train delay > 15min'
]
df_clean = df.drop(columns=cols_to_drop, errors='ignore')

# Renaming columns to facilitate use
new_columns = {
    'Year': 'year',
    'Month': 'month',
    'Departure station': 'departure_station',
    'Arrival station': 'arrival_station',
    'Average travel time (min)': 'avg_travel_time_min',
    'Number of expected circulations': 'nb_expected',
    'Number of cancelled trains': 'nb_cancelled',
    'Number of late trains at departure': 'nb_late_dep',
    'Number of trains late on arrival': 'nb_late_arr',
    'Number of late trains > 15min': 'nb_late_over_15',
    'Number of late trains > 30min': 'nb_late_over_30',
    'Number of late trains > 60min': 'nb_late_over_60',
    'Period': 'period',
    'Delay due to external causes': 'delay_cause_external',
    'Delay due to railway infrastructure': 'delay_cause_infra',
    'Delay due to traffic management': 'delay_cause_traffic',
    'Delay due to rolling stock': 'delay_cause_rolling_stock',
    'Delay due to station management and reuse of material': 'delay_cause_station',
    'Delay due to travellers taken into account': 'delay_cause_travelers'
}

df_clean = df_clean.rename(columns=new_columns)

# Remplacing empty values (NaN) by 0
df_clean = df_clean.fillna(0)

# Substracting canceled trains to expected trains and removing canceled trains column
df_clean['nb_expected'] = df_clean['nb_expected'] - df_clean['nb_cancelled']
df_clean = df_clean.drop(columns=['nb_cancelled'])

# Creating new nb_late_before_15 column
df_clean['nb_late_before_15'] = df_clean['nb_late_arr'] - df_clean['nb_late_over_15']

# Rounding values to 4 digits
df_clean = df_clean.round(4)

# Saving cleaned file
output_filename = 'trains_france_clean.csv'
df_clean.to_csv(output_filename, index=False)

# Some math to flex
org_size = os.path.getsize(file_path)
cleaned_size = os.path.getsize(output_filename)
pct_gain = round((1-cleaned_size/org_size)*100,2)

print(f"Cleaned files saved as: {output_filename}")
print(f"Original size: {org_size} bytes")
print(f"Cleaned file size: {cleaned_size} bytes")
print(f"Gain: {pct_gain}% lighter")