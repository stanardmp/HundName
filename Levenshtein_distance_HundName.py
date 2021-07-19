
"""
# Task

In this dataset of dog names in Zurich, find all names that have a Levenshtein distance of 1 to "Luca". 

 
 The operations can be 
 
 *  Deletion
 *  Insertion
 *  Replacement (substitution)
 
 
- Break down the problem:
0.  Convert all the hundname to lower case 

1. The words need to have same len as 'Luca'

2. The hundname muss all have the same len and 'Luca'. If they do not have same len, the need to contain a sequence of letter in the correct order "luca" somweher ein their text(string)  (#example '"Bo" Bendy of Luca')

5. Remove from the list of names all possible duplicate names from the list  hundname_list_new = list(set(hundname_list))

6.  Deal with possible alternative for the middles letters of our new list of hundnames.

7. Finally, we have a list of hund name that 1 Levenshtein distance away from 'Luca'. 

"""


import pandas as pd 

# load data 
data = pd.read_csv("20210103_hundenamen.csv")
# data.head()
# data.shape

# 0. Convert all the hundname to lower case
HundName_list = HundName_list = [data['HUNDENAME'][i].lower() for i in range(len(data))]

# 1. Select all the names form the hundname list  that have same len as 'Luca'.

h = [HundName_list[i] for i in range(len(HundName_list)) if len(HundName_list[i]) == len("luca")]


# 2. Remove duplicates name from the list

unique_names = list(set(h))


# 3.  name from which we can delete some letters to have 'luca'. (names that have 'luca' in them)

deletion = []
for i in HundName_list:
    f = 'luca' in i
    if f ==True:
        deletion.append(i)

        
# 4. Keep name that have 'luc' or 'uca' in them. 

def uca_luc(Liste):
    extreme = []
    middle = [] 
    
    for i in Liste:
        #extreme 
        if i[-3:] =='uca' or i[:-1] =='luc':
            extreme.append(i)
        #middle
        if (i[0]=='l' and i[2] == 'c' and i[-1] == 'a') or (i[0]=='l' and i[1] =='u' and i[-1] == 'a'): 
            middle.append(i)
            
    return extreme, middle

a, b = uca_luc(unique_names)
HundName_luca_Final = a + b  + deletion

# print(HundName_luca_Final)


# Remove identical name from the list.
l_name = list(set(HundName_luca_Final))
l_name
