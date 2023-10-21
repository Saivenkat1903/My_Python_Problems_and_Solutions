''' Makes a bar graph of Expenses vs Expenditure '''

from matplotlib import pyplot as plt


number_of_categories=int(input("Enter the number of categories\n"))

category_list=list()
expense_list=[]


for i in range(number_of_categories):
    category=input("Enter category:\n")
    expense=input("Enter Expenditure:\n")
    category_list.append(category)
    expense_list.append(int(expense))

thing=len(expense_list)

plt.barh(category_list,expense_list,align='center')
plt.xlabel("Expenses")
plt.ylabel("Categories")
plt.title("Expenditure per category every month")
plt.axis(xmin=0)
plt.show()
