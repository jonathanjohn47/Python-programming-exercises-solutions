import re
p = str(input("Enter passwords separated by commas"))
x = p.split(',')
y = []
for s in x:
    def checksmallletter(s):
        if(re.search(r'[a-z]', s)):
            return True
        else:
            return False

    def checkcapital(s):
        
        if(re.search(r'[A-Z]', s)):
            return True
        else:
            return False
    def checkspecial(s):
        if(re.search(r'[@#$]', s)):
            return True
        else:
            return False
    def checknum(s):
        if(re.search(r'[0-9]', s)):
            return True
        else:
            return False
    def checklen(s):
        if(len(s)>=6) and (len(s)<=12):
            return True
        else:
            return False
    '''
    print(checksmallletter(s))
    print(checkcapital(s))
    print(checkspecial(s))
    print(checknum(s))
    print(checklen(s))
    '''
    if(checksmallletter(s)==True):
        if(checkcapital(s)==True):
            if(checkspecial(s)==True):
                if(checknum(s)==True):
                    if(checklen(s)==True):
                        y.append(s)
                    else:
                        print("Password Format Not Correct")
                else:
                        print("Password Format Not Correct")
            else:
                        print("Password Format Not Correct")
        else:
                        print("Password Format Not Correct")
    else:
                        print("Password Format Not Correct")
print(y)