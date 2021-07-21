
# Load the data 

import pandas as pd 

data = pd.read_csv("20210103_hundenamen.csv")

# 0. Convert all the hundname to lower case
HundName_list = HundName_list = [data['HUNDENAME'][i].lower() for i in range(len(data))] 


# 1. Select all the names form the hundname list  that have same len as 'Luca' or 'len(luca) +1 or len(luca)-1

def name_luca_len(list_names, name_target):
    """
    elect all the names form the hundname list  that have same len( name_target) or len( name_target) +1 or len( name_target)-1
    list_names is a list of hund's names
    name_target is the target name of the dog  a string
    """
    same_len = [list_names[i] for i in range(len(list_names)) if len(list_names[i]) == len(name_target)]
    len_plus1 = [list_names[i] for i in range(len(list_names)) if len(list_names[i]) == len(name_target) + 1 ]
    len_minus1 = [list_names[i] for i in range(len(list_names)) if len(list_names[i]) == len(name_target) -1]
    
    All_list = same_len + len_plus1 + len_minus1
    # 2. Remove duplicates name from the list
    unique_names = list(set(All_list))
    
    return unique_names


# 3. Select all the names that have at least 3 identical letters found in the target name
def identical_letters(name_target, check_names):
    """ Keep only the names that have at least (len(name) - 1) identical letters in them 
    
    name_target  is the target named
    check_names is the list of name we want to chek
    """

    collect1 = list()
    for n1 in n:
        count = 0
        for c1, c2 in zip(n1,name_target):  # check with letter correct position 
            if c1 == c2:
                count = count + 1 
    #     print(count)

        if count == len(name_target) - 1:
    #         print('keep those names')
            collect1.append(n1)
    return collect1
  
  
# 4. Select all  names from the initial list that have name_target in them 
# (from which we can delete some letters to have our targeted name). 


def deletion_part(list_names, name_target):
    """
    Select all  names from the initial list that have 'name_target' in them
    
    list_names is the initial list of names
    name_target is the targeted name of hund
    """
    deletion = []
    for i in list_names:
        f = name_target in i
        if f ==True:
            deletion.append(i)
    return deletion
        
      
        
# put all together and see

name_target = 'luca'  # This canbe changed to any name

unique = name_luca_len(HundName_list, name_target)

identic = identical_letters(name_target, unique)

deletion = deletion_part(HundName_list, name_target)


List_final = deletion + identic

# Remove again duplicates name from the list
List_final = list(set(List_final))
print(List_final, len(List_final))

# Finally, we have a list of hund name that 1 Levenshtein distance away from 'Luca'. 
