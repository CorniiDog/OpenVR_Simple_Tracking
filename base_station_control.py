from os.path import exists
import asyncio
import time
from bleak import BleakScanner, BleakClient, BleakError
import argparse

#############################################################
# Code written by MissingNO123, modified by Connor White
# https://github.com/MissingNO123/HTC_BS_Control/tree/main
# 5/30/2023
#############################################################
PowerState = True


saved_addrs = []

v1_Power_UUID = "0000cb00-0000-1000-8000-00805f9b34fb"
v1_Power_Char = "0000cb01-0000-1000-8000-00805f9b34fb"

CMD_ON  = b"\x12\x00\x00\x28\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
CMD_OFF = b"\x12\x01\x00\x28\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"

v2_Power_UUID = "00001523-1212-efde-1523-785feabcd124"
v2_Power_Char = "00001525-1212-efde-1523-785feabcd124"

CMD_ON_V2 = b"\x01"
CMD_OFF_V2 = b"\x00"

async def powerState(bs, value):
    try:
        async with BleakClient(bs) as client:
            print("~%s~" % bs)
            print("Connecting...")
            while client.is_connected is False:
                time.sleep(0.05)
            print("Connected!")
            print("Powering %s..." % ("ON " if PowerState is True else "OFF"))
            try:
                cmd = CMD_ON_V2 if value else CMD_OFF_V2
                p = await client.read_gatt_char(v2_Power_Char) #check if V2 BS Power Characteristic is available
                p = await client.write_gatt_char(v2_Power_Char, cmd)
            except BleakError: #if V2 Power Characteristic is not available that means it"s probably a V1 BS
                try:
                    cmd = CMD_ON if value else CMD_OFF
                    p = await client.read_gatt_char(v1_Power_Char)
                    p = await client.write_gatt_char(v1_Power_Char, cmd)
                except BleakError:
                    print("Cannot send command to %s, it is probably NOT a base station", bs) # In case some random device with the same name as a BS gets caught by the scan
            print("Disconnecting...")
            await client.disconnect()
    except BleakError as e:
        print("Unable to connect to Base Station: \n{}".format(e))

async def main():
    basestations = []
    if len(saved_addrs) != 0:
        basestations = saved_addrs
    else:
        print("Scanning...")
        devices = await BleakScanner.discover()
        if len(devices) == 0:
            print("No devices found.")
            quit()
        for d in devices:
            if d.name is not None and (d.name.startswith("HTC BS ") or d.name.startswith("LHB-")):
                print("Found Base Station: %s" % d.name)
                basestations.append(d)
        if len(basestations) == 0:
            print("No base stations found.")
            quit()
        print("~~~")

    for bs in basestations:
        await powerState(bs, PowerState)
        print("~~~")
    print("Done!")

def turn_base_stations_on():
    global PowerState
    PowerState = True
    asyncio.run(main())

def turn_base_stations_off():
    global PowerState
    PowerState = False
    asyncio.run(main())

if __name__ == "__main__":
    asyncio.run(main())