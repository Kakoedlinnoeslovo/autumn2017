some_list = []
some_list.append('hello')
some_list.append(1)

some_dict = {'first': 'first_value'}
some_dict['hello'] = 'value'

some_set = {'elem'}
some_set = set('elem')


def some_function(param1, *args, **kwargs):
    if len(args) > 1:
        print('too much args')
    for arg in args:
        print(arg)
    print({arg + 'bar' for arg in args})

some_function('value1', 'foo1', 'bar', value3='bar2')
