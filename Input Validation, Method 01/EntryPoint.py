#check if the zipcode input is numeric
if __name__ == '__main__': 
            
    try:
        zipCode = int(input())    
        print(f'Your zip code is {zipCode}.')

    except:
        print('Please use numeric digits for the zip code.')
