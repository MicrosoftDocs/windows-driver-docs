---
title: Still Image USB I/O Structures
author: windows-driver-content
description: Still Image USB I/O Structures
ms.assetid: d70c5c11-c8f2-4196-a7f5-d97ceef10ca2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Still Image USB I/O Structures





The following table lists and describes all of the structures associated with the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Structure</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>CHANNEL_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff539466)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_GET_CHANNEL_ALIGN_RQST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542849).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>DEVICE_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540576)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_GET_DEVICE_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542856).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DRV_VERSION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff541204)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_GET_VERSION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542866).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IO_BLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542924)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_READ_REGISTERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542869) or [<strong>IOCTL_WRITE_REGISTERS</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542920).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IO_BLOCK_EX</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542928)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_SEND_USB_REQUEST</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542900).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>USBSCAN_GET_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548534)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_GET_USB_DESCRIPTOR</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542864).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>USBSCAN_PIPE_CONFIGURATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548541)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_GET_PIPE_CONFIGURATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542859).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>USBSCAN_PIPE_INFORMATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548547)</p></td>
<td><p>Used to describe a USB transfer pipe for a still image device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>USBSCAN_TIMEOUT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548554)</p></td>
<td><p>Stores time-out values for USB bulk IN and bulk OUT operations, and interrupts.</p></td>
</tr>
</tbody>
</table>

 

These structures are defined in *usbscan.h*. For more information about these structures see:

[USB Still Image Structures](https://msdn.microsoft.com/library/windows/hardware/ff548574)

 

 




