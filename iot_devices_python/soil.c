#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define PCF       120


int main(void){
	
	int value;
	wiringPiSetup ();
	pcf8591Setup (PCF, 0x48);
	while(1){

		value = analogRead  (PCF + 0);
		int result;
		char mystr[5];
		sprintf(mystr, "%d \n", value);
		delay(1000);
		fprintf(stdout, mystr);
	}
	return 0;
}
