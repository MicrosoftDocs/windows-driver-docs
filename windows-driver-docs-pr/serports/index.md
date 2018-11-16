---
title: Serial Controller Driver Design Guide
description: You can design a driver or application that uses the serial I/O request interface to communicate with a peripheral device connected to a serial port.
ms.assetid: 66120e14-20dc-4220-b340-c05cbc59dac8
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Serial Controller Driver Design Guide


You can design a driver or application that uses the [serial I/O request interface](serial-i-o-request-interface.md) to communicate with a peripheral device connected to a serial port. A serial port is a hardware communication interface on a serial controller, which is a 16550 UART or compatible device. To control a serial port to which a peripheral device is permanently connected, you can design a custom serial controller driver that works with version 2 of the serial framework extension (SerCx2), which replaces version 1 (SerCx). Or, to control a named serial port located on the case of a traditional PC, you can use the inbox Serial.sys and Serenum.sys drivers.




## In this section


-   [Serial Controller Drivers Overview](serial-drivers-overview.md)
-   [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md)
-   [Using Serial.sys and Serenum.sys](using-serial-sys-and-serenum-sys.md)

 

 




