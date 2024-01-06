import who_package_101 as who

def cancer(func):
    try:
        print(func.atest())
    except:
        print('404')

def cancer(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            return '404'
    return wrapper

@cancer
def ihateyou(x,y):
    return x+y
    

def main():
    
    who.say_hello()
    x = who.LastStoneWaight()
    y = who.isWarmer()
    print(x.Solution([4, 4, 5, 6, 3]))
    print(y.Solution([4, 4, 5, 6, 3]))
    print(who.test)
    print(y.help())
    #Now for something crazy
    print(who.isWarmer.help(y))
    cancer(y)
    
    print(ihateyou(1,2))
    

if __name__== '__main__':
    main()
