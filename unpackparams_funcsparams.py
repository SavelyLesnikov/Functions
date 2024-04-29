def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(7, 'Str', False)

values_list = [56, True, 'Values']
values_dict = {'a': 'Petrovich', 'b': 71, 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Svyatoslav', 35]
print_params(*values_list_2)
