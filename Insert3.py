class Node:
     def __init__(self,data):
         self.data=data
         self.next=None
n1=Node("va vemmilla")
n2=Node("Naan aval illai")
n3=Node("Un paer solla")
n4=Node("Muthae maniye")
n5=Node("vaayadi petha pulla")
n6=Node("Amma i love you")
n7=Node("AAsa oravae")
n8=Node("vaadi pulla vaadi")
n9=Node("Manamaganin Sathiyam")
n10=Node("Unnodu vaalatha")
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n8
n8.next=n9
n9.next=n10
head=n1
new_node=Node("silu silu")
temp=head
while temp.next:
    temp=temp.next
temp.next=new_node
temp=head
while temp is not None:
    print(temp.data)
    temp=temp.next
print("None")
