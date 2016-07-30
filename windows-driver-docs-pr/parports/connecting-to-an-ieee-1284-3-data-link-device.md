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


