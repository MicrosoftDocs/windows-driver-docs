---
title: Stream Class Registry Values
description: Stream Class Registry Values
ms.assetid: a6800f53-4d55-4a28-839b-47f0cecc17bf
keywords:
- Stream.sys class driver WDK Windows 2000 Kernel , registry
- streaming minidrivers WDK Windows 2000 Kernel , registry
- minidrivers WDK Windows 2000 Kernel Streaming , registry
- registry WDK streaming minidriver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stream Class Registry Values





To install a minidriver under *Stream.sys*, the vendor must supply a device-specific INF file that complies with [generic INF file requirements](https://msdn.microsoft.com/library/windows/hardware/ff547433). In this file, minidrivers running under stream class can set special registry values in the device-specific [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) section. These registry entries serve as binary indicators: set them to hexadecimal value 01 to enable the capability.

Stream class minidrivers can use the following registry values:

<a href="" id="pageoutwhenunopened"></a>**PageOutWhenUnopened**  
This registry entry indicates that the device driver should be paged out when unopened. If the device cannot be paged out when unopened, this feature is turned off for the whole driver.

<a href="" id="powerdownwhenunopened"></a>**PowerDownWhenUnopened**  
This registry entry indicates that the device should be powered down when unopened.

<a href="" id="driverusesswenumtoload"></a>**DriverUsesSWEnumToLoad**  
Software-only device drivers should use this registry string to inform stream class that the device driver requires different *AddRef/DecRef* handling than a hardware device driver.

The following flags were supported on Windows 9x but are obsolete in NT-based operating systems:

<a href="" id="dontsuspendifstreamsarerunning"></a>**DontSuspendIfStreamsAreRunning**  
This registry variable is obsolete in Windows 2000 and later NT-based operating systems. (As of this release, DirectShow listens to power queries and puts all streams into pause when it receives a low-power query.) An application can still inform the system that it is in use by calling **SetThreadExecutionState**. This routine is described in the Microsoft Windows SDK documentation. Alternatively, a driver can use [**PoSetSystemState**](https://msdn.microsoft.com/library/windows/hardware/ff559768).

<a href="" id="oktohibernate"></a>**OkToHibernate**  
This registry string is only valid for drivers running on Windows 98. It is not used in NT-based operating systems.

The following is an extract from the *Usbintel.inf* file that demonstrates how to set these registry values. This file, part of the UsbIntel sample, is available in the Driver Development Kit (DDK) and Windows Driver Kit (WDK) for Windows XP through Windows 7 (Build 7600).

```INF
[Intel.USBDCam]
Include= ks.inf, kscaptur.inf
Needs= KS.Registration,KSCAPTUR.Registration
AddReg= Intel.USBDCam.AddReg
CopyFiles=Intel.USBDCam.Files.Ext
; WIA
SubClass=StillImage
DeviceType=3
DeviceSubType=0x1
Capabilities=0x00000031
DeviceData=Intel.USBDCam.DeviceData
ICMProfiles="sRGB Color Space Profile.icm"
[Intel.USBDCam.AddReg]
HKR,,DevLoader,,*ntkern
HKR,,NTMPDriver,,usbintel.sys
HKR,,PageOutWhenUnopened,3,01
; WIA
HKR,,HardwareConfig,1,1
HKR,,USDClass,,"{0527d1d0-88c2-11d2-82c7-00c04f8ec183}"
```

 

 




