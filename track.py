from library import argparser as parse
args = {}

try:
	args = parse.parse_args()
	if args['sheet'][-4:] == '.xls' :
		QuerySheet = open(args['sheet'],'w')
		myString = "I have passed valid excel sheet as argument"
		QuerySheet.write(myString)	
	else:
		print("passed excel format is not correct, creating default sheet")
		QuerySheet = open(args['user']+'.xls','w')
		myString = "I am learning python \n "
		QuerySheet.write(myString)			
except BaseException as e:
	pass
	# print(e)
else:
	pass
finally:
	print (args)

