import re
import zip

def asd():
    print "ASD"
    pass

def file_len():
	pass

def main():
	fname = 'user_list.txt'
	with open(fname, 'r') as f: #count the user_count
 		for i, l in enumerate(f):
			pass
		user_count = i + 1	
	
	f = open(fname, 'r')
	
	for user in xrange(user_count):
		a = f.readline().strip('\n')
		b,c =zip(a.split('='))
		print b,c
	f.close()


if __name__ == '__main__':
    main()
    asd()
    