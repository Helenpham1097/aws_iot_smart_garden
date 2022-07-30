#include <stdio.h>
#include <wiringPi.h>

// cd /home/pi/SunFounder_SensorKit_for_RPi2/C/controller/
// gcc controller.c -lwiringPi
// ./a.out 1/2/3/4


void light_open(); 
void light_close();

void valve_open();
void valve_close();

int main(int argc, char *argv[]){

	wiringPiSetup ();
	
	wiringPiSetupGpio();
	pinMode(23, OUTPUT);
	pinMode(18, OUTPUT);
	
	int request = atoi(argv[1]);
	
	if (request == 1){
		light_open();
	}
	else if (request == 2){
		light_close();
	}
	else if (request == 3){
		valve_open();
	}
	else if (request == 4){
		valve_close();
	}
	
	return 0;
}

void light_open(){

	digitalWrite(23, HIGH);
}

void light_close(){

	digitalWrite(23, LOW);
}

void valve_open(){

	digitalWrite(18, HIGH);
}

void valve_close(){
	
	digitalWrite(18, LOW);
}
