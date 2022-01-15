#simple calcutlator for mutli-trunk trees in inches 
#adding the total diameter of the largest trunk to one-half the diameter of each additional trunk
#Methodoloy can be found here: https://www.portland.gov/trees/tree-care-and-resources/how-measure-tree#toc-measuring-multi-stemmed-trees
#Date: 011522
#For educational purposes only

#get user input for tree data
trees = input("paste raw diameter values delimited by an x: ")

#split the tree data string into a list based on the "x" delimiter
treelist = trees.split('x')

#convert to float
Prep = [float(i) for i in treelist]

#calc tree dia in inches
multi_dia = (((sum(Prep)-max(Prep))/2)+max(Prep))
#send result to user
print("The multi-trunk Diameter is: ",round(multi_dia,2))

