#Windows Integrity Checker
#Matt Hart
#9/30/2016

import datetime							#import datetime  module for prettier time outputs
import os                       		#import os module for os.walk function
import hashlib                      	#import hashlib module for those juicy hash digests
import errno		         			#import errno  module for error handling
#import system 							#import system module for handling system calls
from winteg_func import *				#import winteg functions for various uses
from termcolor import colored           #import termcolor to make things pretty
import colorama

def main():
	
    #initialize pretty colors and counts
    colorama.init()
    baselineFiles = 0
    checkedFiles = 0
    #Call getOptions to grab CLI arguments
    baseline, check, directory = getOptions()

    #check to see if creating a baseline or checking a baseline
    #Creating a baseline
    if check == 'empty':
        #Create/open baseline file
        baseFile = open(baseline, "w")
        #Walk the specified directory, hash any files, write out to baseline file
        for root, dirs, files in os.walk(directory, topdown=True):
            for name in files:		
                current_file = (os.path.join(root, name))
                current_hash = hashFile(current_file)
                print current_file + " " + current_hash
                baseFile.write(current_file + " " + current_hash + "\n")  
                #increment baseline file count
                baselineFiles = baselineFiles + 1
        print "Number of files added to baseline: " + str(baselineFiles)
    #checking a baseline
    else:
        #Open baseline file to check
        with open(check) as checked:
            content = checked.readlines()
            #initialize list
            data = {}
            #split data into filenames and hash
            for line in content:
                parsed = line.split(' ')
                data[parsed[0]] = parsed[1]
            #hash files listed in baseline file, store in $tempHash
            for key in data.keys():
                tempHash = hashFile(key)
                #increment checked file count
                checkedFiles = checkedFiles + 1
                #check to see if $tempHash differs from baseline hash for file
                if tempHash == data[key].rstrip('\n'):
                    print colored("[+]File: " + key + " integrity is confirmed.", 'green')
                else:
                    print colored("[!]File: " + key + " has been comprimised!", 'red')
        print "Number of files checked: " + str(checkedFiles)
    
if __name__ == '__main__':
    main()