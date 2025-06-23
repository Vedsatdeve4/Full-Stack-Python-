#Build in function on list

li6 = [50,20,30,40,10]
print("li6 =", li6)
print("max =", max(li6))
print("min =", min(li6))
print("len =", len(li6))
print("sorted =", sorted(li6))
print("sorted_rev =", sorted(li6, reverse= True))
print()


#Build in method on List

li7 = [10,20,30,40,50]
print("li7 =", li7)

#Insertion
print("Insertion Method")

#1.To add single element at the end of the list

li7.append(60)
print("li7 =", li7)

#2.To add Multiple element at the end of the list

li7.extend([70,80])
print("li7 =", li7)

#3.To add single element at the particular index of the list

li7.insert(2,25)
print("li7 =", li7)
print()

#Remove
print("Remove Method")
#1.To remove the last element of the list

li7.pop()
print("li7 =", li7)

#2.To remove the element at the particular index of the list

li7.pop(2)
print("li7 =", li7)

#3.To remove the particular element of the list
li7.remove(50)
print("li7 =", li7)

#4.To remove all the element of the list
li7.clear()
print("li7 =", li7)
print()

#Indexing
li8 = [10,20,30,40,50,10,10,10]
print(li8.index(50))
print(li8.index(10))
# print(li8.index(99))  #Error


#Counting

print(li8.count(10))
print(li8.count(99))


        
