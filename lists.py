#зaдания из Lists
number_list = [3, 5, 7, 9, 10.5]
print(number_list)
number_list.append('Python')
print(len(number_list))
print(number_list[0])
print(number_list[-1])
print(number_list[1:4])
number_list.remove('Python')

#задания из Dict
some_dict = {"city": "Москва", "temperature": "20"}
print(some_dict['city'])
some_dict['temperature'] = str(int(some_dict['temperature'])-5)
print(some_dict)
print(some_dict.get('country'))
print(some_dict.get('country', 'Russia'))
some_dict['date'] = '27.05.2019'
print(len(some_dict))