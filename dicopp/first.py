
from . import stor2
from . import nick

from os.path import isfile

a='''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<DCPlusPlus>
	<Settings>
		<Nick type="string">'''
b='''</Nick>
		<ConfigVersion type="string">2.3.0</ConfigVersion>
		<Slots type="int">3</Slots>
		<TotalDownload type="int64">0</TotalDownload>
		<TotalUpload type="int64">0</TotalUpload>
	</Settings>
	<SearchTypes>
		<SearchType Id="6">3gp;asf;asx;avi;divx;flv;mkv;mov;mp4;mpeg;mpg;ogm;pxp;qt;rm;rmvb;swf;vob;webm;wmv</SearchType>
		<SearchType Id="5">bmp;cdr;eps;gif;ico;img;jpeg;jpg;png;ps;psd;sfw;tga;tif;webp</SearchType>
		<SearchType Id="4">app;bat;cmd;com;dll;exe;jar;msi;ps1;vbs;wsf</SearchType>
		<SearchType Id="3">doc;docx;htm;html;nfo;odf;odp;ods;odt;pdf;ppt;pptx;rtf;txt;xls;xlsx;xml;xps</SearchType>
		<SearchType Id="1">ape;flac;m4a;mid;mp3;mpc;ogg;ra;wav;wma</SearchType>
		<SearchType Id="2">7z;ace;arj;bz2;gz;lha;lzh;rar;tar;z;zip</SearchType>
		<SearchType Id="7">iso;mdf;mds;nrg;vcd;bwt;ccd;cdi;pdi;cue;isz;img;vc4</SearchType>
	</SearchTypes>
	<Share />
</DCPlusPlus>'''

def ini():
	f=stor2.get_file()
	if isfile(f)==False:
		import xml.etree.ElementTree as ET
		s=a+nick.name.get_text()+b
		e=ET.fromstring(s)
		t = ET.ElementTree(element=e)
		t.write(f)
