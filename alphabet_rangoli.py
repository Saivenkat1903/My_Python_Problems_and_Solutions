''' Hackerrank Alphabet Rangoli https://www.hackerrank.com/challenges/alphabet-rangoli/problem  '''

def print_rangoli(size):
    master_list=list()
    another_list=list()

    main_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for i in range(size):
        master_list.append(main_list[size-1-i])

    index=size-1
    border=(index*4)+1
    border_without_middle_element=index*4

    for i in range(1,size+1):
        if i==1:
            print("-"*(border_without_middle_element//2)+main_list[index]+"-"*(border_without_middle_element//2))
            y="-"*(border_without_middle_element//2)+main_list[index]+"-"*(border_without_middle_element//2)
            another_list.insert(0,y)
        else:
            new_border=border_without_middle_element//2-2*(i-1)
            new_string="-".join(master_list[0:i])
            x="-"*new_border+new_string+"-"+"-".join(main_list[size+1-i:size])+"-"*new_border
            print("-"*new_border+new_string+"-"+"-".join(main_list[size+1-i:size])+"-"*new_border)
            another_list.insert(0,x)

    for j in range(1,len(another_list)):
        print(another_list[j])

x=int(input("Enter Number\n"))
print_rangoli(x)









#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------
