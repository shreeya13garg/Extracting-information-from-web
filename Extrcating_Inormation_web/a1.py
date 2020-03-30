#Shreeya Garg
#2018415
#section-B
#group-8
import urllib.request
import datetime
# function to get weather response
def weather_response(location, API_key):
	x = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s"%(location,API_key))
	json_str = x.read().decode()
	return json_str
	# write your code 

# function to check for valid response 
def has_error(location,json_str):
	# write your code 
	c = json_str.find("name")
	w = json_str.find("coord")
	f = json_str[c+7:w-3]
	h = f.lower()
	len1 = len(location)
	len2 = len(f)
	if len1>len2:
		s = location.lower().split()
		h = s[0]+s[1]
	elif len1<len2:
		k = f.lower().split()
		h = k[0]+k[1]	
		
	if h == location:
		return False
	else :
		return True

# function to get attributes on nth day
def get_temperature (json_str, t="12:00:00", n=0):
	currdate=str(datetime.date.today())
	slc=int(currdate[8:10])
	slc += n
	nowdate=currdate[0:8]+str(slc)+currdate[10:19]
	r = nowdate+" "+t
	o = json_str.find(r)
	q = json_str.rfind('"temp"',0,o)
	e = json_str.find('"temp_min"',q)
	v = float(json_str[q+7:e-1])
	return v

def get_humidity(json_str,t, n=0):
	currdate=str(datetime.date.today())
	slc=int(currdate[8:10])
	slc += n
	nowdate=currdate[0:8]+str(slc)+currdate[10:19]
	r = nowdate+" "+t
	o = json_str.find(r)
	q = json_str.rfind('"humidity"',0,o)
	e = json_str.find('"temp_kf"',q)
	v = float(json_str[q+11:e-1])
	return v

def get_pressure(json_str,t, n=0):
	currdate=str(datetime.date.today())
	slc=int(currdate[8:10])
	slc += n
	nowdate=currdate[0:8]+str(slc)+currdate[10:19]
	r = nowdate+" "+t
	o = json_str.find(r)
	q = json_str.rfind('"pressure"',0,o)
	e = json_str.find('"sea_level"',q)
	v = float(json_str[q+11:e-1])
	return v 

def get_wind(json_str,t, n=0):
	currdate=str(datetime.date.today())
	slc=int(currdate[8:10])
	slc += n
	nowdate=currdate[0:8]+str(slc)+currdate[10:19]
	r = nowdate+" "+t
	o = json_str.find(r)
	q = json_str.rfind('"speed"',0,o)
	e = json_str.find('"deg"',q)
	v = float(json_str[q+8:e-1])
	return v

def get_sealevel(json_str,t, n=0):
	currdate=str(datetime.date.today())
	slc=int(currdate[8:10])
	slc += n
	nowdate=currdate[0:8]+str(slc)+currdate[10:19]
	r = nowdate+" "+t
	o = json_str.find(r)
	q = json_str.rfind('"sea_level"',0,o)
	e = json_str.find('"grnd_level"',q)
	v = float(json_str[q+12:e-1])
	return v



"""json_str = weather_response("Delhi","92188b47948dc3249713eb02f74c0264")
print(has_error("delhi",json_str))
print(get_temperature(json_str,"12:00:00",2))
print(get_humidity(json_str,"12:00:00",2))
print(get_pressure(json_str,"12:00:00",2))
print(get_wind(json_str,"12:00:00",2))
print(get_sealevel(json_str,"12:00:00",2))"""


