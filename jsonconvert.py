from xml.dom import minidom

def getjson(dom):
	attributes_present = False
	jsonstr = "{"
	try:
		if dom.hasAttributes():
			attributes_present = True
			for attribute in dom._get_attributes().items():
				jsonstr += "\"" + attribute[0] + "\":\"" + attribute[1] + "\","
	except:
		pass
	
	if not dom.hasChildNodes():
		if attributes_present:
			jsonstr += "\"value\":\"" + dom.nodeValue + "\"}"
		else:
			jsonstr = "\"" + dom.nodeValue + "\""
		return jsonstr
	
	if dom.childNodes.length == 1:
		element = dom.childNodes[0]
		if element.nodeName == "#text":
			if attributes_present:
				jsonstr += "\"value\":\"" + element.nodeValue + "\"}"
			else:
				jsonstr = "\"" + element.nodeValue + "\""
		else:
			jsonstr += "\"" + element.nodeName + "\":" + getjson(element) + "}"
	else:
		jsonstr += "\"children\":["
		for element in dom.childNodes:
			lastnode = (element == dom.childNodes[-1])
			if lastnode:
				lastnodestr = ""
			else:
				lastnodestr = ","
			
			if element.nodeName == "#text":
				if not (element.nodeValue == "\n" or element.nodeValue == ""):
					jsonstr += "\"value\":\"" + element.nodeValue + "\"" + lastnodestr
				else:
					if lastnode:
						jsonstr = jsonstr[:-1]
			else:
				jsonstr += "{\"" + element.nodeName + "\":" + getjson(element) + "}" + lastnodestr
		jsonstr += "]}"
	return jsonstr