from random import randint
file = open("customer.txt", "r")
customerdare = file.read().splitlines()
file.close()
while '' in customerdare:
    customerdare.remove('')
print(customerdare)

# I am trying to allow the system to create a randomly generated number which
# doesnt already exist within the customer.txt file
# This is working fine but it is reading the whole file, including phonenumber
# and postocde, ect.. i am trying to only allow the system to read the number Id
# and put it into another array
# with the real system we are able to add to the cumstomer.txt so it has to be
#able to allow other accounts to be added


#for i in range(len(customerdare)):
 #   customerdare[i][::4]
  #  array_id = customerdare 
   # print(array_id)

#member_num = input("Create a 4 digit code for your Member Number: ")
member_num = randint(1000,9999)
a = str(member_num)
verify = False

while verify == False:
    with open('customer.txt') as f:
        if a in f.read():
            member_num = randint(1000,9999)
            a = str(member_num)
        elif a not in f.read():
            verify = True
       
print("\n")
print("Member Number: " + a)
print("\n")
