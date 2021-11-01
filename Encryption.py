import string

up = string.ascii_uppercase
low = string.ascii_lowercase
strings  = 'HelLo1223'


def encryp(strings):
    """
    function to encrypt letters 
    params:
    strings: string to be encrypted
    returns:encrypted string
    """
    
    out = ''
    for i in strings:
        if i.islower():
            out += low[-(low.index(i)+1)]
        elif i.isupper():
            out+= up[-(up.index(i)+1)]
        else:
            out+=i
    return(out)
    
def file_write(letter):
    """
    to add letter to the file
    params:
    letter: cotent to be added to the file
    returns:None
    """
    
print(encryp(strings))
