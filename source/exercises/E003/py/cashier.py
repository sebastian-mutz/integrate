# This pythong script contains a function to lookup product prices for passed products and a function sum these up to return the total.
#
# This is a dictionary of product prices. It is not part of any specific function below and can therefore be accessed from anywhere in the script.
productPriceDict = {'apples':1.50,'doggeFood':2.99,'myPhone18':99999.99,'freedomFromCapitalism':0.0}
#
# function looks up the prices of products
def lookupPrice(product): 
    price = productPriceDict[product]               # loop up the price of a product based on the passed product name and the price dictionary
    return price                                    # return the price to the script/code block that called this function
#    
# this function calculate the total based on passed product list
def calculateTotal(productList):   
    total = 0.0                                     # explicitly set the total to zero before summing up prices
    for i in range ( len(productList) ):            # loop through the list of products
        total = total + lookupPrice(productList[i]) # update the total by looking up the price of the product and adding it to the total
    return total                                    # return the total to the script/code block that called this function 
