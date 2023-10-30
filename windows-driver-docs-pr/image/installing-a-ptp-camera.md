---
title: Installing a PTP Camera
description: Installing a PTP Camera
ms.date: 05/08/2023
---

# Installing a PTP Camera

If your camera supports PTP, all you need to do is plug in your device to get it installed as a WIA device. The Microsoft PTP WIA Minidriver will do the rest.

If you have additions or extensions that you want to add to your PTP camera, you need to create an INF file.

The INF file includes sections from *sti.inf*. This allows Microsoft to make future updates to *sti.inf* when needed, without affecting your INF file.

The USB Device Working Group has assigned class ID 0x06 for still image cameras. In future Windows releases, Microsoft will ship an INF file that loads the PTP driver for this class ID as a *compatible ID* match. This means that vendors can still load a custom driver by shipping an INF file that contains the *hardware ID*. The Windows installer places a higher priority on matching the hardware ID than on matching the class ID. If the INF file with the hardware ID isn't shipped in Windows, the vendor driver isn't loaded automatically. However, the Autorun program for the CD can call [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa) to easily update the vendor driver.

Example INF file for a PTP camera:

```inf
; PTPCAMERA.INF  -- PTP Camera setup file
; Copyright (c) 2002 PTP Camera Company
; Manufacturer:  PTP Camera Company

[Version]
Signature=$WINDOWS NT$
Class=Image
ClassGUID={6bdd1fc6-810f-11d0-bec7-08002be2092f}
Provider=%Mfg%
DriverVer=06/26/2001,1.0
CatalogFile=wia.cat
PnpLockdown=1

[Manufacturer]
%Mfg%=Models,NTamd64

[Models.NTamd64]
%PTPCamera100.DeviceDesc%=PTP100, USB\VID_000&PID_0100

[PTP100]
Include=sti.inf
Needs=STI.PTPUSBSection

AddReg=PTP100.AddReg
DeviceData=PTP100.DeviceData
SubClass=StillImage
DeviceType=2
Capabilities=0x35
Events=PTP100.Events
ICMProfiles="sRGB Color Space Profile.icm"

[PTP100.Services]
Include=sti.inf
Needs=STI.USBSection.Services

[PTP100.DeviceData]
Model=PTP
QueryDeviceForName=1,1
Server=local
UI DLL=sti.dll
UI Class ID={4DB1AD10-3391-11D2-9A33-00C04FA36145}

[PTP100.Events]
Connected=%PTP.Connected%,{A28BBADE-64B6-11d2-A231-00C04FA31809},*
Disconnected=%PTP.Disconnected%,{143E4E83-6497-11d2-A231-00C04FA31809},*

[PTP100.AddReg]

[Strings]
Mfg="PTP Camera Company"
PTPCamera100.DeviceDesc="PTP Camera Model 100"
PTP.Connected="PTP Camera Connected"
PTP.Disconnected="PTP Camera Disconnected"
```
