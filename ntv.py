#!/usr/bin/env python
from os import system as s
import json

player = "mpv"
with open("n_list.json") as l:
    ip_tv = json.load(l)
jml_channel = (len(ip_tv["tv"]))
channel = []
url = []
for i in range(0, len(ip_tv["tv"])):
    list_channel = ip_tv["tv"][i]["channel"]
    list_url = ip_tv["tv"][i]["url"]
    channel.append(list_channel)
    url.append(list_url)

try:
    while True:
        s("clear")
        print(f"""
███╗   ██╗   ████████╗██╗   ██╗
████╗  ██║   ╚══██╔══╝██║   ██║
██╔██╗ ██║█████╗██║   ██║   ██║
██║╚██╗██║╚════╝██║   ╚██╗ ██╔╝
██║ ╚████║      ██║    ╚████╔╝
╚═╝  ╚═══╝      ╚═╝     ╚═══╝  By Nestero
Streaming TV menggunakan IPTV.
	""")
        print("List Channel :")
        for i, key in enumerate(channel):
            if (i + 1) % 3:
                print(i, "=>", '{:15}'.format(key), end='\t')
            else:
                print(i, "=>", key, end='\n')
        p_tv = int(input(f"\nPilih Channel 0 - {jml_channel-1} > "))

        c_tv = url[p_tv]
        t_tv = channel[p_tv]

        if player == "mpv":
            s(f"mpv --fs --title='{t_tv}' {c_tv}")
        else:
            s(f"{player} {c_tv}")
except KeyboardInterrupt:
    print("^")
