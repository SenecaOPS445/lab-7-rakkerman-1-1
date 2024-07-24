def function1():
    global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:',schoolName)

def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:',schoolName)

def function3():
    global schoolName
    print('print() in function3 on schoolName:',schoolName)

def lab7i():
    global schoolName
    schoolName = 'Seneca'
    print('print() in main on schoolName:',schoolName)
    function1()
    function3()
    function2()

if __name__ == '__main__':
    lab7i()
