import os, re
import os.path
import urllib.request

my_path = os.path.abspath(os.path.dirname(__file__))

#directory_in_str = '../pdf/AIME/'
#directory_in_str = '../pdf/AMC/AMC_8/'
#directory_in_str = '../pdf/AMC/AMC_10/'
#directory_in_str = '../pdf/AMC/AMC_12/'
#directory_in_str = '../pdf/AMO/'
directory_in_str = '../pdf/JMO/'

path = os.path.join(my_path, directory_in_str)
# directory = os.fsencode(directory_in_str)
os.chdir(path)
prefix = 'https://artofproblemsolving.com/downloads/printable_post_collections/'

for file in os.listdir(path):
	filename = os.fsdecode(file)
	if filename.endswith(".htm"): 
		# print(os.path.join(path, filename))
		# get print index number from filename
		index = filename.split('_', 1)[0]
		file = filename.split('_', 1)[1]
		#print(index[1:])
		#print(prefix + index[1:])
		urllib.request.urlretrieve(prefix + index[1:], path + file.rsplit('_', 1)[0] + '.pdf')
		'''
		log = open(os.path.join(path, filename))
		for line in log:
			print(line)
		'''
		continue
	else:
		continue