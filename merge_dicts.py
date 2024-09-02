#function named merge_dicts that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, their values should be summed up.

def merge_dicts(dict1, dict2):
    #create a new dictionary to store the merged result
    merged_dict = {}

    #iterate over the keys in both dictionaries
    for key in dict1.keys() | dict2.keys():
        #if the key is already in the merged dictionary, sum up the values
        if key in merged_dict:
            merged_dict[key] += dict1[key] + dict2[key]
        #if the key is not in the merged dictionary, add it with its value from either dictionary
        else:
            merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

    return merged_dict

#test the function with two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))