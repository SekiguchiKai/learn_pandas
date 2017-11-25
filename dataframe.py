# pandasをimport
import pandas as pd

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


