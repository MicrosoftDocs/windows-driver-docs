---
title: Component Firmware Update (CPU) Sample HIDCFU.INF file
description: Component Firmware Update (CPU) Sample HIDCFU.INF file
ms.date: 07/23/2020
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# Component Firmware Update (CPU) Sample HIDCFU.INF file

Sample driver installation file for CFU virtual HID device firmware update.

## Sample HIDCFU.INF file

```INF
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; File:               CfuVirtualHidDeviceFwUpdate.inx
;
; Description:        Driver installation file for Cfu Virtual Hid Device firmware update.
;
; Copyright (C) Microsoft Corporation.  All Rights Reserved.
; Licensed under the MIT license.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

[Version]
Signature="$Windows NT$"
Class=Firmware
ClassGuid={f2e7dd72-6468-4e36-b6f1-6488f42c1b52}
Provider=%ManufacturerName%
CatalogFile=CfuVirtualHidDeviceFwUpdate.cat
DriverVer = 12/16/2019,11.42.16.703
PnPLockDown=1

[SourceDisksNames]
1= %DiskName%

[DestinationDirs]
CfuVirtualHidDeviceFwUpdate.CopyFiles=13

[Manufacturer]
%ManufacturerName%=Standard,NTamd64

[Standard.NTamd64]
%CfuVirtualHidDeviceFwUpdate.DeviceDesc%=CfuVirtualHidDeviceFwUpdate, HID\VID_045E&UP:FA00_U:00F5 ; HardwareID for VirtualHidDevice MCU

[CfuVirtualHidDeviceFwUpdate.NT]
Include            = HidCfu.inf
Needs              = HidCfu.NT
CopyFiles          = CfuVirtualHidDeviceFwUpdate.CopyFiles

[CfuVirtualHidDeviceFwUpdate.NT.Wdf]
Include            = HidCfu.inf
Needs              = HidCfu.NT.Wdf

[CfuVirtualHidDeviceFwUpdate.NT.HW]
AddReg = CfuVirtualHidDeviceFwUpdate_HWAddReg

[CfuVirtualHidDeviceFwUpdate_HWAddReg]
HKR,,FriendlyName,,%FwUpdateFriendlyName%
HKR,,Alignment,0x00010001, 1                       ; (No Alignment)
HKR,,OfferInputValueCapabilityUsageRangeMinimum,0x00010001,0x1A
HKR,,OfferOutputValueCapabilityUsageRangeMinimum,0x00010001, 0x1E
HKR,,PayloadInputValueCapabilityUsageRangeMinimum,0x00010001,0x26
HKR,,PayloadOutputValueCapabilityUsageRangeMinimum,0x00010001,0x31
HKR,,VersionsFeatureValueCapabilityUsageRangeMinimum,0x00010001, 0x42

; Specify the location of the firmware offer and payload file in the registry.
; The files are kept in driver store. When deployed, %13% would be expanded to the actual path
; in driver store.
;
; You can change subkey name under CFU (e.g. "CfuVirtualHidDevice_MCU"), and specify your own offer
; (e.g. "CfuVirtualHidDevice_MCU.offer.bin") and payload (e.g "CfuVirtualHidDevice_MCU.payload.bin") file name.
;
HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_MCU,Offer,   0x00000000, %13%\CfuVirtualHidDevice_MCU.offer.bin
HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_MCU,Payload, 0x00000000, %13%\CfuVirtualHidDevice_MCU.payload.bin
HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_Audio,Offer,   0x00000000, %13%\CfuVirtualHidDevice_Audio.offer.bin
HKR,A410A898-8132-4246-AC1A-30F1E98BB0A4\CfuVirtualHidDevice_Audio,Payload, 0x00000000, %13%\CfuVirtualHidDevice_Audio.payload.bin

[SourceDisksFiles]
CfuVirtualHidDevice_MCU.offer.bin=1
CfuVirtualHidDevice_MCU.payload.bin=1
CfuVirtualHidDevice_Audio.offer.bin=1
CfuVirtualHidDevice_Audio.payload.bin=1

[CfuVirtualHidDeviceFwUpdate.CopyFiles]
CfuVirtualHidDevice_MCU.offer.bin
CfuVirtualHidDevice_MCU.payload.bin
CfuVirtualHidDevice_Audio.offer.bin
CfuVirtualHidDevice_Audio.payload.bin

[CfuVirtualHidDeviceFwUpdate.NT.Services]
Include            = HidCfu.inf
Needs              = HidCfu.NT.Services

; =================== Generic ==================================

[Strings]
ManufacturerName="Surface"
CfuVirtualHidDeviceFwUpdate.DeviceDesc = "CfuVirtualHidDevice Firmware Update"
DiskName = "CfuVirtualHidDevice Firmware Update Installation Disk"
FwUpdateFriendlyName= "CfuVirtualHidDevice Firmware Update"
```
