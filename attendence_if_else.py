# a student will not be allowed to sit in exam if his/her attendence is less than 75%. 
# is student is allowed to sit in exam or not.

class_held=int(input("number of classes heid:"))
class_att=int(input("number of classes attending:"))
total_atte=class_held/class_att*100
if total_atte>=75:
    print("you are allowed to sit in exam")
    medical=input("you have medical cause yes or no:")
else:
    print("sorry, you are not allowed. attend more classes from next time.")

