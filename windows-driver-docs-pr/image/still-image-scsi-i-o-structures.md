---
title: Still Image SCSI I/O Structures
description: Still Image SCSI I/O Structures
ms.assetid: 2cf17295-e3af-4109-bfdd-118aecf80bbe
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Still Image SCSI I/O Structures





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547972" data-raw-source="[&lt;strong&gt;SCSISCAN_CMD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547972)"><strong>SCSISCAN_CMD</strong></a></p></td>
<td><p>Used as a parameter to <a href="https://msdn.microsoft.com/library/windows/desktop/aa363216" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363216)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff542877" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_CMD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542877)"><strong>IOCTL_SCSISCAN_CMD</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff547981" data-raw-source="[&lt;strong&gt;SCSISCAN_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547981)"><strong>SCSISCAN_INFO</strong></a></p></td>
<td><p>Used as a parameter to <a href="https://msdn.microsoft.com/library/windows/desktop/aa363216" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363216)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="https://msdn.microsoft.com/library/windows/hardware/ff542879" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_GET_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542879)"><strong>IOCTL_SCSISCAN_GET_INFO</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

These structures are defined in *scsiscan.h*.

 

 




