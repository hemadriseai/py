#!/usr/local/bin/python3.9
import re,os

filee='/nas/nas_v1/PDK/tsmc_downloads/24012024/PRTF_Innovus_16nm_001_Cad_V17_1a/PR_tech/Cadence/LefHeader/Standard/HVH/PRTF_Innovus_N16_9M_2Xa1Xd3Xe2Z_UTRDL_9T_PODE.17_1a.tlef'

fileid=open(filee)
fcontent=fileid.read()
fileid.close()
r=open('tlefinfo.csv','w')
r.write("layer,type,direction,mask,pitch,offset,minwidth,maxwidth,width,area,minenclosedarea\n")
layers=re.findall('^LAYER\s+(\w+)\s*\n',fcontent,re.M)
print(layers)
for layer in layers:
	data=re.findall(f'^LAYER\s+{layer}\s*\n.*?^END\s+{layer}',fcontent,re.S|re.M)[0]
	ltype=re.findall('\s*TYPE\s+(\S+)',data)[0]
	if ltype.lower() == 'routing':
		try:mask=re.findall('^\s*MASK\s+(\S+)',data,re.M)[0]
		except:mask=''
		try:direction=re.findall('^\s*DIRECTION\s+(\S+)',data,re.M)[0]
		except:direction=''
		try:pitch=re.findall('^\s*PITCH\s+(.*);',data,re.M)[0]
		except:pitch=''
		try:offset=re.findall('^\s*OFFSET\s+(.*);',data,re.M)[0]
		except:offset=''
		try:minwidth=re.findall('^\s*MINWIDTH\s+(\S+)',data,re.M)[0]
		except:minwidth=''
		try:maxwidth=re.findall('^\s*MAXWIDTH\s+(\S+)',data,re.M)[0]
		except:maxwidth=''
		try:width=re.findall('^\s*WIDTH\s+(\S+)',data,re.M)[0]
		except:width=''
		try:area=re.findall('^\s*AREA\s+(\S+)',data,re.M)[0]
		except:area=''
		try:minenclosedarea=re.findall('^\s*MINENCLOSEDAREA\s+(\S+)',data,re.M)[0]
		except:minenclosedarea=''
		r.write(f'{layer},{ltype},{direction},{mask},{pitch},{offset},{minwidth},{maxwidth},{width},{area},{minenclosedarea}\n')

r.close()
