---
title: Serial Controller Drivers Overview
author: windows-driver-content
description: All versions of Windows provide driver support for serial controller devices.
ms.assetid: 1EA0221E-0F68-429B-9DA5-4AE2D3394A09
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Serial Controller Drivers Overview


All versions of Windows provide driver support for serial controller devices. The term *serial controller* refers to a 16550 universal asynchronous receiver-transmitter (UART) or compatible device. A serial controller has a serial port through which it communicates with a serially connected peripheral device. To support serial communication, Windows includes the Serial.sys and Serenum.sys drivers, and versions 1 and 2 of the serial framework extension (SerCx and SerCx2).

## Serial.sys and Serenum.sys


Starting with Windows 2000, the system-supplied serial driver, Serial.sys, supports stand-alone serial ports, [COM ports](configuration-of-com-ports.md), and multiport boards. The system-supplied serial enumeration driver, Serenum.sys, enumerates devices that are connected to a serial port that is controlled by Serial.sys or a compatible serial port driver. Serial.sys typically controls the COM ports (typically named COM1, COM2, and so on) located on the case of a PC that is running Windows. These ports conform loosely to the RS-232 standard, but additionally incorporate de facto standards (for example, for voltage levels, pin connections, and hardware flow control) that have evolved to support PCs. For more information, see [Using Serial.sys and Serenum.sys](using-serial-sys-and-serenum-sys.md).

The Windows driver samples repository on GitHub contains the source code for the [Serial](http://go.microsoft.com/fwlink/p/?LinkId=617962) and [Serenum](http://go.microsoft.com/fwlink/p/?LinkId=617961) driver samples, which operate similarly to, and can be installed in place of, the inbox Serial.sys and Serenum.sys drivers.

## SerCx and SerCx2


Starting with Windows 8, SerCx is a system-supplied component that supports serial communication between integrated circuits on a printed circuit board. SerCx is an extension to the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff544296) (KMDF). This extension simplifies the development of custom drivers for serial controllers. SerCx assists an extension-based serial controller driver by handling many of the processing tasks that are common to serial controllers. This driver communicates with SerCx through the [SerCx device driver interface](https://msdn.microsoft.com/library/windows/hardware/dn265348).

Starting with Windows 8.1, SerCx is superceded by SerCx2. SerCx2 has many improvements over SerCx to reduce the size and complexity of serial controller drivers. In particular, SerCx2 relieves the serial controller driver of the processing work required to manage time-outs, and to coordinate I/O transactions that compete for access to the serial controller. As a result, the serial controller driver is smaller and simpler. The hardware vendor for the serial controller supplies an extension-based serial controller driver that manages the hardware-specific functions in the serial controller, and that relies on SerCx2 to perform generic serial-controller tasks. This driver communicates with SerCx2 through the [SerCx2 device driver interface](https://msdn.microsoft.com/library/windows/hardware/dn265349).

For more information about SerCx2, see [Using Version 2 of the Serial Framework Extension (SerCx2)](using-version-2-of-the-serial-framework-extension.md).

## In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[Serial I/O Request Interface](serial-i-o-request-interface.md)</p></td>
<td><p>To control a peripheral device that is connected to a port on a serial controller, a client application or peripheral device driver sends I/O requests to the port.</p></td>
</tr>
<tr class="even">
<td><p>[Differences Between SerCx2.sys and Serial.sys](differences-between-sercx2-and-serial-sys.md)</p></td>
<td><p>Although the inbox Sercx2.sys and Serial.sys driver components both implement the [serial I/O request interface](serial-i-o-request-interface.md), these components are not interchangeable. They are designed to meet different sets of requirements.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Serial%20Controller%20Drivers%20Overview%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


