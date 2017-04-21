---
title: Still Image SCSI I/O Control Codes
author: windows-driver-content
description: Still Image SCSI I/O Control Codes
ms.assetid: 8db15071-61ac-4bb3-9193-da854a15f376
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Still Image SCSI I/O Control Codes


## <a href="" id="ddk-still-image-scsi-i-o-control-codes-si"></a>


The following table lists and describes all of the I/O Control Codes recognized by the kernel-mode still image driver for SCSI buses.

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
<td><p>[<strong>IOCTL_SCSISCAN_CMD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542877)</p></td>
<td><p>Creates a customized SCSI control descriptor block and sends it to the kernel-mode still image driver for SCSI buses.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SCSISCAN_GET_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542879)</p></td>
<td><p>Returns device information.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SCSISCAN_LOCKDEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542885)</p></td>
<td><p>Reserved for use by Microsoft.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_SCSISCAN_SET_TIMEOUT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542886)</p></td>
<td><p>Modifies the time-out value used by the kernel-mode still image driver for SCSI buses when it accesses a device.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_SCSISCAN_UNLOCKDEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542895)</p></td>
<td><p>Reserved for use by Microsoft.</p></td>
</tr>
</tbody>
</table>

 

These codes are defined in *scsiscan.h*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Still%20Image%20SCSI%20I/O%20Control%20Codes%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


