---
title: What's New in Driver Development for Windows 11, Version 26H1
description: This section describes new features for driver development in Windows 11, version 26H1.
ms.date: 07/22/2026
ms.topic: whats-new
---

# <a name="top"></a>What's new in driver development for Windows 11, version 26H1

This section describes new features and updates for driver development in Windows 11, version 26H1. To target this version of Windows, use [Windows Driver Kit (WDK) 10.0.28000.2526](./download-the-wdk.md) (released July 23, 2026).

## Visual Studio 2026 Support

Developer can now use [Visual Studio 2026](https://visualstudio.microsoft.com/downloads/) to develop drivers with the latest WDK.

## Specific Silicon

26H1 includes platform changes to support specific silicon. Use only if you need these changes. For details see Announcing Windows 11 Insider Preview Build 28000.

## Network drivers

* This Wdk changes enables Ihvs to build drivers for the WiFiCx driver model, that will enable the device to connect to networks advertising Wpa3 compatibility mode security.
* The WiFiCx driver tlv parser version is bumped up to 2.0.14, and capabilities are added to enable both the OS and the driver to use Wpa3 compatibility mode security when connecting to such networks.
* Removed legacy WDI datapath definitions from WiFiCx header.

## Storage drivers

The SDBUS/SDSTOR driver stack now supports SD Ultra Capacity (SDUC) cards for systems that use the SDBUS driver with native SD host controllers. The WDK includes the related SD bus interface updates in ntddsd.h to enable SDUC operations for cards over 2 TB and up to 128 TB.

## Kernel

### d3dkmddi.h

Added kernel header definitions for the GPU Process Debug Blob Collection feature.

## Related articles

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 25H2](driver-changes-for-windows-11-version-25h2.md)
- [Driver development changes for Windows 11, version 24H2](driver-changes-for-windows-11-version-24h2.md)
- [Driver development changes for Windows 11, version 23H2](driver-changes-for-windows-11-version-23h2.md)
- [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)

[Back to Top](#top)
