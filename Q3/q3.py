import pandas as pd
df = pd.read_csv('data.csv',parse_dates=[0],infer_datetime_format=True,date_parser = pd.to_datetime,keep_date_col = True,index_col=0)
"""
    Question 1 answer
"""
bd_df = df.loc[df['country_id'] == 'BDV']
arr = bd_df.site_id.unique()
max_c = ('',0)
for site in arr:
    site_df = bd_df.loc[bd_df['site_id']==site]
    c = site_df.user_id.unique()
    count = len(c)
    if count > max_c[1]:
        max_c = (site,count)
# Question 1 output
print(max_c)
"""
QUESTION 2  ANSWER

"""
# print(pd.to_datetime('2019-02-03 00:00:00'))
filtered = df.loc['2019-02-03 00:00:00':'2019-02-04 23:59:59']
# print(filtered)
arr = filtered.user_id.unique()
ans = []
for user in arr:
    user_df = filtered.loc[filtered['user_id']==user]
    site_count = user_df['site_id'].value_counts().to_dict()
    for site in site_count:
        # print(site['site_id'])
        if site_count[site] > 10:
            ans.append((user,site,site_count[site]))
            break
# Question 2 output
print(ans)
"""
QUESTION 3 & 4 ANSWER
"""
arr = df.user_id.unique()
first = 0
second = 0
third = 0
site_freq = {}
ans4 = 0
custom = pd.DataFrame(columns = df.columns)
for user in arr:
    user_df = df.loc[df.user_id==user]
    row = user_df.tail(1)
    first = user_df.head(1)
    if(row['site_id'].iloc[0]==first['site_id'].iloc[0]):
        ans4 += 1
    custom = pd.concat([custom,row])
# print(custom)
sites = custom.site_id.value_counts().keys().tolist()
site_counts = custom.site_id.value_counts().tolist()
ans = []
for i in range(0,3):
    ans.append((sites[i],site_counts[i]))
# Question 3 Answer
print(ans)
# Question 4 Answer
print(ans4)
