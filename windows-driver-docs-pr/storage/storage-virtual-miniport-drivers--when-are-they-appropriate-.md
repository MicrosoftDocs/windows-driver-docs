---
title: Storage Virtual Miniport Drivers When Are They Appropriate
description: Storage Virtual Miniport Drivers When Are They Appropriate
ms.assetid: 45b9eab9-15b8-4244-bd16-e8850211b8bf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Virtual Miniport Drivers: When Are They Appropriate?


A virtual miniport driver is appropriate when it completely simulates one or more devices, or it has no hardware of its own to control but it communicates with another device using its device driver as a transport for I/O requests. For example, a disk device that uses Random Access Memory (RAM) to store its data is commonly called a RAMDISK. This is a good example of an appropriate use of a virtual miniport driver. Another example would be the use of some type of network adapter that provides a communication link to send and receive storage commands and data. The network adapter has its own device driver that controls its hardware, but the virtual miniport communicates only with the driver, and not the underlying hardware.

A virtual miniport is inappropriate when it is directly controlling real hardware, for example, a host bus adapter.

 

 




