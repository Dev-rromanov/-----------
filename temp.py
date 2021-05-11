def foo(temperature):
    if int(temperature) > 25:
        return 'Hot'
    elif int(temperature) > 15 and int(temperature) < 25:
        return 'Warm'
    elif int(temperature) < 15:
        return 'Cold'

print (foo(26))
        
