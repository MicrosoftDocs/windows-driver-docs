---
title: Still Image USB I/O Structures
author: windows-driver-content
description: Still Image USB I/O Structures
MS-HAID:
- 'stillimg\_de0f061c-f661-44d8-beb8-e991061ad43b.xml'
- 'image.still\_image\_usb\_i\_o\_structures'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d70c5c11-c8f2-4196-a7f5-d97ceef10ca2
---

# Still Image USB I/O Structures


## <a href="" id="ddk-still-image-usb-i-o-structures-si"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Still%20Image%20USB%20I/O%20Structures%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


