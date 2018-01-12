---
title: ACE
description: ACE
ms.assetid: efdf43ae-d4d4-4950-9435-e10bf5b75cf2
keywords: ["access control entry WDK file systems", "ACE WDK file systems"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACE


## <a href="" id="ddk-ace-if"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20ACE%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





