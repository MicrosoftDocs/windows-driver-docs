---
title: Privileges
description: Privileges
keywords: ["privileges WDK objects", "process privileges WDK"]
ms.date: 06/16/2017
---

# Privileges


A *privilege* is a right that is associated with a process, rather than an object. A typical example of a privilege is **SeBackupPrivilege**, which confers on a process the right to back up files on a disk.

A few routines check the privilege of the current process before completing an operation. If a driver routine is executed by the system process, then the operation always succeeds, but if the driver routine is executed by a user process that does not have the required privilege, then the operation can fail.

The following table lists some examples of privileges and routines that can require them to succeed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Privilege</th>
<th>Routine that can require privilege</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>SeManageVolumePrivilege</strong></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile" data-raw-source="[&lt;strong&gt;ZwSetInformationFile&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationfile)"><strong>ZwSetInformationFile</strong></a> with <em>FileInformationClass</em> = <strong>FileValidDataLengthInformation</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>SeTakeOwnershipPrivilege</strong></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck" data-raw-source="[&lt;strong&gt;SeAccessCheck&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)"><strong>SeAccessCheck</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><strong>SeSecurityPrivilege</strong></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck" data-raw-source="[&lt;strong&gt;SeAccessCheck&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-seaccesscheck)"><strong>SeAccessCheck</strong></a></p></td>
</tr>
</tbody>
</table>

 

Most system routines do not perform any privilege checks.

