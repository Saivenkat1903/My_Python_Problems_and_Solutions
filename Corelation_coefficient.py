''' Python Program to calculate corelation coefficient of 2 given sets '''


data_setA=list()
data_setB=list()
data=None



while data!="B":
    data=input("Enter your first set of numbers for data set A. After you are done with data set A, type in B to start typing in values for data set B.\n")
    if data!="B":
        data_setA.append(float(data))

while data!="done":
        data=input("Start typing in values for data set B. After you are done type in 'done'\n")
        if data!="done":
            data_setB.append(float(data))



if len(data_setA)==len(data_setB):
    n=len(data_setA)
    sum_product=0
    sumB_product=0
    sumA_product=0
    sum_a=sum(data_setA)
    sum_b=sum(data_setB)
    paired=zip(data_setA,data_setB)

    for i in paired:
        product=i[0]*i[1]
        sum_product=sum_product+product

    self_productA=zip(data_setA,data_setA)
    for i in self_productA:
        product=i[0]*i[1]
        sumA_product=sumA_product+product

    self_productB=zip(data_setB,data_setB)
    for i in self_productB:
        product=i[0]*i[1]
        sumB_product=sumB_product+product

    final_num=(n*sum_product)-(sum_a*sum_b)
    final_den=((n*sumA_product-(sum_a**2))*(n*sumB_product-(sum_b**2)))**0.5
    final=final_num/final_den

    print(final)
else:
    print("Make sure the data sets have the same number of elements")
