arrangeArray (int a[], int size)
{
    oddInd = 1
    evenInd = 0
    while (true)
    {
        while (evenInd < size && a[evenInd]%2 == 0)
            evenInd += 2;
        while (oddInd < size && a[oddInd]%2 == 1)
            oddInd += 2;
        if (evenInd < size && oddInd < size)
            swap (a[evenInd], a[oddInd])
        else
            break;
    }
 
}


# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    lst.append(ele) # adding the element

arrangeArray(lst, n)

