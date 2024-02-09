// Pin-Definitionen
const int buttonPin[] = {3, A4, A5, 2}; // Taster Pins
const int ledPins[] = {16, 17, 12, 15, 14, 13, 8, 7, 6, 4}; // LED Pins
const int rgbPins[] = {9, 10, 11}; // RGB-LED Pins
const int piezoPin = 5; // Piezo Pin
const int potPin = A6; // Potentiometer Pin

const int delay_time = 250;

// Funktion zur Ausführung der Aktionen
void performActions() {
  // a) LEDs nacheinander aufleuchten lassen
  for (int j = 0; j < 10; j++) {
    digitalWrite(ledPins[j], HIGH);
    delay(delay_time);
    digitalWrite(ledPins[j], LOW);
  }

  // b) RGB-LED in allen drei Grundfarben leuchten lassen
  for (int j = 0; j < 3; j++) {
    digitalWrite(rgbPins[j], HIGH);
    delay(delay_time);
    digitalWrite(rgbPins[j], LOW);
  }

  // c) Piezo piepsen lassen
  tone(piezoPin, 1000, delay_time); // Ändere die Dauer des Tons auf 100 Millisekunden
}

void checkButton() {
  // Warten, bis ein Taster gedrückt wird
  for (int i = 0; i < 4; i++) {
    if (digitalRead(buttonPin[i]) == HIGH) {
      // Taster gedrückt
      performActions();
    }
  }
}

void checkPoti() {
  // Poti lesen und LEDs entsprechend steuern
  int potValue = analogRead(potPin);
  Serial.println(potValue);
  int numLEDs = map(potValue, 0, 1023, 0, 10);

  // LEDs steuern
  for (int i = 0; i < 10; i++) {
    digitalWrite(ledPins[i], i < numLEDs ? HIGH : LOW);
  }
}


void setup() {
  // Initialisierung der Pins
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPin[i], INPUT_PULLUP);
  }
  for (int i = 0; i < 10; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  for (int i = 0; i < 3; i++) {
    pinMode(rgbPins[i], OUTPUT);
  }
  pinMode(piezoPin, OUTPUT);
}

void loop() {
  checkButton();
  checkPoti();
}
