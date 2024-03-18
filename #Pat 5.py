#Pat 5 ques1 expected output of the pythoncode 
data =[10,501,22,37,100,999,87,351]
result=filter(lambda x:x>4,data) #lamdba expression check for value which is greater than 4 and in given input list all values are greater than 4
print(list(result))


#Pat 5 ques 2 write a python code using Lambda function to check every element of alist is an integer or string?
List =[20,30,"Priyanka",45]#take a list which is having int and string value
Intger=list(map(lambda List:int if isinstance(List,int) else str ,List)) # here in lamda function we are checking for int values
print(Intger)


#Pat 5 ques 3 Fibonacee series from 1 to 50 using Lambda function

def fibonacci(count):#creating fibonacci function
	fib_list = [1, 2] #declaring list
	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2, count))) #adding last 2 items of list and appending 
	                                                                        #in existing list, range from 2 to 50
	                                                                         

	return fib_list[:count] #returning list of elemnts from starting to end count-1

print(fibonacci(50)) #print and calling of fibonacci function


#mobile no of bangladesh 880 1xxx NNNNNN  this is tha pattern(13 digit number)
import re #to use regular expression class 
def validate_bangladeshno(number):#create function to  validate bangaldesh number
  pattern =r'^(\+880)+([\s.-]?1[0-9]{3})+([\s.-]?[0-9]{6})$'#regular expresssion of banagladesh
  if re.fullmatch(pattern,number):
    return True
  else:
     return False


banglanumber1="+880.1234.567453"
print("valid bangaldesh number:",validate_bangladeshno(banglanumber1))#call of function through print statements
banglanumber2="111234567453"
print("valid bangaldesh number:",validate_bangladeshno(banglanumber2))
banglanumber3="+8801234567453"
print("valid bangaldesh number:",validate_bangladeshno(banglanumber3))


#mobike no of US starts with +1 and total of 10 digit
import re
def validate_Usnumber(number):#create validate US number function
  pattern =r'^(\+1)+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{3})+([\s.-]?[0-9]{4})$'#regular expression of US number
  if re.match(pattern,number):
    return True
  else:
     return False


number1="+1-234-768-6871"
print("valid US number:",validate_Usnumber(number1))#call of function inside print statement
number2="+11123456745"
print("valid US number:",validate_Usnumber(number2))
number3="1880 1234 567453"
print("valid  US number:",validate_Usnumber(number3))



#check correct format of password-16 alphanumericchars uparcase, lowercase, special chars, numbers
import re
def validate_Password(password):#create function to validate password
   pattern=r'\b[A-Za-z0-9@$!%*#?&]{16}$'#regular expression of password 
   match=re.fullmatch(pattern,password) #condiiton to validate password with pattern of password
   if match:
    return("yes")
   else :
    return("no")

password1="Yh54@#bn89&*%er5"
print("valid password",validate_Password(password1))#call of function inside print statement
password2="AAAAAAZZYYHH1&RG"
print("valid password",validate_Password(password2))
password3="$2#$@#%%$&^RFVG1"
print("valid password",validate_Password(password3))



#Pat 5 email address
import re
def validate_emailaddress(emailaddress): # created function to validate email address
   pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' #regular expression
   if re.fullmatch(pattern,emailaddress): #condiiton to validate email address with pattern of email address
    return("yes")
   else :
    return("no")
emailaddress1="priyanka.kapoor@hmail.com"
print("valid password",validate_emailaddress(emailaddress1)) #calling of function inside print statement
emailaddress2="1234@gmail.com"
print("valid password",validate_emailaddress(emailaddress2))
emailaddress3="priya%gmail.com"
print("valid password",validate_emailaddress(emailaddress3))