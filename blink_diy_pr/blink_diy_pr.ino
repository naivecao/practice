/*
    blink_diy_pr.ino - a diy blink case of Practice(Program)
    Created by naivecao. Novemeber 20, 2015
    Lasted modified by naivecao. Novemeber 20, 2015
    Co,.Ltd:Lcmj
 */


void setup()
{
    Serial.begin(9600);
    pinMode(3, OUTPUT);
}

void loop()
{
    int val = analogRead(0);
    digitalWrite(3, HIGH);
    delay(val);
    digitalWrite(3, LOW);
    delay(val);
    Serial.print(val);
    Serial.print("/n");
}
