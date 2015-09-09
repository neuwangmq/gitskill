# err.py assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is ddd zero!'
    return 10 / n

def main():
    return foo('0')
print main()