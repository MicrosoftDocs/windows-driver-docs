---
title: Still Image USB I/O Control Codes
description: Still Image USB I/O Control Codes
ms.assetid: 66a06a25-2fcb-4b14-85e2-485d2d4ac9d5
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542843" data-raw-source="[&lt;strong&gt;IOCTL_CANCEL_IO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542843)"><strong>IOCTL_CANCEL_IO</strong></a></p></td>
<td><p>Cancels activity on the specified USB transfer pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542849" data-raw-source="[&lt;strong&gt;IOCTL_GET_CHANNEL_ALIGN_RQST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542849)"><strong>IOCTL_GET_CHANNEL_ALIGN_RQST</strong></a></p></td>
<td><p>Returns a USB device&#39;s maximum packet size for the read, write, and interrupt transfer pipes.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542856" data-raw-source="[&lt;strong&gt;IOCTL_GET_DEVICE_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542856)"><strong>IOCTL_GET_DEVICE_DESCRIPTOR</strong></a></p></td>
<td><p>Returns vendor and device identifiers.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542859" data-raw-source="[&lt;strong&gt;IOCTL_GET_PIPE_CONFIGURATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542859)"><strong>IOCTL_GET_PIPE_CONFIGURATION</strong></a></p></td>
<td><p>Returns a description of every transfer pipe supported for a device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542864" data-raw-source="[&lt;strong&gt;IOCTL_GET_USB_DESCRIPTOR&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542864)"><strong>IOCTL_GET_USB_DESCRIPTOR</strong></a></p></td>
<td><p>Returns a specified USB Descriptor.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542866" data-raw-source="[&lt;strong&gt;IOCTL_GET_VERSION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542866)"><strong>IOCTL_GET_VERSION</strong></a></p></td>
<td><p>Returns the version number of the driver.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542869" data-raw-source="[&lt;strong&gt;IOCTL_READ_REGISTERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542869)"><strong>IOCTL_READ_REGISTERS</strong></a></p></td>
<td><p>Reads from USB device registers, using the control pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542872" data-raw-source="[&lt;strong&gt;IOCTL_RESET_PIPE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542872)"><strong>IOCTL_RESET_PIPE</strong></a></p></td>
<td><p>Resets the specified USB transfer pipe.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542900" data-raw-source="[&lt;strong&gt;IOCTL_SEND_USB_REQUEST&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542900)"><strong>IOCTL_SEND_USB_REQUEST</strong></a></p></td>
<td><p>Sends a vendor-defined request to a USB device, using the control pipe, and optionally sends or receives additional data.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542908" data-raw-source="[&lt;strong&gt;IOCTL_SET_TIMEOUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542908)"><strong>IOCTL_SET_TIMEOUT</strong></a></p></td>
<td><p>Sets the time-out value for USB bulk IN, bulk OUT, or interrupt pipe access.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542917" data-raw-source="[&lt;strong&gt;IOCTL_WAIT_ON_DEVICE_EVENT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542917)"><strong>IOCTL_WAIT_ON_DEVICE_EVENT</strong></a></p></td>
<td><p>Returns information about an event occurring on a USB interrupt pipe.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542920" data-raw-source="[&lt;strong&gt;IOCTL_WRITE_REGISTERS&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542920)"><strong>IOCTL_WRITE_REGISTERS</strong></a></p></td>
<td><p>Writes to USB device registers, using the control pipe.</p></td>
</tr>
</tbody>
</table>

 

These codes are defined in *usbscan.h*. For more information about these I/O control codes see:

[USB Still Image I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548569)

 

 




