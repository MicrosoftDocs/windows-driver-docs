---
title: Using Version 2 of the Serial Framework Extension (SerCx2)
author: windows-driver-content
description: You can write a serial controller driver that works together with version 2 of the serial framework extension (SerCx2) to manage a serial controller.
ms.assetid: 192C25B2-936B-40D3-A0EA-5D02A234506E
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Version 2 of the Serial Framework Extension (SerCx2)


You can write a serial controller driver that works together with version 2 of the serial framework extension (SerCx2) to manage a serial controller. You can also write a peripheral driver for a peripheral device that is connected to a port on a serial controller that is jointly managed by SerCx2 and a serial controller driver. This peripheral driver uses the [serial I/O request interface](serial-i-o-request-interface.md) to transfer data to and from the device. An extension-based serial controller driver handles all hardware-specific tasks for the serial controller, but uses SerCx2 to perform many system tasks that are common to all serial controllers. SerCx2 is a system-supplied component starting with Windows 8.1.

**Note**  SerCx2 replaces version 1 of the serial framework extension (SerCx), which was introduced in Windows 8. New serial controller drivers that are intended to run only in Windows 8.1 and later versions of Windows should be written to use the [SerCx2 DDI](https://msdn.microsoft.com/library/windows/hardware/dn265349) instead of the [SerCx DDI](https://msdn.microsoft.com/library/windows/hardware/dn265348). However, Windows 8.1 and later versions of Windows support existing serial controller drivers that use the SerCx DDI.

 

A serial controller is a 16550 universal asynchronous receiver/transmitter (UART) or compatible device. For more information, see [Serial Controller Drivers Overview](serial-drivers-overview.md).

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
<td><p>[SerCx2 Architectural Overview](sercx2-architectural-overview.md)</p></td>
<td><p>SerCx2 works together with a serial controller driver to enable communication between a peripheral driver and a serially connected peripheral device. Typically, the serial controller is integrated into a System on a Chip (SoC) chip to provide low-pin-count communication with a peripheral device that is external to the SoC chip but is soldered to the same printed circuit board.</p></td>
</tr>
<tr class="even">
<td><p>[Serial Controller Driver Design for SerCx2](serial-controller-driver-design-for-sercx2.md)</p></td>
<td><p>To manage your serial controller, you write a serial controller driver that performs hardware-specific tasks and communicates with SerCx2. Starting with Windows 8.1, SerCx2 is a system-supplied component that handles many of the processing tasks that are common to serial controllers.</p></td>
</tr>
<tr class="odd">
<td><p>[Accessing a Device on a SerCx2-Managed Serial Port](accessing-a-device-on-a-sercx2-managed-serial-port.md)</p></td>
<td><p>SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected. To access a peripheral device on a SerCx2-managed serial port, your peripheral driver opens a logical connection to the serial port and obtains a file handle to represent this connection. Then the driver uses this handle to send I/O requests to the port.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Using%20Version%202%20of%20the%20Serial%20Framework%20Extension%20%28SerCx2%29%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


