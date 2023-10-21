"""Challenge 1check

Write a function called linear_search_product that takes the list of products
and a target product name as input. The function should perform a linear search 
to find the target product in the list and return a list of indices of all 
occurrences of the product if found, or an empty list if the product is not found.

"""

def linear_search_product(ProductList,TargetProduct):
    indexs =[]
    
    for index,item in enumerate(ProductList):
        if item == TargetProduct:
            indexs.append(index)
    return indexs


p_list = ['apple','orange','mango','apple','banana','apple']
target = 'apple'
target1 = 'tomato'
res = linear_search_product(p_list,target)
print(res)
