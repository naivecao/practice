/*
    blink_diy.ino - a diy blink case of Practice(Program)
    Created by naivecao. Novemeber 20, 2015
    Lasted modified by naivecao. Novemeber 20, 2015
    Co,.Ltd:Lcmj
 */


int m = 0;
int s = 1;
int p = 0;
int pr = 0;
void setup()
{
        pinMode(3, OUTPUT);
        pinMode(5, OUTPUT); 
        pinMode(6, OUTPUT); 
        pinMode(9, OUTPUT); 
        pinMode(10, OUTPUT); 
        pinMode(11, OUTPUT); 
}

void loop()
{
    pr = analogRead(0);
    if (pr <= 550)
    {
        for(int n = 0; n <= 255; n +=  5 * (m + 1 ))
        {
            switch(m)
            {
                case 0:
                p = 3;
                break;
                case 1:
                p = 5;
                break;
                case 2:
                p = 6;
                break;
                case 3:
                p = 9;
                break;
                case 4:
                p = 10;
                break;
                case 5:
                p = 11;
                break;
            }
            analogWrite(p, n);
            delay(30);
        }
        
        for(int n = 255; n >= 0; n -= 5)
        {
            analogWrite(p, n);
            delay(30);
        }

        m = m + s;
        if(m == 5 || m == 0)
        {
            s = -s;
        }
    } else {
        int randVal = random(0, 1000);
        digitalWrite(3, HIGH);
        delay(randVal);
        digitalWrite(3, LOW);
        delay(randVal);
    }
}
