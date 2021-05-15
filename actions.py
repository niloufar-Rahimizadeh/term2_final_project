import states
import config

def entrance():
    code = input("enter a ID code: ")
    if code =="425":
        config.conf['out']['lock'] = False
        states.salon()
    else:
        config.conf['out']['lock'] = True
        states.maindoor()

def out():
    states.maindoor()

def salon():
    states.salon()

def room():
    states.room() 

def kitchen():
    states.kitchen()


acts = {
    'entrance': entrance,
    'out': out,
    'salon': salon,
    'room': room,
    'kitchen': kitchen
}