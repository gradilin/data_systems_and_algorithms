scanner = {'1000': 'zHbldVSS3k',
           '1001': 'dP6sL081TX',
           '1002': 'wOTKMzApuk',
           '1003': 'hsiJO1PTHy',
           '1004': 'FEqdrhCPX9',
           '1005': 'tF0Wronc6q',
           '1006': 'ikxnCpjjqQ',
           '1007': 'oTTspoSI9v',
           '1008': 'bm6cRuHBrg',
           '1009': 'wIfTF7PkXj',
           '1010': 'GsGv3BTr3P',
           '1012': '2rIE2TWkqh',
           '1013': 'ov7khhUE4R',
           '1014': 'W89Buby4Vs',
           '1015': 'M9N5Z3ieI5',
           '1016': 'TYAa96agec',
           '1017': '1XP76sUhQn',
           '1018': '6XI24yMPQs'
          }

configstring = "" 
for x in scanner.keys(): 
    configstring += x + scanner[x] + '|'

configstring = configstring[0:(len(configstring) - 1)]

config_list = configstring.split("|")
count = len(config_list) 
lowest_val = 10000
confighash = {}

for x in config_list: 
    key = int(x[0:4]) 
    if key < lowest_val: 
        lowest_val = key 
    if x not in confighash.keys(): 
        confighash[key] = x[4:]

config_list = [] 
print(confighash.keys())
upper = (lowest_val + len(confighash))
for x in range(lowest_val, upper):
    print(x) 
    if x not in confighash.keys(): 
        print("incorrect config") 
        break 
    config_list.append(confighash[x])

print(config_list)
     


def filter_even_numbers(numbers):
    # Filter even numbers from the input list
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    return list(even_numbers)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_even_numbers(numbers))  # Output: [2, 4, 6, 8]

# def square_numbers(numbers):
#     # Square each number in the input list
#     squared_numbers = map(lambda x: x ** 2, numbers)
#     return list(squared_numbers)

# # Example usage
# numbers = [1, 2, 3, 4, 5]
# print(square_numbers(numbers))  # Output: [1, 4, 9, 16, 25]

# def sort_tuples_by_second_element(tuples):
#     # Sort the list of tuples by the second element of each tuple
#     sorted_tuples = sorted(tuples, key=lambda x: x[1])
#     return sorted_tuples

# # Example usage
# tuples = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]
# # Output: [(2, 'apple'), (1, 'banana'), (3, 'cherry')]
# print(sort_tuples_by_second_element(tuples))


# def sort_dictionary_by_value(hash):
#     # Sort the dictionary by value (quantity)
#     sorted_list = sorted(hash.items(), key=lambda item: item[1])
#     # Convert the sorted list of tuples back into a dictionary
#     sorted_dict = dict(sorted_list)

#     return sorted_dict

# def sort_dictionary_by_key(hash): 
#     sorted_list  = sorted(hash.items(), key=lambda x: x[0])
#     sorted_dict = dict(sorted_list)
#     return sorted_dict 

# # Sample dictionary
# fruit_quantities = {
#     'apples': 50,
#     'bananas': 20,
#     'oranges': 35,
#     'pears': 10,
#     'grapes': 45
# }

# print(sort_dictionary_by_value(fruit_quantities))





#  '1019': 'GpzoxDlCNc',
#            '1020': '45cjFKYQWU',
#            '1021': 'KdeXgL3dXj',
#            '1022': 'vBHiI24oQs',
#            '1023': 'uYhyJcwGEu',
#            '1024': 'yWVn24T2zd',
#            '1025': '16gYn8LeSg',
#            '1026': 'lINdPb6VXT',
#            '1027': '8e9d6t9LEY',
#            '1028': 's89OW9h2At',
#            '1029': 'sUfoWhw5Ff',
#            '1030': 'ytbOUGVWsv',
#            '1031': 'kxztw7VE1V',
#            '1032': 'NOzV3bWVFQ',
#            '1033': 'A8dTrbSVJo',
#            '1034': 'C7YbKMdIQI',
#            '1035': 'ChhyJ9wYTg',
#            '1036': 'r0hIdi8cdS',
#            '1037': '073KkP2PuN',
#            '1038': 'zQIJrqv6Me',
#            '1039': 'SC2TiXg72H',
#            '1040': 'gzCMFudgc9',
#            '1041': 'obJBVHm6Te',
#            '1042': 'ajFYlZCyBr',
#            '1043': 'mu12EGNue3',
#            '1044': 'NqFd7mnJXh',
#            '1045': 'sHVKgUvKnx',
#            '1046': '04Ez9H3j6s',
#            '1047': 'RwgNdm4kVe',
#            '1048': '24apWgWnuP',
#            '1049': 'uIghxHQx85',
#            '1050': 'fNApdTcLXm',
#            '1051': '9ZF3AyxY1y',
#            '1052': '4cEsbRXIJ0',
#            '1053': '2vuIP2tfCu',
#            '1054': 'JydqmhD1cI',
#            '1055': 'rdRvwdn2ZV',
#            '1056': 'vCIucwUKxI',
#            '1057': 'O1ISKvXojT',
#            '1058': 'qi8TAa9lhq',
#            '1059': 'KSA7hkuYA4',
#            '1060': '0jiEUW6Pyk',
#            '1061': 'Er6cyI8842',
#            '1062': 'nBAMKseOhW',
#            '1063': '5tynBlc2zu',
#            '1064': '5SRH0T7wSC',
#            '1065': 'cE3FFpYGDc',
#            '1066': 'T6pFwkvB9G'

