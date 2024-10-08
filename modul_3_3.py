def print_params(a, b, c):
    print(a, b, c)


values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(**values_dict)
values_list = [11, 2, 1987]
print_params(values_list)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
print_params(a=1, b='строка', c=True)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
