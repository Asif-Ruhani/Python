List=[5,9,10,45,78,23,1,0,-6,-12,-75,56,32]
print(List)

List1=List[0:3] # copy from 0 index to till 3 index( 0,1,2 index)
List2=List[:3]  # copy from 0 index to till 3 index( 0,1,2 index)
print(List1)
print(List2)

List3=List[5:] # copy from 5 index to last
print(List3)

List4=List[3:8]  # copy from 3 index to till 8 index(3,4,5,6,7 index)
print(List4)

List5=List # full copy
print(List5)