import serial

ser = serial.Serial("/dev/cu.usbmodem1101",'9600')
door1 = False
door2 = False
print('unlock the door')

while True:
    
    if door1 and door2:
        print('You have unlocked the door!')
        break

    read = ser.readline().decode('ascii')
    readArray = read.split()
    print(readArray)
    c = readArray[0]
    x = readArray[1]
    y = readArray[3]
    m = readArray[5]
    
    if x == '0':
        door1 = True
        print('You got through the x checkpoint')
    if y == '0':
        door2 = True
        print('You got through the y checkpoint')
    
    

