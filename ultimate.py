import serial
import subprocess
import time

ser = serial.Serial("/dev/cu.usbmodem1101", '9600')


# Define your combinations and corresponding iOS shortcut commands
combos_to_shortcuts = {
    ('down', 'up', 'left', 'right', 'button'): 'Take Video',
    ('up', 'down', 'button', 'right', 'left'): 'Take Screenshot',
    ('left', 'right', 'down', 'up', 'button'): 'Create Recording',
    ('right', 'left', 'button', 'down', 'up'): 'NPR News Now',
    ('left', 'right',): "Play/Pause"
}

combo = []
counter = 0

while True:
    read = ser.readline().decode('ascii')
    readArray = read.split()
    print(readArray)
    
    c = readArray[0]
    x = readArray[1]
    y = readArray[3]
    m = readArray[5]

    if y == '1023':
        if 'down' not in combo:
            combo.append('down')
    if y == '0':
        if 'up' not in combo:
            combo.append('up')

    if x == '0':
        if 'left' not in combo:
            combo.append('left')

    if x == '1023':
        if 'right' not in combo:
            combo.append('right')
    
    if m == 'pressed':
        if 'button' not in combo:
            combo.append('button')

    # Check if the current combo matches any defined shortcuts
    combo_tuple = tuple(combo)
    print(f'Current combo: {combo}')
    if combo_tuple in combos_to_shortcuts:
        shortcut = combos_to_shortcuts[combo_tuple]
        print(f'Triggering iOS Shortcut: {shortcut}')
        
        # Use URL scheme to trigger the shortcut
        subprocess.run(['open', f'shortcuts://run-shortcut?name={shortcut.replace(" ", "%20")}'])
        time.sleep(2)
        combo = []
        
    
    counter += 1
    if counter == 100:
        counter = 0
        combo = []
