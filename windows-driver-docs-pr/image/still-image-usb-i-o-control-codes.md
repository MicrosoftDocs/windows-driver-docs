---
title: Still Image USB I/O Control Codes
author: windows-driver-content
description: Still Image USB I/O Control Codes
ms.assetid: 66a06a25-2fcb-4b14-85e2-485d2d4ac9d5
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Still Image USB I/O Control Codes





The following table lists and describes all of the I/O Control Codes recognized by the kernel-mode still image driver for USB buses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>I/O Control Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IOCTL_CANCEL_IO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542843)</p></td>
<td><p>Cancels activity on the specified USB transfer pipe.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_GET_CHANNEL_ALIGN_RQST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542849)</p></td>
<td><p>Returns a USB device's maximum packet size for the read, write, and interrupt transfer pipes.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_GET_DEVICE_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542856)</p></td>
<td><p>Returns vendor and device identifiers.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_GET_PIPE_CONFIGURATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542859)</p></td>
<td><p>Returns a description of every transfer pipe supported for a device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_GET_USB_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542864)</p></td>
<td><p>Returns a specified USB Descriptor.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_GET_VERSION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542866)</p></td>
<td><p>Returns the version number of the driver.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_READ_REGISTERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542869)</p></td>
<td><p>Reads from USB device registers, using the control pipe.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_RESET_PIPE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542872)</p></td>
<td><p>Resets the specified USB transfer pipe.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SEND_USB_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542900)</p></td>
<td><p>Sends a vendor-defined request to a USB device, using the control pipe, and optionally sends or receives additional data.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SET_TIMEOUT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542908)</p></td>
<td><p>Sets the time-out value for USB bulk IN, bulk OUT, or interrupt pipe access.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_WAIT_ON_DEVICE_EVENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542917)</p></td>
<td><p>Returns information about an event occurring on a USB interrupt pipe.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_WRITE_REGISTERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542920)</p></td>
<td><p>Writes to USB device registers, using the control pipe.</p></td>
</tr>
</tbody>
</table>

 

These codes are defined in *usbscan.h*. For more information about these I/O control codes see:

[USB Still Image I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548569)

 

 




