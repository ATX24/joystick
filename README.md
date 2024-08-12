# 🕹️ Arduino Joystick to iOS Shortcuts

Control and trigger specific iOS shortcuts using an Arduino joystick. The joystick movements and button presses are mapped to different iOS shortcuts, enabling quick and easy access to various functionalities such as taking a video, creating a recording, and more.

## Features

- **Trigger iOS Shortcuts**: The joystick can trigger iOS shortcuts based on specific combinations of movements and button presses.
- **Customizable Combinations**: Define your own combinations to trigger the shortcuts you need.

## Hardware Requirements

- Arduino Uno
- Joystick module
- Push button (integrated with the joystick)

## Software Requirements

- Arduino IDE
- Python 3.x
- PySerial library
- Some software to keep your computer open with the lid closed (Caffeinated)
^ Keeps the code running... personally, I store my computer in my backpack and have a wire connected to the joystick (which I keep in my pocket)

## Setup

1. **Hardware Setup**:
   - Connect the joystick module to the Arduino.
   - Upload the arduino file
   - Run the python code (make sure that the serial monitor on your arduino IDE is off)

2. **Software Setup**:
   - Install the Arduino IDE and upload the appropriate code to the Arduino to read joystick inputs.
   - Set up the Python environment and install the `pyserial` library using the command:
     ```bash
     pip install pyserial
     ```

3. **iOS Shortcuts**:
   - Create the shortcuts on your iOS device that you want to trigger.
   - Ensure that the shortcut names match the ones defined in your Python script.

## Future Development

In the next phase of this project, I'll be equipping a WiFi or Bluetooth module so that the joystick can stand alone 
