# Kaun Banega Crorepati.

name=str(input("Enter your name : "))
print("Hi",name.title(),end=", Welcom to Kaun Banega Crorepati (KBC).\n")
print("\nHere is your first quetion.")

quetions=["(1) What is the capital of India?","(2) How many planets in solar system?","(3) What is the currency of Japan?","(4) Who is the current Prime Minister of the India?","(5) What is the National flower of the India?"]

amount=[10000000,20000000,30000000,40000000,50000000]

print(quetions[0],"\n   (a) Mumbai, (b) Karnataka\n   (c) Gandhinagar, (d) Delhi")
ans0=input("Enter yor answer : ")
if ans0=='d' or ans0=='D':
    print("Your answer is correct.You won the $",amount[0],"\n","\nHere is yor next quetion.")
    print(quetions[1],"\n   (a) 4, (b) 8\n   (c) 5, (d) 9")
    ans1=input("Enter yor answer : ")
    if ans1=='b' or ans1=='D':
        print("Your answer is correct.You won the $",amount[1],"\n","\nHere is yor next quetion.")
        print(quetions[2],"\n   (a) Yen, (b) Euro\n   (c) Dollar (d) Pound")
        ans2=input("Enter yor answer : ")
        if ans2=='a' or ans2=='A':
            print("Your answer is correct.You won the $",amount[2],"\n","\nHere is yor next quetion.")
            print(quetions[3],"\n   (a) Sardar Patel, (b) Narendra Modi\n   (c) Rahul Gandhi, (d) Indira Gandhi")
            ans3=input("Enter yor answer : ")
            if ans3=='b' or ans3=='B':
                print("Your answer is correct.You won the $",amount[3],"\n","\nHere is yor next quetion.")
                print(quetions[4],"\n   (a) Rose, (b) Sunflower\n   (c) Lotus, (d) Jasmine")
                ans4=input("Enter yor answer : ")
                if ans4=='c' or ans4=='C':
                    print("Your answer is correct.You won the $",amount[4],"\n""\nNIce to Play Wjit you. Game Over....")
                else:
                    print("Your answer is wrong...!.Correct answer is (c) Lotus. Nice to play with you.")
            else:
                print("Your answer is wrong...!.Correct answer is (b) Narendra Modi. Nice to play with you.")
        else:
            print("Your answer is wrong...!.Correct answer is (a) Yen. Nice to play with you.")
    else:
        print("Your answer is wrong...!.Correct answer is (b) 8. Nice to play with you.")
else:
    print("Your answer is wrong...!.Correct answer is (d) Delhi. Nice to play with you.")