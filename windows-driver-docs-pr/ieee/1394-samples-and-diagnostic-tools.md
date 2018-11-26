---
title: 1394 Samples and Diagnostic Tools
description: 1394 Samples and Diagnostic Tools
ms.assetid: e3ce71da-8c24-405b-b734-98a8c4f45e6b
keywords:
- IEEE 1394 WDK buses , samples
- 1394 WDK buses , samples
- IEEE 1394 WDK buses , diagnostic tools
- 1394 WDK buses , diagnostic tools
- sample drivers WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# 1394 Samples and Diagnostic Tools


The Windows Driver Kit (WDK) includes the source code for two sample kernel-mode drivers (*1394vdev.sys* and *1394diag.sys*) and diagnostic software that permits driver writers to communicate with the IEEE 1394 stack from user-mode.

The driver source code illustrates how drivers communicate with the upper edge of the IEEE 1394 stack. In addition to asynchronous and isochronous data transfers, the sample source code demonstrates the proper management of Plug and Play (PnP) and power management I/O Request Packets (IRPs).

The system enumerates *1394vdev.sys* and *1394diag.sys* differently. The 1394vdev.sys driver is a virtual diagnostic driver that the IEEE 1394 bus driver loads when it receives an IOCTL\_IEEE1394\_API\_REQUEST request. The *1394diag.sys* driver is a physical diagnostic device driver that the IEEE 1394 bus driver loads when an IEEE 1394 hardware device is plugged into the PC. *1394vdev.inf*, which is included in the WDK, loads both of these drivers.

 

 




