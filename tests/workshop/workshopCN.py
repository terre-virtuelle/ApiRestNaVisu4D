from tkinter import *
from PIL import Image, ImageTk
import requests
from datetime import datetime, timezone

#Variables globales
request=""
scenarioName = ""
questionId="0"
responseId="0"
startId="0"
stopId="0"
trueId="0"
falseId="0"
lat=0
lon=0

#HOST_NAME="localhost"
HOST_NAME = "93.90.200.21"
PORT = "3003"
CONTROL = "control"
EXPORT_FILE = 'export'
READ_FILE = 'read'
WRITE_FILE = 'write'
ORIGIN = "TV"

root = Tk()
root.title("Atelier Centre Nautique")
root.geometry('780x900')
root.option_add("*Font", "Aerial 12")

Label(root, text="Atelier Centre Nautique",font=('Arial',25)).pack(fill='both', expand=True)

frame1 = Frame(root) 
frame1.pack(side='left')

img = ImageTk.PhotoImage(Image.open("Logotv2020.png"))
Label(frame1, image = img).grid(column=8, row=0)

img1 = ImageTk.PhotoImage(Image.open("smaugLogo_1.png"))
Label(frame1, image = img1).grid(column=0, row=0)

#Zone de saisie de la latitude
Label(frame1, text="Latitude",font=('Arial',15),width=15).grid(column=1, row=0)
latitudeEntry = Entry(frame1, width=18)
latitudeEntry.grid(column=1, row=0, sticky=S)

#Zone de saisie de la longitude
Label(frame1, text="Longitude",font=('Arial',15),width=15).grid(column=2, row=0)
longitudeEntry = Entry(frame1, width=18)
longitudeEntry.grid(column=2, row=0, sticky=S)

def sendLatLon():
    global lat, lon
    lat = latitudeEntry.get()
    lon = longitudeEntry.get()
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    request = 'http://'+HOST_NAME+':3003/control?cmd=response&target='+questionId+'&origin='+ORIGIN+'&timestamp=' + time + '&latitude='+ lat +'&longitude=' + lon 
    print(request)
    r = requests.put(request)
    latitudeEntry.delete(0,'end')
    longitudeEntry.delete(0,'end')

sendButtonLatLon = Button(frame1 , text = "Send", command=sendLatLon,background = 'white').grid(column=3, row=0,sticky=S)






#Zone de saisie titre scenario
Label(frame1, text="Scenario name",font=('Arial',15),width=15).grid(column=0, row=1)
scenarioEntry = Entry(frame1, width=18)
scenarioEntry.grid(column=1, row=1)
def sendScenarioName():
    global scenarioName
    scenarioName=scenarioEntry.get()
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    request='http://'+HOST_NAME+':'+PORT+'/'+READ_FILE+'?cmd=scenario&origin='+ORIGIN+'&path=scenarios/'+scenarioName+'&target='+scenarioName+'.json'+'&timestamp=' + time
    print(request)
    r = requests.put(request)
    
sendButton = Button(frame1 , text = "Send", command=sendScenarioName,background = 'white').grid(column=2, row=1, sticky=W)

#Commande de sauvegarde log NMEA
#def log():
#    request = 'http://'+HOST_NAME+':3003/'+WRITE_FILE+'?cmd=log&target='+scenarioName+'&origin='+ORIGIN
#   requests.put(request)
#    print(request)

#Button(frame1 , text = "Log NMEA", command=log, background = 'white').grid(column=3, row=1, sticky=E)

#Commande de génération du pdf
def exportPdf():
    request = 'http://'+HOST_NAME+':3003/'+EXPORT_FILE+'?cmd=scenario&target='+scenarioName+'&origin='+ORIGIN
    requests.put(request)
    print(request)

Button(frame1 , text = "Export pdf   ", command=exportPdf, background = 'white').grid(column=8, row=1)


b1=Button(frame1 , text = "Question1  ", command=lambda:question("1"), background = 'white')
b1.grid(column=0, row=2)
b2=Button(frame1 , text = "Question2  ", command=lambda:question("2"), background = 'white')
b2.grid(column=0, row=3)
b3=Button(frame1 , text = "Question3  ", command=lambda:question("3"), background = 'white')
b3.grid(column=0, row=4)
b4=Button(frame1 , text = "Question4  ", command=lambda:question("4"), background = 'white')
b4.grid(column=0, row=5)
b5=Button(frame1 , text = "Question5  ", command=lambda:question("5"), background = 'white')
b5.grid(column=0, row=6)
b6=Button(frame1 , text = "Question6  ", command=lambda:question("6"), background = 'white')
b6.grid(column=0, row=7)
b7=Button(frame1 , text = "Question7  ", command=lambda:question("7"), background = 'white')
b7.grid(column=0, row=8)
b8=Button(frame1 , text = "Question8  ", command=lambda:question("8"), background = 'white')
b8.grid(column=0, row=9)
b9=Button(frame1 , text = "Question9  ", command=lambda:question("9"), background = 'white')
b9.grid(column=0, row=10)
b10=Button(frame1 , text = "Question10", command=lambda:question("10"), background = 'white')
b10.grid(column=0, row=11)
b11=Button(frame1 , text = "Question11", command=lambda:question("11"), background = 'white')
b11.grid(column=0, row=12)
b12=Button(frame1 , text = "Question12", command=lambda:question("12"), background = 'white')
b12.grid(column=0, row=13)
b13=Button(frame1 , text = "Question13", command=lambda:question("13"), background = 'white')
b13.grid(column=0, row=14)
b14=Button(frame1 , text = "Question14", command=lambda:question("14"), background = 'white')
b14.grid(column=0, row=15)
b15=Button(frame1 , text = "Question15", command=lambda:question("15"), background = 'white')
b15.grid(column=0, row=16)
b16=Button(frame1 , text = "Question16", command=lambda:question("16"), background = 'white')
b16.grid(column=0, row=17)
b17=Button(frame1 , text = "Question17", command=lambda:question("17"), background = 'white')
b17.grid(column=0, row=18)
b18=Button(frame1 , text = "Question18", command=lambda:question("18"), background = 'white')
b18.grid(column=0, row=19)
b19=Button(frame1 , text = "Question19", command=lambda:question("19"), background = 'white')
b19.grid(column=0, row=20)
b20=Button(frame1 , text = "Question20", command=lambda:question("20"), background = 'white')
b20.grid(column=0, row=21)
#Questions 
def question(x):
    global questionId 
    if x == "1":
        b1.config(background='blue')
    if x == "2":
        b2.config(background='blue')
    if x == "3":
        b3.config(background='blue')
    if x == "4":
        b4.config(background='blue')
    if x == "5":
        b5.config(background='blue')
    if x == "6":
        b6.config(background='blue')
    if x == "7":
        b7.config(background='blue')
    if x == "8":
        b8.config(background='blue')
    if x == "9":
        b9.config(background='blue')
    if x == "10":
        b10.config(background='blue')
    if x == "11":
        b11.config(background='blue')
    if x == "12":
        b12.config(background='blue')
    if x == "13":
        b13.config(background='blue')
    if x == "14":
        b14.config(background='blue')
    if x == "15":
        b15.config(background='blue')
    if x == "16":
        b16.config(background='blue')
    if x == "17":
        b17.config(background='blue')
    if x == "18":
        b18.config(background='blue')
    if x == "19":
        b19.config(background='blue')
    if x == "20":
        b20.config(background='blue')

    questionId = 'q'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':'+PORT+'/'+CONTROL+'?cmd=question&origin='+ORIGIN+'&target='+questionId+'&timestamp=' + time)



#start 
def start(x):
    global startId 
    startId = 'start'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':3003/control?cmd=start&target='+startId+'&origin='+ORIGIN+'&timestamp=' + time)

Button(frame1 , text = "Start", command=lambda:start("1"), background = 'green').grid(column=1, row=2, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("2"), background = 'green').grid(column=1, row=3, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("3"), background = 'green').grid(column=1, row=4, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("4"), background = 'green').grid(column=1, row=5, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("5"), background = 'green').grid(column=1, row=6, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("6"), background = 'green').grid(column=1, row=7, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("7"), background = 'green').grid(column=1, row=8, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("8"), background = 'green').grid(column=1, row=9, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("9"), background = 'green').grid(column=1, row=10, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("10"), background = 'green').grid(column=1, row=11, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("11"), background = 'green').grid(column=1, row=12, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("12"), background = 'green').grid(column=1, row=13, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("13"), background = 'green').grid(column=1, row=14, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("14"), background = 'green').grid(column=1, row=15, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("15"), background = 'green').grid(column=1, row=16, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("16"), background = 'green').grid(column=1, row=17, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("17"), background = 'green').grid(column=1, row=18, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("18"), background = 'green').grid(column=1, row=19, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("19"), background = 'green').grid(column=1, row=20, sticky=W)
Button(frame1 , text = "Start", command=lambda:start("20"), background = 'green').grid(column=1, row=21, sticky=W)

#stop 
def stop(x):
    global stopId 
    stopId = 'stop'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':3003/control?cmd=stop&target='+stopId+'&origin='+ORIGIN+'&timestamp=' + time)

Button(frame1 , text = "Stop", command=lambda:stop("1"), background = 'red').grid(column=1, row=2, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("2"), background = 'red').grid(column=1, row=3, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("3"), background = 'red').grid(column=1, row=4, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("4"), background = 'red').grid(column=1, row=5, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("5"), background = 'red').grid(column=1, row=6, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("6"), background = 'red').grid(column=1, row=7, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("7"), background = 'red').grid(column=1, row=8, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("8"), background = 'red').grid(column=1, row=9, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("9"), background = 'red').grid(column=1, row=10, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("10"), background = 'red').grid(column=1, row=11, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("11"), background = 'red').grid(column=1, row=12, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("12"), background = 'red').grid(column=1, row=13, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("13"), background = 'red').grid(column=1, row=14, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("14"), background = 'red').grid(column=1, row=15, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("15"), background = 'red').grid(column=1, row=16, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("16"), background = 'red').grid(column=1, row=17, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("17"), background = 'red').grid(column=1, row=18, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("18"), background = 'red').grid(column=1, row=19, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("19"), background = 'red').grid(column=1, row=20, sticky=E)
Button(frame1 , text = "Stop", command=lambda:stop("20"), background = 'red').grid(column=1, row=21, sticky=E)

#true 
def true(x):
    global trueId 
    trueId = 'true'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':3003/control?cmd=validate&target='+trueId+'&origin='+ORIGIN+'&timestamp=' + time)

Button(frame1 , text = "True", command=lambda:true("1"), background = 'green').grid(column=2, row=2, sticky=W)
Button(frame1 , text = "True", command=lambda:true("2"), background = 'green').grid(column=2, row=3, sticky=W)
Button(frame1 , text = "True", command=lambda:true("3"), background = 'green').grid(column=2, row=4, sticky=W)
Button(frame1 , text = "True", command=lambda:true("4"), background = 'green').grid(column=2, row=5, sticky=W)
Button(frame1 , text = "True", command=lambda:true("5"), background = 'green').grid(column=2, row=6, sticky=W)
Button(frame1 , text = "True", command=lambda:true("6"), background = 'green').grid(column=2, row=7, sticky=W)
Button(frame1 , text = "True", command=lambda:true("7"), background = 'green').grid(column=2, row=8, sticky=W)
Button(frame1 , text = "True", command=lambda:true("8"), background = 'green').grid(column=2, row=9, sticky=W)
Button(frame1 , text = "True", command=lambda:true("9"), background = 'green').grid(column=2, row=10, sticky=W)
Button(frame1 , text = "True", command=lambda:true("10"), background = 'green').grid(column=2, row=11, sticky=W)
Button(frame1 , text = "True", command=lambda:true("11"), background = 'green').grid(column=2, row=12, sticky=W)
Button(frame1 , text = "True", command=lambda:true("12"), background = 'green').grid(column=2, row=13, sticky=W)
Button(frame1 , text = "True", command=lambda:true("13"), background = 'green').grid(column=2, row=14, sticky=W)
Button(frame1 , text = "True", command=lambda:true("14"), background = 'green').grid(column=2, row=15, sticky=W)
Button(frame1 , text = "True", command=lambda:true("15"), background = 'green').grid(column=2, row=16, sticky=W)
Button(frame1 , text = "True", command=lambda:true("16"), background = 'green').grid(column=2, row=17, sticky=W)
Button(frame1 , text = "True", command=lambda:true("17"), background = 'green').grid(column=2, row=18, sticky=W)
Button(frame1 , text = "True", command=lambda:true("18"), background = 'green').grid(column=2, row=19, sticky=W)
Button(frame1 , text = "True", command=lambda:true("19"), background = 'green').grid(column=2, row=20, sticky=W)
Button(frame1 , text = "True", command=lambda:true("20"), background = 'green').grid(column=2, row=21, sticky=W)

#false 
def false(x):
    global falseId 
    falseId = 'false'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':3003/control?cmd=validate&target='+falseId+'&origin='+ORIGIN+'&timestamp=' + time)

Button(frame1 , text = "False", command=lambda:false("1"), background = 'red').grid(column=2, row=2, sticky=E)
Button(frame1 , text = "False", command=lambda:false("2"), background = 'red').grid(column=2, row=3, sticky=E)
Button(frame1 , text = "False", command=lambda:false("3"), background = 'red').grid(column=2, row=4, sticky=E)
Button(frame1 , text = "False", command=lambda:false("4"), background = 'red').grid(column=2, row=5, sticky=E)
Button(frame1 , text = "False", command=lambda:false("5"), background = 'red').grid(column=2, row=6, sticky=E)
Button(frame1 , text = "False", command=lambda:false("6"), background = 'red').grid(column=2, row=7, sticky=E)
Button(frame1 , text = "False", command=lambda:false("7"), background = 'red').grid(column=2, row=8, sticky=E)
Button(frame1 , text = "False", command=lambda:false("8"), background = 'red').grid(column=2, row=9, sticky=E)
Button(frame1 , text = "False", command=lambda:false("9"), background = 'red').grid(column=2, row=10, sticky=E)
Button(frame1 , text = "False", command=lambda:false("10"), background = 'red').grid(column=2, row=11, sticky=E)
Button(frame1 , text = "False", command=lambda:false("11"), background = 'red').grid(column=2, row=12, sticky=E)
Button(frame1 , text = "False", command=lambda:false("12"), background = 'red').grid(column=2, row=13, sticky=E)
Button(frame1 , text = "False", command=lambda:false("14"), background = 'red').grid(column=2, row=14, sticky=E)
Button(frame1 , text = "False", command=lambda:false("14"), background = 'red').grid(column=2, row=15, sticky=E)
Button(frame1 , text = "False", command=lambda:false("15"), background = 'red').grid(column=2, row=16, sticky=E)
Button(frame1 , text = "False", command=lambda:false("16"), background = 'red').grid(column=2, row=17, sticky=E)
Button(frame1 , text = "False", command=lambda:false("17"), background = 'red').grid(column=2, row=18, sticky=E)
Button(frame1 , text = "False", command=lambda:false("18"), background = 'red').grid(column=2, row=19, sticky=E)
Button(frame1 , text = "False", command=lambda:false("19"), background = 'red').grid(column=2, row=20, sticky=E)
Button(frame1 , text = "False", command=lambda:false("20"), background = 'red').grid(column=2, row=21, sticky=E)

#responses 
def response(x):
    global responseId 
    responseId = 'r'+x
    time = str(datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"))
    r = requests.put('http://'+HOST_NAME+':3003/control?cmd=response&target='+responseId+'&origin='+ORIGIN+'&timestamp=' + time)

Button(frame1 , text = "Response1  ", command=lambda:response("1"), background = 'white').grid(column=8, row=2)
Button(frame1 , text = "Response2  ", command=lambda:response("2"), background = 'white').grid(column=8, row=3)
Button(frame1 , text = "Response3  ", command=lambda:response("3"), background = 'white').grid(column=8, row=4)
Button(frame1 , text = "Response4  ", command=lambda:response("4"), background = 'white').grid(column=8, row=5)
Button(frame1 , text = "Response5  ", command=lambda:response("5"), background = 'white').grid(column=8, row=6)
Button(frame1 , text = "Response6  ", command=lambda:response("6"), background = 'white').grid(column=8, row=7)
Button(frame1 , text = "Response7  ", command=lambda:response("7"), background = 'white').grid(column=8, row=8)
Button(frame1 , text = "Response8  ", command=lambda:response("8"), background = 'white').grid(column=8, row=9)
Button(frame1 , text = "Response9  ", command=lambda:response("9"), background = 'white').grid(column=8, row=10)
Button(frame1 , text = "Response10", command=lambda:response("10"), background = 'white').grid(column=8, row=11)
Button(frame1 , text = "Response11", command=lambda:response("11"), background = 'white').grid(column=8, row=12)
Button(frame1 , text = "Response12", command=lambda:response("12"), background = 'white').grid(column=8, row=13)
Button(frame1 , text = "Response13", command=lambda:response("13"), background = 'white').grid(column=8, row=14)
Button(frame1 , text = "Response14", command=lambda:response("14"), background = 'white').grid(column=8, row=15)
Button(frame1 , text = "Response15", command=lambda:response("15"), background = 'white').grid(column=8, row=16)
Button(frame1 , text = "Response16", command=lambda:response("16"), background = 'white').grid(column=8, row=17)
Button(frame1 , text = "Response17", command=lambda:response("17"), background = 'white').grid(column=8, row=18)
Button(frame1 , text = "Response18", command=lambda:response("18"), background = 'white').grid(column=8, row=19)
Button(frame1 , text = "Response19", command=lambda:response("19"), background = 'white').grid(column=8, row=20)
Button(frame1 , text = "Response20", command=lambda:response("20"), background = 'white').grid(column=8, row=21)

now = datetime.now()
Label(frame1, text=now.strftime("%H:%M:%S"),width=15).grid(column=0, row=22, sticky=W)

Label(frame1, text=HOST_NAME,width=15).grid(column=1, row=22, sticky=E)
Label(frame1, text=PORT,width=10).grid(column=2, row=22, sticky=W)

#Reset
def reset():
    b1.config(background='white')
    b2.config(background='white')
    b3.config(background='white')
    b4.config(background='white')
    b5.config(background='white')
    b6.config(background='white')
    b7.config(background='white')
    b8.config(background='white')
    b9.config(background='white')
    b10.config(background='white')
    b11.config(background='white')
    b12.config(background='white')
    b13.config(background='white')
    b14.config(background='white')
    b15.config(background='white')
    b16.config(background='white')
    b17.config(background='white')
    b18.config(background='white')
    b19.config(background='white')
    b20.config(background='white')

resetButton = Button(frame1, text="Reset",command=reset, background = 'white').grid(column=2, row=22,sticky=E)

#Test sur les valeurs entrees
def test():
    print("scenarioName :",scenarioName)
    print("questionId :",questionId)
    print("responseId :",responseId)
    print("startId :", startId)
    print("stopId :",stopId)
    print("trueId :",trueId)
    print("falseId :",falseId)
    print("latitude :",lat)
    print("longitude :",lon)
testButton = Button(frame1, text="Test",command=test, background = 'white').grid(column=8, row=22,sticky=W)


#Sortie de l'appli
quitButton = Button(frame1, text="Quit",command=root.destroy, background = 'red').grid(column=8, row=22, sticky=E)

root.mainloop()
