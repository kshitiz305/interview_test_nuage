import string
import sys




up = string.ascii_uppercase
low = string.ascii_lowercase



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
    
    result = encryp(letter)
    file1 = open("Result.txt","a+")
    file1.write(f"{result} \n")
    file1.close()



file_write(sys.argv[1])
