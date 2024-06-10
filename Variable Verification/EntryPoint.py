# verify you only have digits
def check_numeric_value(demo_int):
    
    return isinstance(demo_int, int)            

# verify if the string is null
def check_null_string (demo_string):  
   
    if demo_string is not None:            
        return True
    else:
        return False
    
       
if __name__ == '__main__':  
    
    # Test Case 1
    demo_string = "This is a demo." 
    demo_int = 12345

    # Test Case 2
    #demo_string = None 
    #demo_int = 12345

    # Test Case 3
    #demo_string = None 
    #demo_int = "This is a demo." 

    print(check_null_string (demo_string))
    print(check_numeric_value(demo_int))
