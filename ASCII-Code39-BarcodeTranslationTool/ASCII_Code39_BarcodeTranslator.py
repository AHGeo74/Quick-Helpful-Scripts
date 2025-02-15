characters = {'048':'0', '049':'1', '050':'2', '051':'3', '052':'4', '053':'5', '054':'6', '055':'7', '056':'8', '057':'9'}

while True:

    longcode = input('Input long form code here: ')

    counter = 0

    str = ''
    barcode = ''

    for c in longcode:
        if counter <= 2:
            str += c
            #print(str)
            counter += 1
        else:
            for key, value in characters.items():
                if str == key:
                    barcode += value
                    counter = 0
                    #print(barcode)
            str = c
            counter += 1
            
    for key, value in characters.items():
        if str == key:
            barcode += value
            str = ''
            counter = 0           
                
    print(barcode)
