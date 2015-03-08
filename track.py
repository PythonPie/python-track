from library import argparser as parse
from library import xmlreader as XmlReader
args = {}

try:
	args = parse.parse_args()
	OutputSheet = None
	XmlData = {}
	User = args['user']
	Password = args['password']
	Query = args['query']
	Sheet = args['sheet']
	SyncKey = args['sync_key']
except BaseException as exception:
	print(exception)
	pass
else:
	XmlFile = args['xml']	
	if XmlFile is not None and XmlFile[-4:] == '.xml':
		XmlData = XmlReader.processXmlData(XmlFile)
		if User is None :
			args['user'] = XmlData['user']
		if Password is None :
			args['password'] = XmlData['password']
		if Query is None :
			args['query'] = XmlData['query']
		if Sheet is None :
			args['sheet'] = XmlData['file']
		if SyncKey is None :
			args['sync_key'] = XmlData['sync-key']
	else :
		print('Please provide the essential inputs either via command line or via valid xml file')
	pass
finally:
	if Sheet is None or Sheet[-4:] != '.xls':
		print("No Valid excel sheet is passed, the default output sheet will be created with user name.\n")
		Sheet = args['user']+'.xls'
		args['sheet'] = Sheet
	OutputSheet = open(Sheet,'w')
	myData = "I think I got the solution for the issue I was having\n"
	OutputSheet.write(myData)
	OutputSheet.close()
	print (args)

