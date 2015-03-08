from xml.etree.ElementTree import parse as elemTree

def processXmlData(XmlFile) :
	xmlData = {}
	try:
		readXmlData = elemTree(source = XmlFile)
		xmlData['file'] = readXmlData.findtext('file')
		xmlData['user'] = readXmlData.findtext('user')
		xmlData['password'] = readXmlData.findtext('password')
		xmlData['query'] = readXmlData.findtext('query')
		for dateDetails in readXmlData.findall('date-columns'):
			for dateChild in dateDetails:
				xmlData[dateChild.text] = dateChild.text
		xmlData['sync-key'] = readXmlData.findtext('sync-key')
	except BaseException as XmlException:
		print("xml parse error")
		print(XmlException)
	else:
		pass
	finally :
		XmlDictionary = xmlData
		return XmlDictionary
	
	