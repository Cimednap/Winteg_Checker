#Winteg checker function file

import argparse 		                    #depenency for command line options
import datetime							#import datetime  module for prettier time outputs
import os                       		#import os module for os.walk function
import hashlib                      	#import hashlib module for those juicy hash digests
import errno		         			#import errno  module for error handling
#import system 							#import system module for handling system calls

#############################################################################################
##Function: hashFile
##Purpose: hashes file contents and returns the md5 hash digest 
##Returns: string
#############################################################################################
def hashFile(fname):

	#Declares $F variable, filename passed to function
	F = fname
	
	#hash the file passed to the function
	try:
		with open( F, 'rb') as theFile:
			data = theFile.read()
			md5sum = hashlib.md5(data).hexdigest()
		return	md5sum
		
	#Error handling
	except IOError, ioex:
		print "Error Hashing File: " + F
		print 'errno:', ioex.errno
		print 'err code:', errno.errorcode[ioex.errno]
		print 'err message:', os.strerror(ioex.errno)
		
#############################################################################################
##Function: getOptions
##Purpose: Reads in command line arguments from the user and assigns them to values
##Returns: base, check, and path strings
#############################################################################################				
def getOptions():
    
    #Decalre $parser variable, creates an instance of OptionParser
    parser = argparse.ArgumentParser()

    #Add parser option for directory
    parser.add_argument("-b", dest='baseline', help='Creates baseline file, default is baseline.txt, custom file name can be passed.', nargs='?')
    parser.add_argument("-c", dest='checker', help='Runs an intregrity check on the passed baseline file', nargs='?')
    parser.add_argument("-d", dest='directory', help='The starting path of the intergrity checker, used in combination with [-b]')
    
    #Parse arguments passed and store in $args
    args = parser.parse_args()
    
    #assign arguments to their respective variables
    base = args.baseline if args.baseline is not None else 'baseline.txt'
    check = args.checker if args.checker is not None else 'empty'
    path = args.directory

    return base, check, path
    
    #TODO --> Add in a requirement so that if you specify the creation of a baseline, that you also must specify a directory

    
    
    
    
    
    
    
    
    