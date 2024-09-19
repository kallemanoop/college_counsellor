import pandas as pd
import matplotlib.pyplot as plt
import sys

print(
    "Welcome to Collge Counsellor. A program which shortlists some of the best colleges for the filter/conditions that the user gives. Such as College Type, Fees, State and Rating. You will have to enter the input in correct syntax.\n")
df = pd.read_csv('main.csv')
dr = df.drop(['Campus Size', 'Total Enrollments', 'Total Faculty', 'Genders Accepted', 'City'], axis=1)
pd.set_option('display.max_columns', 10)
# print(dr)
stateList = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana',
             'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur',
             'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
             'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Delhi', 'Jammu and Kashmir']
print("Budget: ")
budget = input()
newList = []

# can be rewriten with switch case loops
for i in range(len(stateList)):
    x = stateList[i].lower()
    newList.append(x)
print("College Type: 'private' or 'public/government': ")
college_Type = input().lower()
if college_Type == 'private' or college_Type == 'public/government':
    pass
else:
    print("Invalid Input")
    sys.exit()
print("Your choice of State: ")
state = input().lower()
if state in newList:
    pass
else:
    print("Invalid input")
    sys.exit()
print("Rating: ")
rating = float(input())
if rating < 4:
    pass
else:
    print("The Rating limit is 4")
    sys.exit()

dr.dropna(inplace=True)
for i in dr['College Type']:
    dr2 = dr.replace('Public/Government', 'public')
statesList = dr["State"].tolist()
if state in statesList:
    pass
else:
    print(" ")
# print(dr)

for i in dr.index:
    if dr.loc[i, "College Type"].lower() != college_Type:
        dr.drop(i, inplace=True)

for i in dr.index:
    if dr.loc[i, "Average Fees"] > budget:
        dr.drop(i, inplace=True)
# print(dr)
for i in dr.index:
    if dr.loc[i, "State"].lower() != state:
        dr.drop(i, inplace=True)

for i in dr.index:
    if dr.loc[i, "Rating"] < str(rating):
        dr.drop(i, inplace=True)
dr.set_index('College Name')
# print(dr)
dr2 = dr.sort_values(['Rating'], ascending=False)
dr2.sort_values(['Average Fees'], ascending=False)
dr2['Rating'] = list(map(float, dr2['Rating']))
dr2['Average Fees'] = list(map(float, dr2['Average Fees']))
# print(dr2)
avg = dr2['Rating'].mean()
avgFees = dr2['Average Fees'].mean()
dr2 = dr2[dr2['Rating'] > avg]
dr2 = dr2[dr2['Average Fees'] < avgFees]
dr2.sort_values(['Average Fees'], ascending=False)
avg = dr2['Rating'].mean()
avgFees = dr2['Average Fees'].mean()

#  for i in dr2.index:
#    if dr2.loc[i,"Rating"]<avg and dr2.loc[i,'Average Fees']<avgFees:
#     dr2.drop(i,inplace=True)

print(avg, avgFees)
if dr2.empty:
    print("No colleges found for your desired filters.")
else:
    pass
print(dr2)
x = dr2['College Name'].tolist()
y = dr2['Average Fees'].tolist()
# plt.plot(x,y,'*--r')
plt.barh(x, y, color='c')
plt.xlabel("Fees")
plt.ylabel("Colleges")
plt.show()












