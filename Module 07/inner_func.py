# in python function is a first class object
def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return '201 successful'
    return inner_fun

# print(double_decker())
# print(double_decker()())


def do_something(work):
    print('work started')
    # print(work)
    work()
    print('work ended')
    
# do_something(2)
# do_something('ami busy')

def coding():
    print('coding in python')
    # return 'coding in python'
    
# do_something(coding) # if direct call
# do_something(coding()) # if return

def sleeping():
    print('sleeping and dreaming in python')
    
do_something(sleeping)