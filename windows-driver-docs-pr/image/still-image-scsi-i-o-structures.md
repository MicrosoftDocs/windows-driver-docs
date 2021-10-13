---
title: Still Image SCSI I/O Structures
description: Still Image SCSI I/O Structures
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
<td><p><a href="/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_cmd" data-raw-source="[&lt;strong&gt;SCSISCAN_CMD&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_cmd)"><strong>SCSISCAN_CMD</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_cmd" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_CMD&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_cmd)"><strong>IOCTL_SCSISCAN_CMD</strong></a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_info" data-raw-source="[&lt;strong&gt;SCSISCAN_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiscan/ns-scsiscan-_scsiscan_info)"><strong>SCSISCAN_INFO</strong></a></p></td>
<td><p>Used as a parameter to <a href="/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol" data-raw-source="[&lt;strong&gt;DeviceIoControl&lt;/strong&gt;](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)"><strong>DeviceIoControl</strong></a>, when the specified I/O control code is <a href="/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_get_info" data-raw-source="[&lt;strong&gt;IOCTL_SCSISCAN_GET_INFO&lt;/strong&gt;](/windows-hardware/drivers/ddi/scsiscan/ni-scsiscan-ioctl_scsiscan_get_info)"><strong>IOCTL_SCSISCAN_GET_INFO</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

These structures are defined in *scsiscan.h*.

