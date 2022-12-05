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
from SpeechController_gTTS import SpeechController
import itemTree

import chime
import time

# For the audio feedback:
speech_controller = SpeechController()

item_tree = itemTree.itemTree
cur_idx = 0
nav_menu = itemTree.menu

prev_gesture=""

#Rotation config
rot_left=0.4
rot_right=-0.2

prev_rotated=False
prev_time=time.time()

def change_preset_next(event):
    global cur_idx
    cur_idx += 1
    if cur_idx == len(nav_menu):
        cur_idx -= 1
        play_error()

    say_current_item()
    # remember this gesture as previous
    prev_gesture=event.name

def change_preset_prev(event):
    global cur_idx
    cur_idx -= 1
    if cur_idx < 0:
        cur_idx = 0
        play_error()

    say_current_item()
    # remember this gesture as previous
    prev_gesture=event.name

def current_item(event):
    say_current_item()
    # remember this gesture as previous
    prev_gesture=event.name

def change_brightness_up(event):
    global cur_idx
    global prev_gesture

    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]

    if selected_item['type'] == 'percentage':
        brightness = iface.get_state(selected_item['name'])
        print(brightness)
        if not (brightness.isnumeric()):
            #hack for mocking percentage value in case there is not default value
            brightness=0

        if brightness == 100:
            play_error()
            return

        new_val = str(min(100, int(brightness) + 20))
        print(f'{selected_item["name"]} = {new_val}')
        speech_controller.say(new_val)
        iface.post_state(selected_item['name'], new_val)

    # remember this gesture as previous
    prev_gesture=event.name

def change_brightness_down(event):
    global cur_idx
    global prev_gesture

    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]

    if selected_item['type'] == 'percentage':
        brightness = iface.get_state(selected_item['name'])
        if not (brightness.isnumeric()):
            # hack for mocking percentage value in case there is not default value
            brightness = 0

        if brightness == 0:
            play_error()
            return

        new_val = str(max(0, int(brightness) - 20))
        print(f'{selected_item["name"]} = {new_val}')
        speech_controller.say(new_val)
        iface.post_state(selected_item['name'], new_val)

        # remember this gesture as previous
    prev_gesture = event.name


# Callbacks
def toggle_light(event):
    global cur_idx
    global prev_gesture
    event.print_line()
    new_state = "OFF"

#    if prev_gesture == 'FIST_ROT_RIGHT' or prev_gesture =='FIST_ROT_LEFT':
#        print(f"ignoring recurring gesture: {prev_gesture}, {event.name}")
#        return
    #    item=item_tree[selected_room][selected_device][selected_item]
    #    cur_state=iface.get_state(item.get('name'))

    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]
    print("toggle selected_item: " + str(selected_item))

    cur_state = iface.get_state(selected_item['name'])
    state_label = cur_state

    if selected_item['type'] == 'bool':
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
        speech_controller.say("Ok, switched " + state_label)
    elif selected_item['type'] == 'percentage':
        speech_controller.say("Current value " + state_label)


def change_preset(event):
    global cur_idx
    global prev_gesture
    event.print_line()
    preset = event.name

    global prev_time
    now=time.time()
    time_diff=(float)(now-prev_time)
    print(f'diff: {time_diff}')

    start_change_preset(event)

    if prev_gesture==event.name and time_diff < 2.5:
        print(f'ignoring diff: {time_diff}')
        return

    prev_time=now
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
        if rotation < rot_right:
            cur_idx += 1
            if cur_idx == len(nav_menu):
                cur_idx -= 1
                play_error()

        elif rotation > rot_left:
            cur_idx -= 1
            if cur_idx < 0:
                cur_idx = 0
                play_error()

    #print(f'cur_idx: {cur_idx}')
    if last_idx != cur_idx:
        say_current_item()

    # remember this gesture as previous
    prev_gesture=preset


def say_current_item():
    selected_item = item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]
    print(f'selected item: {str(selected_item)}')
    speech_controller.say(selected_item['label'])

def change_brightness(event):
    global cur_idx
    global prev_gesture
    #event.print_line()

    rotation = event.hand.rotation
    print(f'hand rotation: {event.hand.rotation}')
    if rotation < rot_right:
        level = "+"
    elif rotation > rot_left:
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
            play_error()
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

def start_change_preset(event):
    global prev_rotated

    rotation = event.hand.rotation
    if rotation < rot_right or rotation > rot_left:
        if not prev_rotated:
            #change_preset(event)
            #say_current_item()
#            play_action_begin()
            prev_rotated=True
    elif prev_rotated==True:
        say_current_item()
        prev_rotated=False

def play_range_in_out(event=None):
    print(f"event.name: {event.name}, trigger: {event.trigger}")
    chime.theme('zelda')

    if event.trigger=="enter":
        chime.info()
    elif event.trigger=="leave":
        chime.error()

def play_action_begin(event=None):
    chime.theme('material')
    chime.info()

def play_error(event=None):
    chime.theme('zelda')
    chime.warning()

config = {

    # 'tracker': {'args': {'body_pre_focusing': 'higher'}},

    # 'renderer' : {'enable': True, 'args':{'output':'toggle_light.mp4'}},
    'renderer': {'enable': True},

    'pose_actions': [
        {'name': 'IN_and_OUT_OF_RANGE', 'pose': 'ALL', 'callback': 'play_range_in_out',"first_trigger_delay":0.2, "trigger": "enter_leave","max_missing_frames": 5},
        {'name': 'PRESET 1', 'pose': 'ONE', 'callback': 'change_preset', "first_trigger_delay": 0.3},
        {'name': 'PRESET 2', 'pose': ['TWO'], 'callback': 'change_preset', "first_trigger_delay": 0.3},
        {'name': 'PRESET 3', 'pose': 'THREE', 'callback': 'change_preset', "first_trigger_delay": 0.3},
        #{'name': 'PRESET 4', 'pose': ['FOUR'], 'callback': 'change_preset', "first_trigger_delay": 0.3},
#        {'name': 'BEGIN_ACTION', 'pose': ['FIVE', 'FOUR'], 'callback': 'start_change_preset',
#         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 0.5, },
        {'name': 'NAVIGATE_current', 'pose': ['PALM_ROT_ZERO'], 'callback': 'current_item',
         "trigger": "enter", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },
        {'name': 'NAVIGATE_next', 'pose': ['PALM_ROT_RIGHT'], 'callback': 'change_preset_next',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },
        {'name': 'NAVIGATE_prev', 'pose': ['PALM_ROT_LEFT'], 'callback': 'change_preset_prev',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },
        {'name': 'BRIGHTNESS_toggle', 'pose': 'FIST_ROT_ZERO', 'callback': 'toggle_light',
         "trigger": "enter", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },
        {'name': 'BRIGHTNESS_up', 'pose': 'FIST_ROT_RIGHT', 'callback': 'change_brightness_up',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },
        {'name': 'BRIGHTNESS_down', 'pose': 'FIST_ROT_LEFT', 'callback': 'change_brightness_down',
         "trigger": "periodic", "first_trigger_delay": 0.2, "next_trigger_delay": 2.6, },

    ]
}

speech_controller.say("Use your palm to navigate the menu. Rotate it to the right to scroll down and to the left to scroll up. Use your fist to switch on or off.")
HandController(config).loop()
