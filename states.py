import asc
import actions


def get_input(ac_list):
    print('Actions', ac_list)
    ac = input("Select an action: ")
    while not ac_list.__contains__(ac):
        ac = input("Select an action: ")
    else:
        function = actions.acts[ac]
        function()


def maindoor():
    print(asc.door)
    get_input(['entrance'])


def salon():
    print(asc.salon)
    get_input(['out', 'room', 'kitchen', 'television'])

def room():
    print(asc.room)
    get_input(['salon', 'panel'])

def ki