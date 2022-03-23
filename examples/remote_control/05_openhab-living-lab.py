#!/usr/bin/env python3

README = """
Switching on/off an IP bulb (brand Yeelight) with the FIST or OK pose
One color preset among 4 can be selected with ONE, TWO, THREE or FOUR pose
The brightness can be changed by rotating an open hand (FIVE)

"""

print(README)

from time import time
from HandController import HandController
import iface
from SpeechController import SpeechController
import itemTree

# For the audio feedback:
speech_controller = SpeechController()

item_tree=itemTree.itemTree
selected_room="kitchen"
selected_device="light"
selected_item="Kueche1_KNX_Licht_Schalten"

# Callbacks
def toggle_light(event):
    event.print_line()
    new_state="OFF"

#    item=item_tree[selected_room][selected_device][selected_item]

#    cur_state=iface.get_state(item.get('name'))
    cur_state=iface.get_state(selected_item)
    state_label=cur_state
    if cur_state == "OFF":
        new_state="ON"
        state_label="on"
    else:
        new_state="OFF"
        state_label="off"

#    error_msg=iface.post_state(item.get('name'),state_label)
    error_msg = iface.post_state(selected_item, new_state)
    print(error_msg)
    #if error_msg == "OK":
    speech_controller.say("Ok, switched "+state_label+" "+" light")
    #else:
    #    speech_controller.say("Error, switching "+state_label+" "+item.get('label'))

def change_preset(event):
    event.print_line()
    preset = event.name

    global selected_item
    if preset == "PRESET 1":
        speech_controller.say("Changed to kitchen light")
        selected_item = "Kueche1_KNX_Licht_Schalten"
    elif preset == "PRESET 2":
        speech_controller.say("Changed to living room lights")
        selected_item="WZ_LichtDimmer"
#    elif preset == "PRESET 3":
#        speech_controller.say("Changed to kitchen light")
#        selected_item = "Kueche1_KNX_Licht_Schalten"
#    elif preset == "PRESET 4":
#        speech_controller.say("Changed to kitchen light")
#       selected_item = "Kueche1_KNX_Licht_Schalten"

def change_brightness(event):
    event.print_line()
    rotation = event.hand.rotation
    if rotation < -0.2:
        level = "+"
    elif rotation > 0.4:
        level = "-"
    else:
        return  

    brightness = iface.get_state(selected_item)
    if not(brightness.isnumeric()):
        return

    if (brightness == 1 and level == "-") or (brightness == 100 and level == "+"):
        return
    if level == "+":
        new_val=str(min(100, int(brightness) + 20))
        speech_controller.say(new_val)
        iface.post_state(selected_item,new_val)
    else:
        new_val=str(max(0, int(brightness) - 20))
        speech_controller.say(new_val)
        iface.post_state(selected_item,new_val)

config = {

    # 'tracker': {'args': {'body_pre_focusing': 'higher'}},

    #'renderer' : {'enable': True, 'args':{'output':'toggle_light.mp4'}},
    'renderer': {'enable': True},

    'pose_actions' : [
        {'name': 'ON_OFF', 'pose': 'FIST', 'callback': 'toggle_light',"first_trigger_delay":0.3},
        {'name': 'PRESET 1', 'pose':'ONE', 'callback': 'change_preset',"first_trigger_delay":0.3},
        {'name': 'PRESET 2', 'pose':'TWO', 'callback': 'change_preset',"first_trigger_delay":0.3},
        {'name': 'PRESET 3', 'pose':'THREE', 'callback': 'change_preset',"first_trigger_delay":0.3},
        {'name': 'PRESET 4', 'pose':'FOUR', 'callback': 'change_preset',"first_trigger_delay":0.3},
        {'name': 'BRIGHTNESS', 'pose': 'FIVE', 'callback': 'change_brightness',
        "trigger":"periodic", "first_trigger_delay":0.3, "next_trigger_delay":1.5, },
    ]
}

HandController(config).loop()