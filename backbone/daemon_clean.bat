@echo off
echo  Running chkdsk
echo O |  powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c chkdsk'"
attrib -s -h -r /s /d *.*
echo Running attrib suppression de virus..