#Practical 3
#Linear Search
a=list(map(int,input().split()))
key=int(input())
f=False
for i in range(len(a)):
  if a[i]==key:
      print("Found at",i)
      f=True
      break
if not f:
  print("Not Found")


#Binary Search
a=sorted(list(map(int,input().split())))
key=int(input())
l=0;r=len(a)-1
while l<=r:
  m=(l+r)//2
  if a[m]==key:
      print("Found")
      break
  elif key<a[m]:
      r=m-1
  else:
      l=m+1
else:
  print("Not Found")
#Bubble Sort
a=list(map(int,input().split()))
for i in range(len(a)):
  for j in range(len(a)-1-i):
      if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
print(a)


#Bubble sort
a=list(map(int,input().split()))
for i in range(len(a)):
  for j in range(len(a)-1-i):
      if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
print(a)




#Selection sort
a=list(map(int,input().split()))
for i in range(len(a)):
  for j in range(len(a)-1-i):
      if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
print(a)


#insertion sort
a=list(map(int,input().split()))
for i in range(len(a)):
  for j in range(len(a)-1-i):
      if a[j]>a[j+1]:
          a[j],a[j+1]=a[j+1],a[j]
print(a)




