---
title: IEC-61883 Client Drivers
author: windows-driver-content
description: IEC-61883 Client Drivers
MS-HAID:
- '61883\_dg\_34b0864e-4f68-48b1-8c61-aa45d8258cbc.xml'
- 'IEEE.iec\_61883\_client\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2a3f62d0-c1f2-4978-8f89-3ed800d697f4
keywords: ["IEC-61883 client drivers WDK IEEE 1394 bus", "61883 WDK IEEE 1394 bus", "IEEE 1394 WDK buses , IEC-61883 client drivers", "1394 WDK buses , IEC-61883 client drivers", "protocols WDK buses"]
---

# IEC-61883 Client Drivers


## <a href="" id="ddk-iec-61883-client-drivers-kg"></a>


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
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BIEEE\buses%5D:%20IEC-61883%20Client%20Drivers%20%20RELEASE:%20%287/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


