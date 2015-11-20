/*
    blink_diy.ino - a diy blink case of Practice(Program)
    Created by naivecao. Novemeber 20, 2015
    Lasted modified by naivecao. Novemeber 20, 2015
    Co,.Ltd:Lcmj
 */


int m = 0;
int s = 1;
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
    for(int n = 0; n <= 255; n +=  5 * (m + 1 ))
    {
        switch(m)
        {
            case 0:
            analogWrite(3, n);
            break;
            case 1:
            analogWrite(5, n);
            break;
            case 2:
            analogWrite(6, n);
            break;
            case 3:
            analogWrite(9, n);
            break;
            case 4:
            analogWrite(10, n);
            break;
            case 5:
            analogWrite(11, n);
            break;
        }
        delay(30);
    }
    
    for(int n = 255; n >= 0; n -= 5)
    {
        switch(m)
        {
            case 0:
            analogWrite(3, n);
            break;
            case 1:
            analogWrite(5, n);
            break;
            case 2:
            analogWrite(6, n);
            break;
            case 3:
            analogWrite(9, n);
            break;
            case 4:
            analogWrite(10, n);
            break;
            case 5:
            analogWrite(11, n);
            break;
        }
        delay(30);
    }
    
    m = m + s;
    if(m == 5 || m == 0)
    {
        s = -s;
    }
}
