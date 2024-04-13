---
title: Connecting to an IEEE 1284.3 Data Link Device
description: Connecting to an IEEE 1284.3 Data Link Device
keywords:
- parallel ports WDK , IEEE 1284 devices
- IEEE 1284 WDK
- data link service support WDK parallel ports
ms.date: 03/03/2023
---

# Connecting to an IEEE 1284.3 Data Link Device





The system-supplied function driver for parallel ports does not provide full support for the IEEE 1284.3 data link layer services; however, it does provide internal device control requests that an upper-level driver can use to connect, disconnect, reset, and signal an IEEE 1284.3 data link device. These services are under development and are intended to support new devices that are not generally available. For more information about support for IEEE 1284.3 data link services, see the sample code *\\src\\kernel\\parport* in the Microsoft Windows Driver Development Kit (DDK). (The DDK preceded the Windows Driver Kit \[WDK\].)

 

 




