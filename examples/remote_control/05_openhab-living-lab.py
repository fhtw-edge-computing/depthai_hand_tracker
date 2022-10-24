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

item_tree = itemTree.itemTree
cur_idx = 0
nav_menu = itemTree.menu

prev_gesture=""

# Callbacks
def toggle_light(event):
    global cur_idx
    global prev_gesture
    event.print_line()
    new_state = "OFF"

    if prev_gesture == event.name:
        print(f"ignoring recurring gesture: {prev_gesture}=={event.name}")
        return
    #    item=item_tree[selected_room][selected_device][selected_item]
    #    cur_state=iface.get_state(item.get('name'))

    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]
    print("toggle selected_item: " + str(selected_item))
    cur_state = iface.get_state(selected_item['name'])
    state_label = cur_state
    if cur_state == "OFF":
        new_state = "ON"
        state_label = "on"
    elif cur_state == "ON":
        new_state = "OFF"
        state_label = "off"
    elif cur_state == "0":
        new_state = "100"
        state_label = "on"
    elif cur_state == "100":
        new_state = "0"
        state_label = "off"

    #    error_msg=iface.post_state(item.get('name'),state_label)
    error_msg = iface.post_state(selected_item['name'], new_state)
    print(error_msg)
    # if error_msg == "OK":
    speech_controller.say("Ok, switched " + state_label + " " + " light")
    # else:
    #    speech_controller.say("Error, switching "+state_label+" "+item.get('label'))


def change_preset(event):
    global cur_idx
    global prev_gesture
    event.print_line()
    preset = event.name

    last_idx = cur_idx

    if preset == "PRESET 1":
        cur_idx = 0
    elif preset == "PRESET 2":
        cur_idx = 1
    elif preset == "PRESET 3":
        cur_idx = 2
    #elif preset == "PRESET 4":
        #cur_idx = 3
    elif preset == "NAVIGATE":
        rotation = event.hand.rotation
        print(f'hand rotation: {event.hand.rotation}')
        if rotation < -0.20:
            cur_idx += 1
            if cur_idx == len(nav_menu): cur_idx -= 1
        elif rotation > 0.40:
            cur_idx -= 1
            if cur_idx < 0: cur_idx = 0

    #print(f'cur_idx: {cur_idx}')
    if last_idx != cur_idx:
        selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]
        print(f'selected item: {str(selected_item)}')
        speech_controller.say(selected_item['label'])

    # remember this gesture as previous
    prev_gesture=preset


def change_brightness(event):
    global cur_idx
    global prev_gesture
    event.print_line()

    rotation = event.hand.rotation
    print(f'hand rotation: {event.hand.rotation}')
    if rotation < -0.20:
        level = "+"
    elif rotation > 0.40:
        level = "-"
    else:
        level = "="

    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]

    if selected_item['type'] == 'bool':
        toggle_light(event)
    elif selected_item['type'] == 'percentage':
        brightness = iface.get_state(selected_item['name'])
        if not (brightness.isnumeric()):
            #hack for mocking percentage value in case there is not default value
            brightness=0

        if (brightness == 1 and level == "-") or (brightness == 100 and level == "+"):
            return
        if level == "+":
            new_val = str(min(100, int(brightness) + 20))
            print(f'{selected_item["name"]} = {new_val}')
            speech_controller.say(new_val)
            iface.post_state(selected_item['name'], new_val)
        elif level == "-":
            new_val = str(max(0, int(brightness) - 20))
            print(f'{selected_item["name"]} = {new_val}')
            speech_controller.say(new_val)
            iface.post_state(selected_item['name'], new_val)
        else:
            toggle_light(event)

    # remember this gesture as previous
    prev_gesture=event.name


config = {

    # 'tracker': {'args': {'body_pre_focusing': 'higher'}},

    # 'renderer' : {'enable': True, 'args':{'output':'toggle_light.mp4'}},
    'renderer': {'enable': True},

    'pose_actions': [
        #{'name': 'ON_OFF', 'pose': 'ANY', 'callback': 'toggle_light',"first_trigger_delay":0.3},
        {'name': 'PRESET 1', 'pose': 'ONE', 'callback': 'change_preset', "first_trigger_delay": 0.3},
        {'name': 'PRESET 2', 'pose': ['TWO'], 'callback': 'change_preset', "first_trigger_delay": 0.3},
        {'name': 'PRESET 3', 'pose': 'THREE', 'callback': 'change_preset', "first_trigger_delay": 0.3},
        #{'name': 'PRESET 4', 'pose': ['FOUR'], 'callback': 'change_preset', "first_trigger_delay": 0.3},
        {'name': 'NAVIGATE', 'pose': ['FIVE', 'FOUR'], 'callback': 'change_preset',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 3, },
        {'name': 'BRIGHTNESS', 'pose': 'FIST', 'callback': 'change_brightness',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 3, },
    ]
}

HandController(config).loop()
