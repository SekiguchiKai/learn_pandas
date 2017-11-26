# pandasをimport
import pandas as pd

print("=====create DataFrame from dictionary=====")
# dictionaryを作成する
dictionary = {
    'Name': ["Python", "Go", "java"],
    'Type': ["Dynamic", "Static", "Static"]
}
print("=====dictionary=====")
print(dictionary)
# Transpose index and columns
# DataFrame.Tでdictionaryから
df = pd.DataFrame(dictionary).T
print("=====DataFrame=====")
print(df)

print("=====create DataFrame=====")
df2 = pd.DataFrame([["Python", "Go", "java"],
        ["Dynamic", "Static", "Static"],
        ]).T
print("=====DataFrame2=====")
print(df2)

df2.columns = ["Name", "Type"]
df2.index = ["0", "1", "2"]

print("=====DataFrame with columns and index=====")
print(df2)

print("=====replace columns and index of DataFrame. =====")
df2.columns = ["名前", "型"]
df2.index = ["A", "B", "C"]
print(df2)

print("=====rename columns and index of DataFrame. =====")
df3 = df2.rename(columns={'名前': 'Name', '型': 'Type'})
df3 = df3.rename(index={'A': '0', 'B': '1', 'C': '2'})
print(df3)