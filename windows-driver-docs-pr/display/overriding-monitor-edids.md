---
title: Overriding Monitor EDIDs with an INF
description: With an INF file you can override the Extended Display Identification Data (EDID) of any monitor.
ms.assetid: AA7DC29B-54D5-461A-8252-600D84F0F581
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overriding Monitor EDIDs with an INF


With an INF file you can override the Extended Display Identification Data (EDID) of any monitor. A sample INF file, Monsamp.inf, that shows how to do this was provided with the Windows Driver Kit (WDK) through Windows 7 (WDK version 7600). Monsamp.inf is reproduced here.

For info on how to use and modify Monsamp.inf, see [Monitor INF File Sections](monitor-inf-file-sections.md).

## <span id="Approaches_to_correcting_EDIDs"></span><span id="approaches_to_correcting_edids"></span><span id="APPROACHES_TO_CORRECTING_EDIDS"></span>Approaches to correcting EDIDs


All monitors, analog or digital, must support EDID, which contains info such as the monitor identifier, manufacturer data, hardware identifier, timing info, and so on. This data is stored in the monitor’s EEPROM in a format that is specified by the Video Electronics Standards Association (VESA).

Monitors provide the EDID to Microsoft Windows components, display drivers, and some user-mode applications. For example, during initialization the monitor driver queries the Windows Display Driver Model (WDDM) driver for its brightness query interface and device driver interface (DDI) support, which is in the EDID. Incorrect or invalid EDID info on the monitor’s EEPROM can therefore lead to problems such as setting incorrect display modes.

There are two approaches to correcting EDIDs:

-   The standard solution is to have the customer send the monitor back to the manufacturer, who reflashes the EEPROM with the correct EDID and returns the monitor to the customer.
-   A better solution, described here, is for the manufacturer to implement an INF file that contains the correct EDID info, and have the customer download it to the computer that's connected to the monitor. Windows extracts the updated EDID info from the INF and provides it to components instead of the info from the EEPROM EDID, effectively overriding the EEPROM EDID.

In addition to replacing the EDID info as described here, a vendor can provide an override for the monitor name and the preferred display resolution. Such an override is frequently made available to customers through Windows Update or digital media in the shipping box. Such an override receives higher precedence than the EDID override mentioned here. Guidelines for achieving this can be found in [Monitor INF File Sections](monitor-inf-file-sections.md).

## <span id="EDID_format"></span><span id="edid_format"></span><span id="EDID_FORMAT"></span>EDID format


EDID data is formatted as one or more 128-byte blocks:

-   EDID version 1.0 through 1.2 consists of a single block of data, per the VESA specification.
-   With EDID version 1.3 or enhanced EDID (E-EDID), manufacturers can specify one or more extension blocks in addition to the primary block.

Each block is numbered, starting with 0 for the initial block. To update EDID info, the manufacturer’s INF specifies the number of the block to be updated and provides 128 bytes of EDID data to replace the original block. The monitor driver obtains the updated data for the corrected blocks from the registry and uses the EEPROM data for the remaining blocks.

## <span id="Updating_an_EDID"></span><span id="updating_an_edid"></span><span id="UPDATING_AN_EDID"></span>Updating an EDID


To update an EDID by using an INF:

1.  The monitor manufacturer implements an INF that contains the updated EDID info and downloads the file to the user’s computer. This can be done through Windows Update or by shipping a CD with the monitor.
2.  The monitor class installer extracts the updated EDID info from the INF and stores the info as values under this registry key:

    ```registry
    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\DISPLAY
    ```

    Each EDID override is stored under a separate key. For example:

    ```registry
    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\DISPLAY\DELA007\
          5&1608c50f&0&10000090&01&20\Device Parameters\EDID_Override
    ```

3.  The monitor driver checks the registry during initialization and uses any EDID info that's stored there instead of the corresponding info on EEPROM. EDID info that has been added to the registry always takes precedence over EEPROM EDID info.
4.  Windows components and user-mode apps use the updated EDID info.

## <span id="Overriding_an_EDID_with_an_INF"></span><span id="overriding_an_edid_with_an_inf"></span><span id="OVERRIDING_AN_EDID_WITH_AN_INF"></span>Overriding an EDID with an INF


To override an EDID, include an [**AddReg directive**](https://msdn.microsoft.com/library/windows/hardware/ff546320) in the INF for each block that you want to override, in the following format:

```inf
HKR, EDID_OVERRIDE, BlockNumber, Byte 1, Byte 2, Byte 3, Byte 4,...
```

The block number is followed by 128 hexadecimal integers that contain the binary EDID data.

Manufacturers must update only those EDID blocks that are incorrect. The system obtains the remaining blocks from EEPROM. The following example shows the relevant sections of an INF that updates EDID blocks 0, 4, and 5. The monitor driver obtains blocks 1 - 3 and any extension blocks that follow block 5 from EEPROM:

```inf
[ABC.DDInstall.HW]
ABC.AddReg
...
[ABC.AddReg]
HKR, EDID_OVERRIDE, 0, 1, 00, FF, ..., 3B
HKR, EDID_OVERRIDE, 4, 1, 1F, 3E, ..., 4E
HKR, EDID_OVERRIDE, 5, 1, 24, 5C, ..., 2D
...
```

For more info on INFs in general, and **AddReg** and **DDInstall** in particular, see [Creating an INF File](https://msdn.microsoft.com/library/windows/hardware/ff538378).

```inf
; monsamp.INF
;
; Copyright (c) Microsoft Corporation.  All rights reserved.
;
; This is a generic INF file for overriding EDIDs 
; of any monitors, starting with Windows Vista.
;

[Version]
signature="$WINDOWS NT$"
Class=Monitor
ClassGuid={4D36E96E-E325-11CE-BFC1-08002BE10318}
Provider="MS_EDID_OVERRIDE"
DriverVer=04/18/2006, 1.0.0.0

; Be sure to add the directive below with the proper catalog file after 
; WHQL certification.
;CatalogFile=Sample.cat


[DestinationDirs]
DefaultDestDir=23

[SourceDisksNames]
1=%SourceDisksNames%

; Enable the following section to copy a monitor profile.
[SourceDisksFiles]
;profile1.icm=1

[Manufacturer]
%MS_EDID_OVERRIDE%=MS_EDID_OVERRIDE,NTx86,NTamd64

; Modify the hardware ID (MON1234) to match that of the monitor being used.
[MS_EDID_OVERRIDE.NTx86]
%MS_EDID_OVERRIDE-1%=MS_EDID_OVERRIDE-1.Install, MONITOR\MON1234

; Modify the hardware ID (MON1234) to match that of the monitor being used.
[MS_EDID_OVERRIDE.NTamd64]
%MS_EDID_OVERRIDE-1%=MS_EDID_OVERRIDE-1.Install.NTamd64, MONITOR\MON1234

[MS_EDID_OVERRIDE-1.Install.NTx86]
DelReg=DEL_CURRENT_REG
AddReg=MS_EDID_OVERRIDE-1.AddReg, 1024, 1280, DPMS
CopyFiles=MS_EDID_OVERRIDE-1.CopyFiles

[MS_EDID_OVERRIDE-1.Install.NTamd64]
DelReg=DEL_CURRENT_REG
AddReg=MS_EDID_OVERRIDE-1.AddReg, 1024, 1280, DPMS
CopyFiles=MS_EDID_OVERRIDE-1.CopyFiles

[MS_EDID_OVERRIDE-1.Install.NTx86.HW]
AddReg=MS_EDID_OVERRIDE-1_AddReg

[MS_EDID_OVERRIDE-1.Install.NTamd64.HW]
AddReg=MS_EDID_OVERRIDE-1_AddReg

[MS_EDID_OVERRIDE-1_AddReg]
HKR,EDID_OVERRIDE,"0",0x01,0x00,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x00,0x35,\
0xEE,0x34,0x12,0x01,0x00,0x00,0x00,0x0A,0x0E,0x01,0x03,0x68,0x22,0x1B,\
0x78,0xEA,0xAE,0xA5,0xA6,0x54,0x4C,0x99,0x26,0x14,0x50,0x54,0xA5,0x4B,\
0x00,0x71,0x4F,0x81,0x80,0xA9,0x40,0x01,0x01,0x01,0x01,0x01,0x01,0x01,\
0x01,0x01,0x01,0x30,0x2A,0x00,0x98,0x51,0x00,0x2A,0x40,0x30,0x70,0x13,\
0x00,0x52,0x0E,0x11,0x00,0x00,0x1E,0x00,0x00,0x00,0xFF,0x00,0x41,0x42,\
0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x30,0x31,0x0A,0x00,0x00,0x00,\
0xFC,0x00,0x4D,0x53,0x20,0x31,0x32,0x33,0x34,0x0A,0x0A,0x0A,0x0A,0x0A,\
0x0A,0x00,0x00,0x00,0xFD,0x00,0x38,0x4C,0x1F,0x50,0x12,0x00,0x0A,0x20,\
0x20,0x20,0x20,0x20,0x20,0x00,0xDB

[DEL_CURRENT_REG]
HKR,MODES
HKR,,MaxResolution
HKR,,DPMS
HKR,,ICMProfile

; Pre-defined AddReg sections. These can be used for default settings 
; when a given standard resolution is used.

[1024]
HKR,,MaxResolution,,"1024,768"
[1280]
HKR,,MaxResolution,,"1280,1024"

[DPMS]
HKR,,DPMS,,1

[MS_EDID_OVERRIDE-1.AddReg]
HKR,"MODES\1024,768",Mode1,,"31.0-94.0,55.0-160.0,+,+"
HKR,"MODES\1280,1024",Mode1,,"31.0-94.0,55.0-160.0,+,+"

; Enable the following section to copy a monitor profile.
[MS_EDID_OVERRIDE-1.CopyFiles]
;PROFILE1.ICM

[Strings]
MonitorClassName="Monitor"
SourceDisksNames="MS_EDID_OVERRIDE Monitor EDID Override Installation Disk"

MS_EDID_OVERRIDE="MS_EDID_OVERRIDE"
MS_EDID_OVERRIDE-1="MS EDID Override"
```

 

 





