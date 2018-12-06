---
title: Using Version 2 of the Serial Framework Extension (SerCx2)
description: You can write a serial controller driver that works together with version 2 of the serial framework extension (SerCx2) to manage a serial controller.
ms.assetid: 192C25B2-936B-40D3-A0EA-5D02A234506E
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="sercx2-architectural-overview.md" data-raw-source="[SerCx2 Architectural Overview](sercx2-architectural-overview.md)">SerCx2 Architectural Overview</a></p></td>
<td><p>SerCx2 works together with a serial controller driver to enable communication between a peripheral driver and a serially connected peripheral device. Typically, the serial controller is integrated into a System on a Chip (SoC) chip to provide low-pin-count communication with a peripheral device that is external to the SoC chip but is soldered to the same printed circuit board.</p></td>
</tr>
<tr class="even">
<td><p><a href="serial-controller-driver-design-for-sercx2.md" data-raw-source="[Serial Controller Driver Design for SerCx2](serial-controller-driver-design-for-sercx2.md)">Serial Controller Driver Design for SerCx2</a></p></td>
<td><p>To manage your serial controller, you write a serial controller driver that performs hardware-specific tasks and communicates with SerCx2. Starting with Windows 8.1, SerCx2 is a system-supplied component that handles many of the processing tasks that are common to serial controllers.</p></td>
</tr>
<tr class="odd">
<td><p><a href="accessing-a-device-on-a-sercx2-managed-serial-port.md" data-raw-source="[Accessing a Device on a SerCx2-Managed Serial Port](accessing-a-device-on-a-sercx2-managed-serial-port.md)">Accessing a Device on a SerCx2-Managed Serial Port</a></p></td>
<td><p>SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected. To access a peripheral device on a SerCx2-managed serial port, your peripheral driver opens a logical connection to the serial port and obtains a file handle to represent this connection. Then the driver uses this handle to send I/O requests to the port.</p></td>
</tr>
</tbody>
</table>

 

 

 




