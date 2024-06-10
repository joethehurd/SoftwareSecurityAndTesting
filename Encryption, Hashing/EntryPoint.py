import hashlib

def hash_password(pwd):
    # encode password string to bytes
    enc_pwd = pwd.encode()     
    
    # encrypt bytes
    d = hashlib.sha3_256(enc_pwd)  
    
    # generate binary hash of password string in hexidecimal  
    hash = d.hexdigest()# simply use hexdigest to satisfy exam security requirements    
    
    return hash
    
if __name__ == '__main__':
    pwd = input()   
    
    print(hash_password(pwd))
