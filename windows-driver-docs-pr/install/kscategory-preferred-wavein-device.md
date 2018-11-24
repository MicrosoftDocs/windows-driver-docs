---
title: KSCATEGORY_PREFERRED_WAVEIN_DEVICE
description: KSCATEGORY_PREFERRED_WAVEIN_DEVICE
ms.assetid: d5f20f18-396a-4cb7-b653-038310ce8e42
keywords: ["KSCATEGORY_PREFERRED_WAVEIN_DEVICE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_PREFERRED_WAVEIN_DEVICE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_PREFERRED_WAVEIN_DEVICE


The KSCATEGORY_PREFERRED_WAVEIN_DEVICE [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category for the preferred wave input device.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Attribute</th>
<th align="left">Setting</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Identifier</p></td>
<td align="left"><p>KSCATEGORY_PREFERRED_WAVEIN_DEVICE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{D6C50671-72C1-11D2-9755-0000F8004788}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

A user selects the preferred wave input device in the Multimedia property pages in the Control Panel.

This functional category is reserved for exclusive use by the system-supplied [WDM Audio Components](https://msdn.microsoft.com/library/windows/hardware/ff538905).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Server 2003, Windows XP, Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





