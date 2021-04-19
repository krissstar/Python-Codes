#........ and shoot for the Sky in you getting a big promotion & opportunity
#Enter Full Names
print("Enter First and Last Name:")

fname = input()
lname = input ()

fullnames = fname + "" + lname
#Enter phone, email
print("Enter Customer's Phone Number: ")
phone = input()
print("Enter Customer's email aaddress: ")
email = input()
#price of a used car
price = 10000
print("Good credit? y/n?" )
check =input()



has_good_credit = True;
if check == "y":
#if has_good_credit:
 down_payment = 0.1 * price
else:
 down_payment = 0.2 * price
print("fDown Payment : " , +down_payment)
print('')
print("Full Names:"  +fullnames)
print("Phone: " +phone)
print("Email: " + email)
print("Down Payment: ", +down_payment)