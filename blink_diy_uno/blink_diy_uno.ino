/*
    blink_diy_uno.ino - a diy blink case of Practice(Program)
    Created by naivecao. Novemeber 20, 2015
    Lasted modified by naivecao. Novemeber 20, 2015
    Co,.Ltd:Lcmj
 */


void setup()
{
    pinMode(13, OUTPUT);
}

void loop()
{
    int randVal = random(0, 1000);
    digitalWrite(13, HIGH);
    delay(randVal);
    digitalWrite(13, LOW);
    delay(randVal);
}
