int VRx = A0;
int VRy = A1;
int SW = 2;

void setup() {
  pinMode(SW, INPUT_PULLUP);
  Serial.begin(9600);      // Serial Monitor
}

void loop() {
  int xValue = analogRead(VRx);
  int yValue = analogRead(VRy);
  int buttonState = digitalRead(SW);

  String data = "X: " + String(xValue) + " Y: " + String(yValue) + " Button: " + (buttonState == LOW ? "pressed" : "released");

  Serial.println(data);     
  
  delay(100);
}
