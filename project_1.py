# Email Validation in Python (Using String Function)

email = input("Enter your Email : ")
a, b, c = 0, 0, 0
# 1 Email should has more than 6 charachter.
if len(email) >= 6:
    # 2 Email has first latter is Alphabet.
    if email[0].isalpha():
        # 3 Email should has atleast one @. 
        if ("@" in email) and (email.count("@") == 1):
            # 4 Position of "." should on third or fourth from last.
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    # 5 If email has space.
                    if i == i.isspace():
                        a = 1
                    # 5 Email has alphabet.
                    elif i.isalpha():
                        # 5 Email has lower case.
                        if i==i.upper():
                            b=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        c=1
                if a==1 or b==1 or c==1:
                    print("Wrong Email 5")
                else:
                    print("Right Email")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1")