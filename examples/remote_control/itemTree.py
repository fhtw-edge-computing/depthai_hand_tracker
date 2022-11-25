menu = [["kitchen", "light", "item1"],
        ["kitchen", "light", "item2"],
        ["kitchen", "light", "item3"],
        ["kitchen", "blind", "blind1"],
        ["kitchen", "blind", "blind2"],
        ["livingroom", "light", "item1"],
        ["livingroom", "light", "item2"],
        ["livingroom", "blind", "blind1"],
        ]

menu2 = [
    ["kitchen", "light"],
    ["kitchen", "blind"],
    ["livingroom", "light"],
    ["livingroom", "blind"],
    ["bedroom", "light"],
    ["seminarroom", "light"],
    ["seminarroom", "blind"],
]

menu3 = [["kitchen", "light", "item1"],
         ["kitchen", "light", "item2"],
         ["seminarroom", "light"]]

itemList = [
    [{'name': 'Kueche1_KNX_Licht_Schalten',
      'type': 'bool',  # ON or OFF
      'label': 'Lights dinner table',
      'tags': ['kitchen', 'lights']}],
    [{'name': 'Kuche_Jalousie1',
      'type': 'percentage',
      'label': 'Blinds kitchen',
      'tags': ['kitchen', 'blinds']}]
]

jsonitemTreeGeneric = {
    'label': 'Kitchen',
    'type': 'group',
    'name': '',
    'items': [
        {
            'name': 'Kueche1_KNX_Licht_Schalten',
            'type': 'bool',  # ON or OFF
            'label': 'Lights dinner table kitchen'
        },
        {
            'name': 'Kuche_Jalousie1',
            'type': 'percentage',
            'label': 'Blinds 1 kitchen'
        }
    ]
}

itemTree = {
    'kitchen': {  # ONE
        'light': {
            'item1': {
                'name': 'Kueche1_KNX_Licht_Schalten',
                'type': 'bool',  # ON or OFF
                'label': 'One: Lights dinner table kitchen'
            },
            'item2': {
                'name': 'Kueche2_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'Two: Lights cooking table kitchen'
            },
            'item3': {
                'name': 'Kueche_LichtDimmer',
                'type': 'percentage',  # 0 - 100
                'label': 'Three: Dimmable lights kitchen'
            },
            'item4': {
                'name': 'LED_On_Off',
                'type': 'bool',
                'label': 'Lights L E D'
            },
            'item5': {
                'name': 'LED_ColorTemp',
                'type': 'percentage',
                'label': 'Lights L E D Color'
            }
        },
        'blind': {
            'blind1': {
                'name': 'Kuche_Jalousie1',
                'type': 'percentage',
                'label': 'Blinds 1 kitchen'
            },
            'blind2': {
                'name': 'Kuche_Jalousie2',
                'type': 'percentage',
                'label': 'Blinds 2 kitchen'
            }
        }
    },
    'livingroom': {  # TWO
        'light': {
            'item1': {
                'name': 'WZ_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'Lights living room'
            },
            'item2': {
                'name': 'WZ_LichtDimmer',
                'type': 'percentage',
                'label': 'Dimmable lights living room'
            }
        },
        'blind': {
            'blind1': {
                'name': 'Wohnzimmer_Jalousie1',
                'type': 'percentage',
                'label': 'Blinds 1 living room'
            },
            'blind2': {
                'name': 'Wohnzimmer_Jalousie2',
                'type': 'percentage',
                'label': 'Blinds 2 living room'
            },
            'blinds': {  # 3
                'name': 'WZ_Jalousien',
                'type': 'percentage',
                'label': 'Blinds living room'
            }
        }
    },
    'bedroom': {  # THREE
        'light': {
            'item1': {
                'name': 'Schlafzimmer_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'switch'
            },
            'item2': {
                'name': 'SZ_LichtDimmer',
                'type': 'percentage',
                'label': 'dimmer'
            }
        }
    },
    'seminarroom': {  # FOUR
        'light': {
            'item1': {
                'name': 'SR_LichtDimmer',
                'type': 'percentage',
                'label': 'dimmer'
            },
            'item2': {
                'name': 'SR_Beamerseite',
                'type': 'percentage',
                'label': 'dimmer projector side'
            },
            'item3': {
                'name': 'SR_Kuechenseite',
                'type': 'percentage',
                'label': 'dimmer kitchen side'
            }

        },
        'blind': {
            'blind1': {
                'name': 'Seminarraum_Jalousie1',
                'type': 'percentage',
                'label': 'blind 1'
            },
            'blind2': {
                'name': 'Seminarraum_Jalousie2',
                'type': 'percentage',
                'label': 'blind 2'
            }
        }
    },
    'iot_lab': {  # FIVE
        'light': {
            'item1': {
                'name': 'IoT_LichtDimmer',
                'type': 'percentage',
                'label': 'dimmer'
            },
            'item2': {
                'name': 'IoT_Beamer',
                'type': 'percentage',
                'label': 'dimmer projector'
            },
            'item3': {
                'name': 'IoT_Ecke',
                'type': 'percentage',
                'label': 'dimmer corner'
            },
            'item4': {
                'name': 'IoT_Buero',
                'type': 'percentage',
                'label': 'dimmer office'
            },
            'item5': {
                'name': 'Szenen_IoT',
                'type': 'percentage',
                'label': 'scenes'
            }
        },
        'blind': {
            'blind1': {
                'name': 'IoT_Jalousie1',
                'type': 'percentage',
                'label': 'blind 1'
            },
            'blind2': {
                'name': 'IoT_Jalousie2',
                'type': 'percentage',
                'label': 'blind 1'
            },
            'blind3': {
                'name': 'IoT_Jalousie3',
                'type': 'percentage',
                'label': 'blind 1'
            },
            'blind4': {
                'name': 'IoT_Jalousie4',
                'type': 'percentage',
                'label': 'blind 1'
            }
        }
    },
    'bathroom': {  # SIX
        'light': {
            'item1': {
                'name': 'Bad_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'switch'
            },
            'item2': {
                'name': 'Bad_Tuer',
                'type': 'bool',
                'label': 'door'
            }
        }
    },
    'bathroom2': {  # SEVEN currently just as placeholder
        'light': {
            'item1': {
                'name': 'Bad_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'switch'
            },
            'item2': {
                'name': 'Bad_Tuer',
                'type': 'bool',
                'label': 'door'
            }
        }
    },
    'bathroom3': {  # EIGHT currently just as placeholder
        'light': {
            'item1': {
                'name': 'Bad_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'switch'
            },
            'item2': {
                'name': 'Bad_Tuer',
                'type': 'bool',
                'label': 'door'
            }
        }
    },
    'bathroom4': {  # NINE currently just as placeholder
        'light': {
            'item1': {
                'name': 'Bad_KNX_Licht_Schalten',
                'type': 'bool',
                'label': 'switch'
            },
            'item2': {
                'name': 'Bad_Tuer',
                'type': 'bool',
                'label': 'door'
            }
        }
    },
    'apartment': {  # ALOHA (10)
        'light': {
            'centrallight': {
                'name': 'Wohnung_Zentral_ON_OFF',
                'type': 'bool',
                'label': 'central switch'
            }
        },
        'blind': {
            'centralblinds': {
                'name': 'Wohnung_Jalousien',
                'type': 'percentage',
                'label': 'central blinds'
            }
        },
        'temperature': {
            'centraltemp': {
                'name': 'SOLL_Wohnung_Temp',
                'type': 'percentage',
                'label': 'central temperature'
            }
        }
    }
}

# ----------------------------------------------------------------------------------------------------------------
# For testing:
if __name__ == '__main__':
    import json

    # test item tree:
    print(str(itemTree))
    # write to JSON
    with open("my.json", "w") as f:
        json.dump(itemTree, f, indent=4)  # indent for pretty print

    print(itemTree['kitchen']['light']['item1'])
    item = itemTree['kitchen']['light']['item1']
    print(item)
    print(f'name={item["name"]} type={item["type"]}')

    print("\nTest converting to list:")
    area_list = list(itemTree)  # level 1 in dict
    print(area_list)
    a_key = area_list[0]
    print(a_key)
    function_list_area1 = list(itemTree[area_list[0]])
    print(function_list_area1)

    print("\nlist von kitchen und light:")
    list_x = list(itemTree['kitchen']['light'])
    print(f'length of list_x: {len(list_x)}')
    item2_key = list_x[3]
    print(item2_key)
    item2 = itemTree['kitchen']['light'][item2_key]  # is a dict
    print(item2)
    iname = item2['name']
    print(iname)
    itype = item2['type']
    print(itype)
    # Prevent KeyError if key is not in dict:
    ilabel = item2.get('label')
    if ilabel:
        print(ilabel)
    else:
        print('no label')

    item_tree = itemTree
    cur_idx = 2
    nav_menu = menu
    selected_item=item_tree[nav_menu[cur_idx][0]][nav_menu[cur_idx][1]][nav_menu[cur_idx][2]]
    print("toggle selected_item: "+str(selected_item))
    print("toggle selected_item: " + selected_item['label'])



