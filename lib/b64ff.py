#-*- coding: utf-8-*-
#17.05.23 by ur0n2
#b64ff.py: base64 for file
#pass the text file and binary file test.

import base64
import sys

def encode_base64(finput):
	encode_base64_data = base64.b64encode(finput)
	return encode_base64_data 


def decode_base64(finput):
	decode_base64_data = base64.b64decode(finput)
	return decode_base64_data 


def print_usage():
	print("Usage: Base64 encode to file: b64ff.py e in.b64 o out.b64") 
	print("       Base64 decode to file: b64ff.py d in.b64 o out.b64")
	print("       Can be omitted arguments are 'o' and 'out.b64'\n")


def print_data(data):
	wanna = raw_input("Do u wanna print data? ('y' or anything typing for quit)")

	if wanna == "y":
		print(data)
	else: 
		return #exit() is except


if __name__ == '__main__':	
	try:
		#Encode
		if sys.argv[1] == "e":
			with open(sys.argv[2], "rb") as finput:
				data = finput.read()
				if len(sys.argv) == 3: #Omitted arguments are 'o' and 'out.b64
					data = encode_base64(data)
					with open("out.b64", "wb") as foutput:
						foutput.write(data)
					print_data(data)
				elif sys.argv[3] == "o":	
					data = encode_base64(data)
					with open(sys.argv[4], "wb") as foutput:
						foutput.write(data)
					print_data(data)
				else:
					print_usage()
		#Decode
		elif sys.argv[1] == "d":
			with open(sys.argv[2], "rb") as finput:
				data = finput.read()
				if len(sys.argv) == 3: #Omitted arguments are 'o' and 'out.b64
					data = decode_base64(data)
					with open("out.b64", "wb") as foutput:
						foutput.write(data)
					print_data(data)
				elif sys.argv[3] == "o":
					data = decode_base64(data)
					with open(sys.argv[4], "wb") as foutput:
						foutput.write(data)
					print_data(data)
				else:
					print_usage()
		else: 
			print_usage()
	except:
		if len(sys.argv) == 1:
			print_usage()
		else:
			print("Error is occurred") #maybe almost error related to file descriptor.
