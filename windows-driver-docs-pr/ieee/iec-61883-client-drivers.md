---
title: IEC-61883 Client Drivers
description: IEC-61883 Client Drivers
ms.assetid: 2a3f62d0-c1f2-4978-8f89-3ed800d697f4
keywords:
- IEC-61883 client drivers WDK IEEE 1394 bus
- 61883 WDK IEEE 1394 bus
- IEEE 1394 WDK buses , IEC-61883 client drivers
- 1394 WDK buses , IEC-61883 client drivers
- protocols WDK buses
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IEC-61883 Client Drivers





IEC-61883 is a standard communications and control interface used by IEEE 1394 audio and video devices. In Windows 98 SE, Windows 2000 and earlier operating systems, 61883 functionality was implemented as part of the Microsoft Digital Video (MSDV) camcorder driver, *msdv.sys*. In Windows Me, Windows XP, and later operating systems, 61883 functionality has been moved to a separate driver dedicated to 61883 support. Vendor-supplied IEC-61883 client drivers send requests to the system-supplied [IEC-61883 Protocol Driver](https://msdn.microsoft.com/library/windows/hardware/ff537191) (*61883.sys*) to communicate with their devices.

IEC-61883 specifications define the protocol by which numerous consumer electronic audio and video devices can interconnect. These specifications include definitions for general data format, data flow, and connection schemes for audiovisual information. The IEC-61883 protocol driver supports devices that conform to the following ratified IEC-61883 specifications:

-   IEC-61883-1: General

-   IEC-61883-2: SD-VCR Data Transmission

-   IEC-61883-3: HD-VCR Data Transmission

-   IEC-61883-4: MPEG2-TS Data Transmission

-   IEC-61883-5: SDL-DVCR Data Transmission

-   IEC-61883-6: Audio and Music Data Transmission Protocol

This section includes:

[IEC-61883 Protocol Driver](https://msdn.microsoft.com/library/windows/hardware/ff537191)
[IEC-61883 Protocol Driver in a Client Driver Stack](https://msdn.microsoft.com/library/windows/hardware/ff537193)
 

 




