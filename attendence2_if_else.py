# modify the above qoe to allow student to sit if he/she has medical cause. 
# ask user if he/she has medical cause or not "y" or "n" and print accordingly.
medical=input("do you have medical cause yes or no:")
# if medical=="yes":
#     print("you are allowed ")
    
# class_held=int(input("number of classes heid:"))
# class_att=int(input("number of classes attending:"))
# total_atte=class_held/class_att*100

if medical=="yes":
    print("you are allowed ")
else:
    class_held=int(input("number of classes heid:"))
    class_att=int(input("number of classes attending:"))
    total_atte=class_held/class_att*100
    if total_atte>=75:
        print("allowed")
    else:
        print("not allowed")