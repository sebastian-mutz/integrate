# This is a module consisting of several function to convert units. This will also demonstrate the concept of nested functions.

# convert()
# ---------
# This is main function called by external script. It takes 3 input arguments:
# 1. value       - the value (floating point number) you wish to convert
# 2. currentUnit - the unit the value you passed 
# 3. targetUnit  - the unit you want your output value to be in 
# 
# It will call the appropriate converter based on the input arguments and 
# return the convertedValue. 

def convert(value, currentUnit, targetUnit):

    # k2c()
    # ---------
    # This function converts Kelvin to Celsius.
    # Input (argument): value in Kelvin
    # Output (returned): value in Celsius
    def k2c(value):
        return value-273.15

    # c2k()
    # ---------
    # This function converts Celsius to Kelvin.
    # Input (argument): value in Celsius
    # Output (returned): value in Kelvin
    def c2k(value):
        return value+273.15
    
    # Here we determine which of the converted functions will be called
    if currentUnit == 'K' and targetUnit == 'C':
        convertedValue = k2c(value)
    elif currentUnit == 'C' and targetUnit == 'K':    
        convertedValue = c2k(value)        
    else:
        print("Invalid arguments")
        
    # return the converted value                
    return convertedValue
