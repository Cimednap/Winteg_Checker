# Winteg_Checker
Simple Windows file integrity checker.

Can be used to create a baseline file to store hashes of [file names : content] and to check the intergrity of the files stored in the baseline file.    

`winteg_checker.py -h`  
*usage: winteg_checker.py [-h] [-b [BASELINE]] [-c [CHECKER]] [-d DIRECTORY]* 

optional arguments:  
  -h, --help     show this help message and exit  
  -b [BASELINE]  Creates baseline file, default is baseline.txt, custom file
                 name can be passed.  
  -c [CHECKER]   Runs an intregrity check on the passed baseline file  
  -d DIRECTORY   The starting path of the intergrity checker, used in
                 combination with [-b]
