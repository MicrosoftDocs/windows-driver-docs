---
title: Still Image SCSI I/O Control Codes
description: Still Image SCSI I/O Control Codes
ms.assetid: 8db15071-61ac-4bb3-9193-da854a15f376
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Still Image SCSI I/O Control Codes





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542877" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_CMD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542877)"><strong>IOCTL_SCSISCAN_CMD</strong></a></p></td>
<td><p>Creates a customized SCSI control descriptor block and sends it to the kernel-mode still image driver for SCSI buses.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542879" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_GET_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542879)"><strong>IOCTL_SCSISCAN_GET_INFO</strong></a></p></td>
<td><p>Returns device information.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542885" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_LOCKDEVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542885)"><strong>IOCTL_SCSISCAN_LOCKDEVICE</strong></a></p></td>
<td><p>Reserved for use by Microsoft.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542886" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_SET_TIMEOUT&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542886)"><strong>IOCTL_SCSISCAN_SET_TIMEOUT</strong></a></p></td>
<td><p>Modifies the time-out value used by the kernel-mode still image driver for SCSI buses when it accesses a device.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff542895" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_UNLOCKDEVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff542895)"><strong>IOCTL_SCSISCAN_UNLOCKDEVICE</strong></a></p></td>
<td><p>Reserved for use by Microsoft.</p></td>
</tr>
</tbody>
</table>

 

These codes are defined in *scsiscan.h*.

 

 




