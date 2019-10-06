from sense_hat import SenseHat
import time
Red = (255,0,0)
Green= (0,255,0)
Blue= (0,0,255)
unitColor=Red
ucCounter=0
sense=SenseHat()
unit=False
meth=False
mod=0#0 for temp, 1 for pree, 2 for hum
sense.show_message("E.S. <-<-")
time.sleep(2)
sense.show_message("Temp.")
######################
while True:
  for event in sense.stick.get_events():

    if event.direction =="down" and event.action=="pressed":#Switch Units
      if not mod==2:
        sense.clear()
        if mod==0:
          sense.show_letter("C")
        elif mod==1:
          sense.show_message("mmbar")#
        unit=True
        time.sleep(2)
    elif event.direction=="up" and event.action=="pressed":
        if not mod==2:
            sense.clear()
            if mod==0:
              sense.show_letter("F")
            elif mod==1:
              sense.show_message("mmHg")#
            unit=False
            time.sleep(2)

    elif event.direction=="left" and event.action=="pressed":#Switch Methods
      if mod==0:
        if meth==False:
          sense.clear()
          sense.show_letter("P")
          meth=True
          time.sleep(2)
        elif meth==True:
          sense.clear()
          sense.show_letter("H")
          meth=False
          time.sleep

    elif event.direction=="right" and event.action=="pressed":#Switch Methods
      if mod==0:
        sense.clear()
        sense.show_message("Pres.")
        mod=mod+1
        meth=False
        time.sleep(2)
      elif mod==1:
        sense.clear()
        sense.show_message("Huma.")
        mod=mod+1
        meth=False
        time.sleep(2)
      elif mod==2:
        sense.clear()
        sense.show_message("Temp.")
        mod=0
        meth=False
        time.sleep
    elif event.direction=="middle" and event.action=="pressed":#Switch Color of Units
      if ucCounter==0:
        ucCounter=ucCounter+1
        unitColor=Green
      elif ucCounter==1:
        ucCounter=ucCounter+1
        unitColor=Blue
      else:
        ucCounter=0
        unitColor=Red
######################Main Loop
  if mod==0:#Temp
    if meth==False:
      if unit==True:
        sense.show_message(str(int(sense.get_temperature()+0.5)))
        sense.show_message("C",text_colour=unitColor)
      else:
        sense.show_message(str(int((sense.get_temperature()*1.8+32)+0.5)))
        sense.show_message("F",text_colour=unitColor)
    else:
      if unit==True:
        sense.show_message(str(int(sense.get_temperature_from_pressure()+0.5)))
        sense.show_message("C",text_colour=unitColor)
      else:
        sense.show_message(str(int((sense.get_temperature_from_pressure()*1.8+32)+0.5)))
        sense.show_message("F",text_colour=unitColor)

  if mod==1:#Press
    if unit==True:
      sense.show_message(str(int(sense.get_pressure()+0.5)))
      sense.show_message("Mbar",text_colour=unitColor)
    else:
      sense.show_message(str(int((sense.get_pressure()*0.75)+0.5)))
      sense.show_message("mmHg",text_colour=unitColor)
  if mod==2:#Human
    sense.show_message(str(int(sense.get_humidity()+0.5)))
    sense.show_message("%",text_colour=unitColor)
