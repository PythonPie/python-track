from library import argparser as parse
from library import xmlreader as XmlReader
args = {}

try:
	args = parse.parse_args()
	OutputSheet = None
	XmlData = {}
	Command = args['command']
	User = args['user']
	Password = args['password']
	Query = args['query']
	Sheet = args['sheet']
	SyncKey = args['sync_key']
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
	# sheet is an optional parameter, if not specified will create a default sheet.
	if Sheet is None :
		print("No Valid excel sheet is passed, the default output sheet will be created with query name.\n")
		args['sheet'] = args['query']+'.xls'
		Sheet = args['sheet']
	for key,value in args.items():
		if value is None and key is not 'xml':
			raise IOError('Please provide the essential inputs either via command line or via valid xml file')
except BaseException as exception:
	# print('deadbeef')
	print(exception)
	pass
else:
	pass
finally:
	OutputSheet = open(Sheet,'w')
	myData = "I think I got the solution for the issue I was having\n"
	OutputSheet.write(myData)
	OutputSheet.close()
	print (args)

