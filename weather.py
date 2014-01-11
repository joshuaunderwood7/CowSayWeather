import urllib2                                                                     
import commands                                                                    
import os                                                                          
from sys import argv                                                               
from xml.dom.minidom import parseString                                            
                                                                                   
def getTemp(url):                                                                  
    weatherFile = urllib2.urlopen(url)                                             
    data = weatherFile.read()                                                      
    dom = parseString(data)                                                        
                                                                                   
    city   = dom.getElementsByTagName('location')[0].toxml()                       
    city   = city.replace('<location>','').replace('</location>','')               
    temp_f = dom.getElementsByTagName('temp_f')[0].toxml()                         
    temp_f = temp_f.replace('<temp_f>','').replace('</temp_f>','')                 
                                                                                   
    return "The temperature in " + city  + \                                       
                     " is " + temp_f + "F"                                         
                                                                                   
outputString = ["Hello "+ os.environ['USER'] + "."]                                
if len(argv) > 2:                                                                  
    outputString = ["Hello "+ argv[2] + "."]                                       
                                                                                   
#Get the weather string                                                            
url = "http://w1.weather.gov/xml/current_obs/display.php?stid="                    
if len(argv) > 1:                                                                  
    url += argv[1]                                                                 
else:                                                                              
    url += "KAPA"                                                                  
outputString.append(getTemp(url))                                                  
                                                                                   
#get fortune                                                                       
(code, OutPut) = commands.getstatusoutput("fortune")                            
if code == 0 : outputString.append(OutPut)                                                        
                                                                                   
finalOutputString  = ""                                                            
for s in outputString:                                                             
    s = s.replace("'",'`').replace('\t',' ').replace('\n',' ').replace('@',' ').replace('\r',' ')
    finalOutputString += s + " "                                                   
                                                                                   
os.system("cowsay " + repr(finalOutputString)[1:])                                 
  
