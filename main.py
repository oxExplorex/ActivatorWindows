import ctypes
import sys
import os

os.system("title Activator win10, win11 I lolz.guru I Рыжик I t.me/notcarrottop I v2")

def activate_win10(key):
    print("Installing the key...")
    os.system(f'slmgr.vbs -ipk {key}')
    print("Key is saved!\nSet up redirect activation...")
    os.system('slmgr /skms kms.03k.org')
    print("Saved!")
    print("Set up automatic reactivation...")
    os.system('slmgr /ato')
    print("Finished!\nPress any key for exit.")

def activate_win11():
    pass

def logo():
    os.system("cls")
    print("Лучше запускать .EXE файл от имени Администратора с самого начала!")
    print("Если у вас не получается активировать win, то переключитесь на основного пользователя")
    print("По любым предложениям писать в тг или на форум\n")
    print("tg: t.me/notcarrottop")
    print("lolz: https://lolz.guru/members/375940/")
    print("subject: https://lolz.guru/threads/4065365/\n\n")

def exits():
    os.system("pause")
    exit()

def do_not_understand():
    print("I don't understand")
    exits()



if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
else:
    logo()
    print("What operating system do you have?\n1) win 10\n2) win 11\n\n3) win 2019 Server")
    win = input()
    if win == "1":
        win10 = [
            ['Windows 10 Home SL build 10240', '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH'],
            ['Windows 10 Home build 10240', 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99'],
            ['Windows 10 Pro build 10240', 'VK7JG-NPHTM-C97JM-9MPGT-3V66T'],
            ['Windows 10 Enterprise build 10240', 'NPPR9-FWDCX-D2C8J-H872K-2YT43'],
            ['Windows 10 Enterprise build 10240', 'XGVPP-NMH47-7TTHJ-W3FW7-8HV2C'],
            ['Windows 10 Professional 10240', 'W269N-WFGWX-YVC9B-4J6C9-T83GX'],
            ['Windows 10 Home build 10240', 'YTMG3-N6DKC-DKB77-7M9GH-8HVX7'],
            ['Windows 10 Home SingleLanguage build 10240', 'BT79Q-G7N6G-PGBYW-4YWX6-6F4BT'],
            ['Windows 10 Home CountrySpecific build 10240', 'N2434-X9D7W-8PF6X-8DV9T-8TYMD'],
            ['Windows 10 Pro VL build 10240', 'QJNXR-7D97Q-K7WH4-RYWQ8-6MT6Y'],
            ['Windows 10 Корпоративная 2015 с долгосрочным обслуживанием N', "2F77B-TNFGY-69QQF-B8YKP-D69TJ"],
            ['Windows 10 Корпоративная 2015 с долгосрочным обслуживанием', 'WNMTR-4C88C-JK8YV-HQ7T2-76DF9'],
            ['Windows 10 для образовательных учреждений', 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2'],
            ['Windows 10 для образовательных учреждений N', '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ'],
            ['Windows 10 Профессиональная', 'W269N-WFGWX-YVC9B-4J6C9-T83GX'],
            ['Windows 10 Профессиональная N', 'MH37W-N47XK-V7XM9-C7227-GCQG9'],
            ['Windows 10 Корпоративная', 'NPPR9-FWDCX-D2C8J-H872K-2YT43'],
            ['Windows 10 Корпоративная N', 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4']
        ]
        logo()
        [print(f"{i+1}) {x[0]}") for i, x in enumerate(win10)]
        win10_input = input()
        if win10_input.isdigit() and 1 <= int(win10_input) <= len(win10):
            win10_input = int(win10_input) - 1

            activate_win10(win10[win10_input][1])
            exits()
        else:
            do_not_understand()
    elif win == "2":
        win11_name = ["Windows 11 Pro", "Windows 11 Pro N", "Windows 11 Pro for Working Stations", "Windows 11 Pro for Working Stations N",
                "Windows 11 Pro for School N", "Windows 11 Pro for School N", "Windows 11 Corporative",
                "Windows 11 Corporative N", "Windows 11 Corporative G", "Windows 11 Corporative GN"]
        win11_key = ["W269N-WFGWX-YVC9B-4J6C9-T83GX", "MH37W-N47XK-V7XM9-C7227-GCQG9", "NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J",
            "9FNHH-K3HBT-3W4TD-6383H-6XYWF", "6TP4R-GNPTD-KYYHQ-7B7DP-J447Y", "YVWGF-BXNMC-HTQYQ-CPQ99-66QFC",
            "NPPR9-FWDCX-D2C8J-H872K-2YT43", "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4", "YYVX9-NTFWV-6MDM3-9PT4T-4M68B", "44RPN-FTY23-9VTTB-MP9BX-T84FV"]
        os.system("cls")
        logo()
        [print(f"{i+1}) {x}") for i, x in enumerate(win11_name)]
        win11_input = input()
        if win11_input.isdigit() and 1 <= int(win11_input) <= len(win11_name):
            win11_input = int(win11_input) - 1

            print("Installing the key...")
            os.system(f"slmgr/ipk {win11_key[win11_input]}")
            print("Key is saved!\nSet up redirect activation...")
            os.system("slmgr /skms kms.digiboy.ir")
            print("Saved!")
            print("Set up automatic reactivation...")
            os.system("slmgr /ato")
            print("Finished!\nPress any key for exit.")
            exits()
        else:
            do_not_understand()
    elif win == "3":
        print("Installing the key...")
        os.system(f"slmgr/ipk PRN7B-TYC3H-9KH72-8QHVV-BDYMD")
        print("Key is saved!\nSet up redirect activation...")
        os.system("slmgr /skms kms.digiboy.ir")
        print("Saved!")
        print("Set up automatic reactivation...")
        os.system("slmgr /ato")
        print("Finished!\nPress any key for exit.")
    else:
        do_not_understand()
