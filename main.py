import requests
import os
import json

from tqdm import tqdm

import PSFirmManager.ps4_db as ps4_db
import PSFirmManager.ps3_db as ps3_db

config_file = open("PSFirmManager/config.json", "r")
config_json = json.loads(s=config_file.read())
config_file.close()

author = config_json["Author"]
version = config_json["Version"]
supported_consoles = config_json["Consoles"]

if os.name.upper() == "NT": clear = "cls"
else: clear = "clear"

while True:
    os.system(clear)

    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")
    print(" (1) PS5 Firmware manager [ COMING SOON ]")
    print(" (2) PS4 Firmware manager")
    print(" (3) PSVita Firmware manager [ COMING SOON ]")
    print(" (4) PS3 Firmware manager")
    print(" (5) PSP Firmware manager [ COMING SOON ]")
    print(" (0) Exit PSFirmManager\n")

    cmd = input("> ")
    try: cmd = int(cmd)
    except ValueError: continue

    if cmd == 0:
        os.system(clear)
        break

    if cmd == 2:
        while True:
            os.system(clear)

            print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")
            print(" (1) Download official PS4 firmwares")
            print(" (2) Download official PS4 beta firmwares")
            print(" (3) Download PS4 Syscon firmwares")
            print(" (4) Prepare USB for offline firmware update [ COMING SOON ]")
            print(" (0) Return to main menu\n")

            cmd = input("> ")
            try: cmd = int(cmd)
            except ValueError: continue

            if cmd == 0:
                os.system(clear)
                break
            
            if cmd == 1:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps4_db.official_firmwares:
                        print(" (" + str(i) + ")\tDownload PS4 Firmware " + firm_version + " # MD5: " + ps4_db.official_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps4_db.official_firmwares.keys())[cmd]
                    firmware = list(ps4_db.official_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS4UPDATE.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS4UPDATE.PUB", "wb") as file, tqdm(
                        desc="PS4UPDATE.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                    
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break
            
            if cmd == 2:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps4_db.official_beta_firmwares:
                        print(" (" + str(i) + ")\tDownload PS4 Beta Firmware " + firm_version + " # MD5: " + ps4_db.official_beta_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps4_db.official_beta_firmwares.keys())[cmd]
                    firmware = list(ps4_db.official_beta_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS4UPDATE.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS4UPDATE.PUB", "wb") as file, tqdm(
                        desc="PS4UPDATE.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                    
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break
            
            if cmd == 3:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps4_db.syscon_firmwares:
                        print(" (" + str(i) + ")\tDownload PS4 Syscon Firmware " + firm_version + " # MD5: " + ps4_db.syscon_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps4_db.syscon_firmwares.keys())[cmd]
                    firmware = list(ps4_db.syscon_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]
                    out_file = download_url.split("/")[-1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print("\n[*] Downloading " + out_file + f" {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open(out_file, "wb") as file, tqdm(
                        desc=out_file,
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                    
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break
    
    if cmd == 4:
        while True:
            os.system(clear)

            print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")
            print(" (1) Download official PS3 firmwares")
            print(" (2) Download PS3 Hybrid firmwares (HFW)")
            print(" (3) Download PS3 Custom firmwares (CFW) [ COMING SOON ]")
            print(" (4) Download PS3 Dev firmwares [ COMING SOON ]")
            print(" (5) Download PS3 Syscon firmwares")
            print(" (6) Download PS3 Arcade (GEX) firmwares")
            print(" (7) Download PS3 AV-Tool firmwares")
            print(" (8) Prepare USB for offline firmware update [ COMING SOON ]")
            print(" (0) Return to main menu\n")

            cmd = input("> ")
            try: cmd = int(cmd)
            except ValueError: continue

            if cmd == 0:
                os.system(clear)
                break

            if cmd == 1:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps3_db.official_firmwares:
                        print(" (" + str(i) + ")\tDownload PS3 Firmware " + firm_version + " # MD5: " + ps3_db.official_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps3_db.official_firmwares.keys())[cmd]
                    firmware = list(ps3_db.official_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS3UPDAT.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS3UPDAT.PUB", "wb") as file, tqdm(
                        desc="PS3UPDAT.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                    
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break
        
            if cmd == 2:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps3_db.hybrid_firmwares:
                        print(" (" + str(i) + ")\tDownload PS3 Hybrid Firmware " + firm_version + " # MD5: " + ps3_db.hybrid_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps3_db.hybrid_firmwares.keys())[cmd]
                    firmware = list(ps3_db.hybrid_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS3UPDAT.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS3UPDAT.PUB", "wb") as file, tqdm(
                        desc="PS3UPDAT.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                        
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break
    
            if cmd == 5:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps3_db.syscon_firmwares:
                        print(" (" + str(i) + ")\tDownload PS3 Syscon Firmware " + firm_version + " # MD5: " + ps3_db.syscon_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps3_db.syscon_firmwares.keys())[cmd]
                    firmware = list(ps3_db.syscon_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]
                    out_file = download_url.split("/")[-1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print("\n[*] Downloading " + out_file + f" {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open(out_file, "wb") as file, tqdm(
                        desc=out_file,
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                    
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break

            if cmd == 6:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps3_db.arcade_firmwares:
                        print(" (" + str(i) + ")\tDownload PS3 Arcade (GEX) Firmware " + firm_version + " # MD5: " + ps3_db.arcade_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps3_db.arcade_firmwares.keys())[cmd]
                    firmware = list(ps3_db.arcade_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS3UPDAT.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS3UPDAT.PUB", "wb") as file, tqdm(
                        desc="PS3UPDAT.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                        
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break

            if cmd == 7:
                while True:
                    os.system(clear)

                    print("PSFirmManager v" + version + " by https://github.com/SpectrTech A.K.A. " + author + "\n")

                    i = 1
                    for firm_version in ps3_db.av_tool_firmwares:
                        print(" (" + str(i) + ")\tDownload PS3 AV-Tool Firmware " + firm_version + " # MD5: " + ps3_db.av_tool_firmwares[firm_version][0])
                        i += 1
                    print(" (0)\tReturn to main menu\n")

                    cmd = input("> ")
                    try: cmd = int(cmd)
                    except ValueError: continue

                    if cmd == 0:
                        os.system(clear)
                        break

                    cmd -= 1
                    firmware = list(ps3_db.av_tool_firmwares.keys())[cmd]
                    firmware = list(ps3_db.av_tool_firmwares.values())[cmd]

                    md5_checksum = firmware[0]
                    download_url = firmware[1]

                    download_stream = requests.get(download_url, stream=True)
                    download_stream.raise_for_status()

                    total_size = int(download_stream.headers.get("content-length", 0))
                    print(f"\n[*] Downloading PS3UPDAT.PUB {total_size / (1024 * 1024):.2f} MB | MD5: " + md5_checksum)

                    with open("PS3UPDAT.PUB", "wb") as file, tqdm(
                        desc="PS3UPDAT.PUB",
                        total=total_size,
                        unit="iB",
                        unit_scale=True,
                        unit_divisor=1024,
                    ) as bar:
                        for chunk in download_stream.iter_content(chunk_size=1024):
                            file.write(chunk)
                            bar.update(len(chunk))
                        
                    input("Press [ENTER] to continue.")

                    os.system(clear)
                    break