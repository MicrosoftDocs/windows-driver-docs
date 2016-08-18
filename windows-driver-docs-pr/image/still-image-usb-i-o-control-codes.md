---
title: Still Image USB I/O Control Codes
author: windows-driver-content
description: Still Image USB I/O Control Codes
MS-HAID:
- 'stillimg\_6b814fe6-97df-4ae2-8a7b-b8c601f8b9d1.xml'
- 'image.still\_image\_usb\_i\_o\_control\_codes'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 66a06a25-2fcb-4b14-85e2-485d2d4ac9d5
---

# Still Image USB I/O Control Codes


## <a href="" id="ddk-still-image-usb-i-o-control-codes-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Still%20Image%20USB%20I/O%20Control%20Codes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


