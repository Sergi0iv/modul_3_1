calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(a):
    count_calls()
    return len(a), a.upper(), a.lower()


def is_contains(a, e):
    count_calls()
    for i in e:
        if a.lower() == i.lower():
            return True
    return False


print(string_info('sergey'))
print(string_info('kozmodemyansk'))
print(is_contains('Sergey', ['Andrey', 'Sergey', 'Anna']))
print(is_contains('Nikolay', ['Sergey', 'Andrey', 'Anna']))
print(calls)
