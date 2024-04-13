---
title: Hello World Installation File
description: Hello World installation file
ms.date: 06/23/2023
---

# Hello World installation file

A minidriver requires a setup information (INF) file to be installed. An INF file is a text file containing all of the information needed to install the device.

For more information about INF files, see [INF Files for WIA Devices](inf-files-for-wia-devices.md) and [Creating an INF File](../install/overview-of-inf-files.md).

The *hellowld.inf* file should contain the following:

```inf
; HELLOWLD.INF  -- Hello World WIA Minidriver setup file
; Copyright (c) 2002-2003 Hello World Company
; Manufacturer:  Hello World Company

[Version]
Signature=$WINDOWS NT$
Class=Image
ClassGUID={6bdd1fc6-810f-11d0-bec7-08002be2092f}
Provider=%Mfg%
DriverVer=06/26/2001,1.0.0.0
CatalogFile=wia.cat
PnpLockdown=1

[DestinationDirs]
DefaultDestDir=13

[Manufacturer]
%Mfg%=Models,NTamd64

[Models.NTamd64]
%WIADevice.DeviceDesc% = WIADevice.Scanner, HELLOWORLD_PNP_ID

[WIADevice.Scanner]
Include=sti.inf
Needs=STI.SerialSection
SubClass=StillImage
DeviceType=2
DeviceSubType=0x0
Capabilities=0x30
DeviceData=WIADevice.DeviceData
AddReg=WIADevice.AddReg
CopyFiles=WIADevice.CopyFiles
ICMProfiles="sRGB Color Space Profile.icm"

[WIADevice.Scanner.Services]
Include=sti.inf
Needs=STI.SerialSection.Services

[WIADevice.DeviceData]
Server=local
UI DLL=sti.dll
UI Class ID={4DB1AD10-3391-11D2-9A33-00C04FA36145}

[WIADevice.AddReg]
HKR,,HardwareConfig,1,1
HKR,,USDClass,,"{7C1E2309-A535-45b1-94B3-9A020EE600C6}"
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6},,,"Hello World WIA Minidriver"
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6}\InProcServer32,,,%13%\hellowld.dll
HKCR,CLSID\{7C1E2309-A535-45b1-94B3-9A020EE600C6}\InProcServer32,ThreadingModel,,Both

[WIADevice.CopyFiles]
hellowld.dll

[SourceDisksFiles.amd64]
hellowld.dll=1
[SourceDisksNames.amd64]
1=%Location%,,,

[Strings]
Mfg="Hello World Company"
WIADevice.DeviceDesc="Hello World WIA Minidriver"
Location="Hello World WIA Minidriver Installation Source"
```
