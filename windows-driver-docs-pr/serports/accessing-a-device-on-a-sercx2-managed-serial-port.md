---
title: Accessing a Device on a SerCx2-Managed Serial Port
description: SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected.
ms.assetid: EF7F42D3-21A5-42F8-86AB-897281DF4F18
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing a Device on a SerCx2-Managed Serial Port


SerCx2 and a serial controller driver jointly manage a serial port to which a peripheral device is permanently connected. To access a peripheral device on a SerCx2-managed serial port, your peripheral driver opens a logical connection to the serial port and obtains a file handle to represent this connection. Then the driver uses this handle to send I/O requests to the port.

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
<td><p><a href="peripheral-drivers-for-devices-on-sercx2-managed-serial-ports.md" data-raw-source="[Peripheral Drivers for Devices on SerCx2-Managed Serial Ports](peripheral-drivers-for-devices-on-sercx2-managed-serial-ports.md)">Peripheral Drivers for Devices on SerCx2-Managed Serial Ports</a></p></td>
<td><p>Typically, a serial port managed by SerCx2 is permanently connected to a peripheral device. This device is controlled by a peripheral driver that sends I/O requests to the serial port. These requests transfer data to and from the device, and configure the state of the serial port. I/O requests sent by the peripheral driver are jointly handled by SerCx2 and an associated serial controller driver.</p></td>
</tr>
<tr class="even">
<td><p><a href="opening-a-sercx2-managed-serial-port.md" data-raw-source="[Opening a SerCx2-Managed Serial Port](opening-a-sercx2-managed-serial-port.md)">Opening a SerCx2-Managed Serial Port</a></p></td>
<td><p>If your peripheral driver controls a device on a serial port that is jointly managed by SerCx2 and a serial controller driver, your driver can open a logical connection to this port and then send I/O requests to the device through the port.</p></td>
</tr>
<tr class="odd">
<td><p><a href="sercx2-handling-of-read-and-write-requests.md" data-raw-source="[SerCx2 Handling of Read and Write Requests](sercx2-handling-of-read-and-write-requests.md)">SerCx2 Handling of Read and Write Requests</a></p></td>
<td><p>A peripheral driver sends write (<a href="https://msdn.microsoft.com/library/windows/hardware/ff546904" data-raw-source="[&lt;strong&gt;IRP_MJ_WRITE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546904)"><strong>IRP_MJ_WRITE</strong></a>) and read (<a href="https://msdn.microsoft.com/library/windows/hardware/ff546883" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546883)"><strong>IRP_MJ_READ</strong></a>) requests to a port on a serial controller to transfer data to and from a peripheral device that is connected to the port. The way in which SerCx2 handles these requests is well-defined, even when the requests time out or are canceled.</p></td>
</tr>
<tr class="even">
<td><p><a href="reading-data-from-a-sercx2-managed-serial-port.md" data-raw-source="[Reading Data from a SerCx2-Managed Serial Port](reading-data-from-a-sercx2-managed-serial-port.md)">Reading Data from a SerCx2-Managed Serial Port</a></p></td>
<td><p>A serial controller (or UART) typically includes a receive FIFO. This FIFO provides hardware-controlled buffering of data received from the peripheral device that is connected to the serial port. To read data from the receive FIFO, the peripheral driver for this device sends read (<a href="https://msdn.microsoft.com/library/windows/hardware/ff546883" data-raw-source="[&lt;strong&gt;IRP_MJ_READ&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546883)"><strong>IRP_MJ_READ</strong></a>) requests to the serial port.</p></td>
</tr>
</tbody>
</table>

 

 

 




