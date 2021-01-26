
import xml.etree.ElementTree as ET
import os.path

import limit

def ini():
	tree = ET.parse(os.path.expandvars('${HOME}/.config/eiskaltdc++/DCPlusPlus.xml'))
	root = tree.getroot()
	limit.start=int(root.find('Settings').find('TotalUpload').text)
