---
title: Still Image SCSI I/O Structures
author: windows-driver-content
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

 

 




