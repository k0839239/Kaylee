
#file1 = open('kayleeberns_original.txt')
#for line in file1.readlines():
        #print(line.shift())

def get_text():
    try:
        number = int(input('Enter a number 1-26:  '))
        if number in range(1, 27):
            return number
        else:
            print("Invalid number")
            return get_text()
    except:
        print("not a valid input")
        return get_text()
    
get_text()

alphabet = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

return number-1