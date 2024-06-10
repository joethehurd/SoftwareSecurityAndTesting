from string import Template

CONFIG = {

    "API_KEY": "'you've just exposed your secret_key'"
}
class User:

    name = ""
    email = ""

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def __str__(self):

        return self.name
        
if __name__ == '__main__':
    name = input()
    email = input()
    
    user = User(name, email)
        
    temp_string = "Hello, my name is $name." 
    temp_object = Template(temp_string)    
    
    print(temp_object.substitute(name=f"{name}"))     
