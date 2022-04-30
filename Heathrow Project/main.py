
import pandas as pd
import matplotlib.pyplot as plt
# Change settings to be able to see all columns
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
df = pd.read_csv('Heathrow Statistics .csv')

# Turn the countries into columns and delete data which isn't needed
df.rename(columns=df.iloc[1], inplace=True)
df.drop([0, 1], axis=0, inplace=True)
df['Month'] = df['Month'].astype("datetime64")
df.set_index('Month', inplace=True)
print(df.head())

# Change the type of the total number from an object to a float
df.replace(',', '', regex=True, inplace=True)
c = df.select_dtypes(object).columns
df[c] = df[c].apply(pd.to_numeric, errors='coerce')

# Check if the types have been changed
print(df.dtypes)

# Extract data from 2017 to 2022
five_yrs = df["2017": "2022"]
print(five_yrs)

# Plot data from 2017-2022 to see the trend in the data
fig, ax = plt.subplots()
ax.plot(five_yrs['Total'], marker='o')
ax.set(xlabel="Date (YYYY-MM-DD)",
       ylabel="Total Passengers (per million)",
       title="Total number of passengers in heathrow in the last five years")
plt.show()
