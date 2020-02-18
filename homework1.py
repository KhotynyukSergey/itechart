'''#task1
n = int(input())
count = 0
for i in range(1,n+1):
    for j in range(0,i):
        if count<n:
            print(i)
            count+=1
'''




'''#task2
n = int(input("Введите количество элементов списка: "))
lst=[]
while n:
    lst.append(int(input()))
    n-=1
print("Список состоит из чисел : " + str(lst))
n = int(input("Введите число для поиска позиции в списке lst "))
result_lst=[]
for i in range(0,len((lst))):
    if n==lst[i]:
        result_lst.append(i)
if result_lst.__len__()==0:
    print("Отсутствует !")
else:
    print("Позиции : " + str(result_lst))
'''




'''#task3
def printMatrix ( matrix ):
   for row in matrix:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()
n = int(input("Ввдите количество строк матрицы : "))
k = int(input("Введите количество стобцов матрицы : "))
matrix=[]

left = 0
right = 0
top = 0
bottom = 0

resulting_matrix=[]

for i in range(n):
    matrix.append([])
    for j in range(k):
       matrix[i].append(int(input()))
    print()

for i in range(n):
    resulting_matrix.append([])
    for j in range(k):
       resulting_matrix[i].append(0)
    print()


print("Исходная матрица : ")
printMatrix(matrix)

for i in range(n):
    for j in range(k):

        if j + 1 == k:
            right = 0
        else:
            right = j + 1
        if j - 1 == -1:
            left = k - 1
        else:
            left = j - 1
        if i + 1 == n:
            bottom = 0
        else:
            bottom = i + 1
        if i - 1 == -1:
            top = n - 1
        else:
            top = i - 1
        resulting_matrix[i][j] = matrix[top][j] + \
                           matrix[bottom][j] + \
                           matrix[i][left] + \
                           matrix[i][right]
print("Конечная матрица матрица : ")
printMatrix(resulting_matrix)'''