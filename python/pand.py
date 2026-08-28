import pandas as pd

"""
#0
data = [1,2,3,4]
s = pd.Series(data, index=['a','b','c','d'])
print(s) , print(s.values) , print(s.index)

calories = {'day1': 420, 'day2': 380, 'day3': 390}
myvar = pd.Series(calories)
print(myvar)  , print(myvar['day1']) , print(myvar['day2'] + myvar['day3'])


#1
dt = {"Name": ["A", "B", "C", "D" ,], 
      "Age": [20, 30, 40, 50]
      }
df = pd.DataFrame(dt)
print(df)
df["Job"] =["Dev", "Dev", "Dev", "Dev"]
new_row = {"Name": "E", "Age": 60, "Job": "Dev"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df)

#2
df = pd.read_csv("po.csv")
#print(df) ,print(df.to_string(index=False)),print(df["Name"].to_string(index=False)) , print(df["Type1"].to_string(index=False)),print(df[["Name", "Type1" ,"Height"]].to_string(index=True))
tall = df[df["Height"] > 2]
heavy = df[df["Weight"] > 100]
type = df[(df["Type1"] == "Grass") | (df["Type2"] == "Water")]
print(tall.to_string(index=False))
print(heavy.to_string(index=False))
print(type.to_string(index=False))

#3
df = pd.read_csv("po.csv")
#print(df.mean(axis=0, numeric_only=True)) , print(df.max(axis=0, numeric_only=True)),print(df.min(axis=0, numeric_only=True))
group = df.groupby("Type1")
print(group["Height"].mean()),print(group["Height"].sum()),print(group["Height"].max()),print(group["Height"].min()),print(group["Height"].count())

"""
#4
df = pd.read_csv("po.csv")
drop = df.drop("Height" , axis=1)
print(drop)

drop1 = df.dropna(subset=["Type2"])
complete = df.fillna({"Type2": "None"})
replace = df.replace({"Type1": {"Grass": "Planta"}})
print(drop1)
print(complete)
print(replace)