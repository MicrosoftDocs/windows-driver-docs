---
title: ACE
description: ACE
ms.assetid: efdf43ae-d4d4-4950-9435-e10bf5b75cf2
keywords: ["access control entry WDK file systems", "ACE WDK file systems"]
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ACE





An ACE is an access-control entry (ACE) in an access-control list (ACL).

Following are the currently defined ACE types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>ACCESS_ALLOWED_ACE</p></td>
<td align="left"><p>Grants specified rights to a user or group. This ACE is stored in a discretionary ACL (DACL).</p></td>
</tr>
<tr class="even">
<td align="left"><p>ACCESS_DENIED_ACE</p></td>
<td align="left"><p>Denies specified rights to a user or group. This ACE is stored in a DACL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SYSTEM_AUDIT_ACE</p></td>
<td align="left"><p>Specifies what types of access will cause system-level audits. This ACE is stored in a system ACL (SACL).</p></td>
</tr>
</tbody>
</table>

 

A fourth ACE structure, SYSTEM\_ALARM\_ACE, is not currently supported.

An ACL contains a list of ACEs. An ACE defines access to an object for a specific user or group or defines the types of access that generate system-administration messages or alarms for a specific user or group. The user or group is identified by a security identifier (SID).

Each ACE starts with an ACE\_HEADER structure. The format of the data following the header varies according to the ACE type specified in the header.

This structure must be aligned on a 32-bit boundary.

Requirements: ntifs.h (include ntifs.h)

## Related topics


[**ACCESS\_ALLOWED\_ACE**](https://msdn.microsoft.com/library/windows/hardware/ff538796)

[**ACCESS\_DENIED\_ACE**](https://msdn.microsoft.com/library/windows/hardware/ff538831)

[**ACE\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff538847)

[**ACL**](https://msdn.microsoft.com/library/windows/hardware/ff538866)

[**RtlAddAccessAllowedAce**](https://msdn.microsoft.com/library/windows/hardware/ff552092)

[**RtlGetAce**](https://msdn.microsoft.com/library/windows/hardware/ff552288)

[**SID**](https://msdn.microsoft.com/library/windows/hardware/ff556740)

[**SYSTEM\_ALARM\_ACE**](https://msdn.microsoft.com/library/windows/hardware/ff556769)

[**SYSTEM\_AUDIT\_ACE**](https://msdn.microsoft.com/library/windows/hardware/ff556771)

 

 






