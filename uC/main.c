//Grundeinstellungen für CPU
#define F_CPU 12500000UL

//Erweiterte Bibliotheken zur Verwendung
#include <avr/io.h>
#include <util/delay.h>

//Definiton von "delay" als fester Wert für die Funktion _delay_ms()
#define delay 250

//Deklaration ("Bekanntmachung") der Funktionen damit es zu keinen Fehler kommt
//Hinweis: Nur notwendig wenn die Funktion erst am Ende des Files ausgeführt werden
void eventall(void);
void eventt1(void);
void eventt2(void);
void eventt3(void);
void eventt4(void);

//Funktion zur Definition der Ein-/Ausgänge
void init(void)
{
	
	//Taster Reset:	C6
	//Taster:		T2.1 = D1; T2.2 = D7; T2.3 = B0; T2.4 = B1
	//LED:			1 = C2; 2 = C1; 3 = C0; 4 = C3; 5 = C4;
	//				6 = C5; 7 = B5; 8 = B4; 9 = B3; 10 = B2;
	
	//1 = Ausgang; 0 = Eingang
	//0b76543210
	
	DDRB |= 0x3C; //0b00111100
	DDRC |= 0x3F; //0b00111111
	DDRD |= 0x00; //0b00000000
}

int main(void)
{
	init();
	for (;;)
	{
		//T2.1 check
		if (PIND & 0x02)
		{
			eventt1();
		}
		
		//T2.2 check
		else if (PIND & 0x80)
		{
			eventt2();
		}
		
		//T2.3 check
		else if (PINB & 0x01)
		{
			eventt3();
		}
		
		//T2.4 check
		else if (PINB & 0x02)
		{
			eventt4();
		}
	}
}

void eventall(void)
{
	
	//LED 1 an und aus
	PORTC |= 0x04;
	_delay_ms(delay);
	PORTC &= 0xFB;
	
	//LED 2 an und aus
	PORTC |= 0x02;
	_delay_ms(delay);
	PORTC &= 0xFD;
	
	//LED 3 an und aus
	PORTC |= 0x01;
	_delay_ms(delay);
	PORTC &= 0xFE;
	
	//LED 4 an und aus
	PORTC |= 0x08;
	_delay_ms(delay);
	PORTC &= 0xF7;
	
	//LED 5 an und aus
	PORTC |= 0x10;
	_delay_ms(delay);
	PORTC &= 0xEF;
	
	//LED 6 an und aus
	PORTC |= 0x20;
	_delay_ms(delay);
	PORTC &= 0xDF;
	
	//LED 7 an und aus
	PORTB |= 0x20;
	_delay_ms(delay);
	PORTB &= 0xDF;
	
	//LED 8 an und aus
	PORTB |= 0x10;
	_delay_ms(delay);
	PORTB &= 0xEF;
	
	//LED 9 an und aus
	PORTB |= 0x08;
	_delay_ms(delay);
	PORTB &= 0xF7;
	
	//LED 10 an und aus
	PORTB |= 0x04;
	_delay_ms(delay);
	PORTB &= 0xFB;
	
}

void eventt1(void)
{
	for(int i = 0; i < 2; i++)
	{
		//LED 1 an und aus
		PORTC |= 0x04;
		_delay_ms(delay);
		PORTC &= 0xFB;
				
		//LED 10 an und aus
		PORTB |= 0x04;
		_delay_ms(delay);
		PORTB &= 0xFB;
	}
	
	eventall();	
}

void eventt2(void)
{
	for(int i = 0; i < 2; i++)
	{
		//LED 2 an und aus
		PORTC |= 0x02;
		_delay_ms(delay);
		PORTC &= 0xFD;
		
		//LED 9 an und aus
		PORTB |= 0x08;
		_delay_ms(delay);
		PORTB &= 0xF7;
	}
	
	eventall();
}

void eventt3(void)
{
	for(int i = 0; i < 2; i++)
	{
		//LED 3 an und aus
		PORTC |= 0x01;
		_delay_ms(delay);
		PORTC &= 0xFE;
		
		//LED 8 an und aus
		PORTB |= 0x10;
		_delay_ms(delay);
		PORTB &= 0xEF;
	}
	
	eventall();
}

void eventt4(void)
{
	for(int i = 0; i < 2; i++)
	{
		//LED 4 an und aus
		PORTC |= 0x08;
		_delay_ms(delay);
		PORTC &= 0xF7;
		
		//LED 7 an und aus
		PORTB |= 0x20;
		_delay_ms(delay);
		PORTB &= 0xDF;
	}
	
	eventall();
}
