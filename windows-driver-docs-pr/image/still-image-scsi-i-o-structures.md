---
title: Still Image SCSI I/O Structures
author: windows-driver-content
description: Still Image SCSI I/O Structures
ms.assetid: 2cf17295-e3af-4109-bfdd-118aecf80bbe
---

# Still Image SCSI I/O Structures


## <a href="" id="ddk-still-image-scsi-i-o-structures-si"></a>


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
<td><p>[<strong>SCSISCAN_CMD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547972)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_SCSISCAN_CMD</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542877).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SCSISCAN_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547981)</p></td>
<td><p>Used as a parameter to [<strong>DeviceIoControl</strong>](https://msdn.microsoft.com/library/windows/desktop/aa363216), when the specified I/O control code is [<strong>IOCTL_SCSISCAN_GET_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff542879).</p></td>
</tr>
</tbody>
</table>

 

These structures are defined in *scsiscan.h*.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Still%20Image%20SCSI%20I/O%20Structures%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


