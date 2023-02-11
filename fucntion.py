def get_summ(one, two, delimiter='&'):
    return f'{str(one)}{delimiter}{str(two)}'

result = get_summ('Learn', 'python')
print(result.upper())