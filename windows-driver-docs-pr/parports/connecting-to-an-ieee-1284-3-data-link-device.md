---
title: Connecting to an IEEE 1284.3 Data Link Device
author: windows-driver-content
description: Connecting to an IEEE 1284.3 Data Link Device
MS-HAID:
- 'vspd\_99922a87-4074-4dba-a6c8-089a6e0f2be1.xml'
- 'parports.connecting\_to\_an\_ieee\_1284\_3\_data\_link\_device'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 306ff7db-472b-400a-8f14-3f7667160ded
keywords: ["parallel ports WDK , IEEE 1284 devices", "IEEE 1284 WDK", "data link service support WDK parallel ports"]
---

# Connecting to an IEEE 1284.3 Data Link Device


## <a href="" id="ddk-connecting-to-an-ieee-1284-3-data-link-device-kg"></a>


The system-supplied function driver for parallel ports does not provide full support for the IEEE 1284.3 data link layer services; however, it does provide internal device control requests that an upper-level driver can use to connect, disconnect, reset, and signal an IEEE 1284.3 data link device. These services are under development and are intended to support new devices that are not generally available. For more information about support for IEEE 1284.3 data link services, see the sample code *\\src\\kernel\\parport* in the Microsoft Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bparports\parports%5D:%20Connecting%20to%20an%20IEEE%201284.3%20Data%20Link%20Device%20%20RELEASE:%20%287/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


