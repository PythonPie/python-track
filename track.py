from library import argparser as parse
from library import xmlreader as XmlReader
args = {}
OutputSheet = None
try:
	args = parse.parse_args()
	
	InputXml = args['xml']
	if InputXml[-4:] == '.xml':
		XmlReader.processXmlData(InputXml)
	else :
		print('Kindly provide valid xml file as input\n')
	InputSheet = args['sheet']
	if InputSheet[-4:] == '.xls' :
		OutputSheet = open(InputSheet,'w')
	else:
		OutputSheet = open(InputSheet+'.xls','w')
except BaseException as exception:
	if args['sheet'] is None :
		print("No Valid excel sheet is passed, the default output sheet will be created with user name.\n")
		OutputSheet = open(args['user']+'.xls','w')
	if args['xml'] is None :
		print("xml file is not mandatory, however the essential input should be provided via command line \n")	
	pass
	# print(exception)
else:
	pass
finally:
	myData = "I think I got the solution for the issue I was having\n"
	OutputSheet.write(myData)
	OutputSheet.close()
	print (args)

