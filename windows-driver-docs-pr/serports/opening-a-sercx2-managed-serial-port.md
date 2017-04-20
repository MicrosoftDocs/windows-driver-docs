---
title: Opening a SerCx2-Managed Serial Port
author: windows-driver-content
description: If your peripheral driver controls a device on a serial port that is jointly managed by SerCx2 and a serial controller driver, your driver can open a logical connection to this port and then send I/O requests to the device through the port.
ms.assetid: CBFE1789-0D60-480A-B467-4690DFF88AAC
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opening a SerCx2-Managed Serial Port


Starting with Windows 8.1, version 2 of the serial framework extension (SerCx2) works together with a serial controller driver to manage a serial port on a serial controller. If your peripheral driver controls a device on a serial port that is jointly managed by SerCx2 and a serial controller driver, your driver can open a logical connection to this port and then send I/O requests to the device through the port.

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
<td><p>[Connection IDs for Serially Connected Peripheral Devices](connection-ids-for-serially-connected-peripheral-devices.md)</p></td>
<td><p>If you write a driver for a peripheral device that is connected to a serial port managed by SerCx2, the list of hardware resources that the driver receives includes a <em>connection ID</em> that encapsulates the device connection information from the platform firmware.</p></td>
</tr>
<tr class="even">
<td><p>[Connecting a UMDF Peripheral Driver to a Serial Port](connecting-a-umdf-peripheral-device-driver-to-a-serial-port.md)</p></td>
<td><p>The UMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.</p></td>
</tr>
<tr class="odd">
<td><p>[Connecting a KMDF Peripheral Driver to a Serial Port](connecting-a-kmdf-peripheral-device-driver-to-a-serial-port.md)</p></td>
<td><p>The KMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Opening%20a%20SerCx2-Managed%20Serial%20Port%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


