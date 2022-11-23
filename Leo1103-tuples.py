'''
The function skip_tuples will receive the tuples
    the function will return the tuples but skip each element

Main function
    tuples will be define as variable t
    print the function skip_tuples
'''

def skip_tuples(Tuples):
    '''
    Tuples: input tuples
    returns: skip tuples
    '''
    return Tuples[::2]

def main():
    t = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(t))

if __name__ == "__main__":
    main()