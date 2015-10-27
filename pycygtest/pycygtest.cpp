// pycygtest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

#include <Python.h>

extern "C"
{
	void Py_Initialize();

}

using namespace std;

int

main(int argc, char *argv[])
{
	//Py_SetProgramName(argv[0]);  /* optional but recommended */
	//Py_Initialize();
	//PyRun_SimpleString("from time import time,ctime\n"
	//	"print 'Today is',ctime(time())\n");
	//Py_Finalize();
	
	
	

	cout << getenv("ROS_PACKAGE_PATH") << endl;


	return 0;
}
