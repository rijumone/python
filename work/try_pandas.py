import pandas as pd
import itertools
"""
reader = pd.read_csv("conversion_rules_stats_advertiser_id_1563953_from_2017-06-02_to_2017-12-05_1512488361.csv", sep=',', iterator=True, chunksize=10)

sql = ""
for row in reader:
    for line in row:
        print(line)
    print("******************")
"""

df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6]})

print(df)

df = df.pivot(index='foo', columns='bar', values='baz')

print(df)

reader = pd.read_csv("/home/jump450/Zemanta/data/completed/conversion_goals_account_id_1058_from_2017-11-10_to_2017-12-11_1512978090.csv", sep=',')



print(reader.head())
# for row in reader:
#     # print()
#     row_data_list_lst = row.values.tolist()
#     for line in row_data_list_lst:
#         print(line)
#     print("******************")