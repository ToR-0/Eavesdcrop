#include <iostream>
#include <windows.h>
using namespace std; 
void openit() {
	// Name of program
	system("pyinstaller --onefile eclient.py");
	// put the other CPP program in the directory and compile it!
}
int main() {
	HWND windowed;
	windowed = FindWindowA("ConsoleWindowClass", NULL);
	ShowWindow(windowed, 0);
	openit();
	// Don't forget to compile me ;)
}
