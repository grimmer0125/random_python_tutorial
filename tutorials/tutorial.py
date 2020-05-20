#%%
x = 3
print(f'x is {x}')


def sum(n):
    # try to change x
    x = 10

    # quick math: (1+n)*n/2
    sum = 0
    for i in range(1, n + 1):
        print(i)
        sum = sum + i
    print(f'sum is {sum}')
    return sum


y = sum(10)
print(f'x is {x}')
