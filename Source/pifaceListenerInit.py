##listener init
import pifacedigitalio
import PifaceControllerMain 


def listening():
    
    pifacedigital = pifacedigitalio.PiFaceDigital()

    listener = pifacedigitalio.InputEventListener(chip=pifacedigital)
    for i in range(4):
        listener.register(i, pifacedigitalio.IODIR_ON, PifaceControllerMain.switch_pressed)
        listener.register(i, pifacedigitalio.IODIR_OFF, PifaceControllerMain.switch_unpressed)
    listener.activate()
    print("Started listening")
        
def stopListening():
    listening.listener.deactivate()
    print("Stopped listening")

print("ready to start listening")