---
title: Serial Controller Driver Design Guide
author: windows-driver-content
description: You can design a driver or application that uses the serial I/O request interface to communicate with a peripheral device connected to a serial port.
ms.assetid: 66120e14-20dc-4220-b340-c05cbc59dac8
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Serial Controller Driver Design Guide


You can design a driver or application that uses the [serial I/O request interface](serial-i-o-request-interface.md) to communicate with a peripheral device connected to a serial port. A serial port is a hardware communication interface on a serial controller, which is a 16550 UART or compatible device. To control a serial port to which a peripheral device is permanently connected, you can design a custom serial controller driver that works with version 2 of the serial framework extension (SerCx2), which replaces version 1 (SerCx). Or, to control a named serial port located on the case of a traditional PC, you can use the inbox Serial.sys and Serenum.sys drivers.

## <a href="" id="ddk-serial-ports-and-devices-design-guide-kg"></a>


## In this section


-   [Serial Controller Drivers Overview](serial-drivers-overview.md)
-   [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md)
-   [Using Serial.sys and Serenum.sys](using-serial-sys-and-serenum-sys.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20Controller%20Driver%20Design%20Guide%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


