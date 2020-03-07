import random
lucky=random.randint(65,91)
for i in range(20):
    userno=input("enter a character from A-Z : ")
    gen_lucky=chr(lucky)
    if userno == gen_lucky:
        print(" CONGO !!!!! You won")
        break
    else:
        print("try again")
else:
    print("Better luck next time")
