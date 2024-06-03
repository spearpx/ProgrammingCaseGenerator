

def snake(n):
    """This is a function to convert a string to snake case string"""
    snakestr = n
    for i in snakestr:
        if i==' ' or i=='-':
            snakestr = snakestr.replace(i,'_')            
    return snakestr     

def pascal(n):
    """This is a function used to convert a string to pascal case string"""
    passtr = n
    startIndex = passtr.index(' ')
    res = passtr[0:startIndex].capitalize()
    res = res + passtr[startIndex+1:].capitalize()
    if ' ' in res:
        pascal(res)
    return res        


def kebab(n):
    """This function is used to convert a string to a kebab case string"""
    kebabstr = n
    for i in kebabstr:
        if i == ' ' or i == '_':
            kebabstr = kebabstr.replace(i,'-')
    return kebabstr

def camel(n):
    """This function is used t oconvert a string to a camel case string"""
    camelstr = n
    startIndex = camelstr.index(' ')
    camel1 = camelstr[0:startIndex]
    camel1 = camel1 + camelstr[startIndex+1:].capitalize()
    if ' ' in camel1:
        camel(camel1)
    return camel1

def casegen(inputtxt,casereq):
    match casereq:
        case 'camel': 
            return camel(inputtxt)
        case 'pascal':
            return pascal(inputtxt)
        case 'kebab':
            return kebab(inputtxt)
        case 'snake':
            return snake(inputtxt)

    
inputtxt = input("Enter a string!: ")
casereq = input("Enter the case you want to convert it to: ")
print (f"The string '{inputtxt}' for a case of '{casereq}' is given by {casegen(inputtxt,casereq)}")