#include "MeOrion.h"

MeDCMotor motor(M2);

uint8_t motorSpeed = 200;
char cmd;
void setup() {                   
    Serial.begin(9600);
}

void loop() {
    if(Serial.available()){
        cmd = Serial.read(); 
        printf("%c",cmd);
        if(cmd=='a'){
            motor.run(motorSpeed);
            delay(3000);
            motor.stop();
        }
        else if(cmd=='b'){
            motor.run(-motorSpeed);
            delay(3000);
            motor.stop();
        }
    }
}