import pandas as pd

df = pd.read_csv("top 40 gender.csv")
df["Date Charted"] = pd.to_datetime(df["Date Charted"]).dt.strftime("%Y-%m-%d")
df['year'] = pd.DatetimeIndex(df["Date Charted"]).year
df_clean = df[df['Gender'].notna()]
df_clean

#Making a loop so it prints out gender ratio every year
for year in range(1971,2012):
    test = (df["Date Charted"]> (str(year))) & (df["Date Charted"]<= (str(year+1)))
    decades = df.loc[test]
    decades["Gender"].value_counts(normalize=True)
    print(decades["Gender"].value_counts(normalize=True))    
    
#for decade 1971-81 
start_date = '1971-01-01'
end_date = '1981-01-01'
test = (df["Date Charted"]> start_date) & (df["Date Charted"]<= end_date)
decades = df.loc[test]
decades["Gender"].value_counts(normalize=True)

#for decade 1981-91 
start_date = '1981-01-01'
end_date = '1991-01-01'
test = (df["Date Charted"]> start_date) & (df["Date Charted"]<= end_date)
decades = df.loc[test]
decades["Gender"].value_counts(normalize=True)

#for decade 1991-2001 
start_date = '1991-01-01'
end_date = '2001-01-01'
test = (df["Date Charted"]> start_date) & (df["Date Charted"]<= end_date)
decades = df.loc[test]
decades["Gender"].value_counts(normalize=True)

#for decade 2001-2011
start_date = '2001-01-01'
end_date = '2011-01-01'
test = (df["Date Charted"]> start_date) & (df["Date Charted"]<= end_date)
decades = df.loc[test]
decades["Gender"].value_counts(normalize=True)

#Make the data visualization for every decade (total 4 decades)
#Making a bar chart for male-female percentage over 4 decades
import matplotlib.pyplot as plt

height = [0,1,2,3,4,5,6,7]
sizes = [0.656271, 0.343729, 0.728527, 0.271473, 0.732854, 0.267146, 0.721733, 0.278267]
labels = ["F 1971-81", "M 1971-81", "F 1981-91", "M 1981-91", "F 1991-01", "M 1991-01", "F 2001-11", "M 2001-11"]
plt.xticks(height, labels)
plt.xticks(rotation=45)
plt.bar(height, sizes, color=['red','blue','red','blue','red','blue','red','blue'])
plt.ylabel("Gender proportion")
plt.title("Top 40 charts artist gender ratio, decades 1971-2001")
plt.show()
