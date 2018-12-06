---
title: Opening a SerCx2-Managed Serial Port
description: If your peripheral driver controls a device on a serial port that is jointly managed by SerCx2 and a serial controller driver, your driver can open a logical connection to this port and then send I/O requests to the device through the port.
ms.assetid: CBFE1789-0D60-480A-B467-4690DFF88AAC
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="connection-ids-for-serially-connected-peripheral-devices.md" data-raw-source="[Connection IDs for Serially Connected Peripheral Devices](connection-ids-for-serially-connected-peripheral-devices.md)">Connection IDs for Serially Connected Peripheral Devices</a></p></td>
<td><p>If you write a driver for a peripheral device that is connected to a serial port managed by SerCx2, the list of hardware resources that the driver receives includes a <em>connection ID</em> that encapsulates the device connection information from the platform firmware.</p></td>
</tr>
<tr class="even">
<td><p><a href="connecting-a-umdf-peripheral-device-driver-to-a-serial-port.md" data-raw-source="[Connecting a UMDF Peripheral Driver to a Serial Port](connecting-a-umdf-peripheral-device-driver-to-a-serial-port.md)">Connecting a UMDF Peripheral Driver to a Serial Port</a></p></td>
<td><p>The UMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="connecting-a-kmdf-peripheral-device-driver-to-a-serial-port.md" data-raw-source="[Connecting a KMDF Peripheral Driver to a Serial Port](connecting-a-kmdf-peripheral-device-driver-to-a-serial-port.md)">Connecting a KMDF Peripheral Driver to a Serial Port</a></p></td>
<td><p>The KMDF driver for a peripheral device on a SerCx2-managed serial port requires certain hardware resources to operate the device. Included in these resources is the information that the driver needs to open a logical connection to the serial port.</p></td>
</tr>
</tbody>
</table>

 

 

 




