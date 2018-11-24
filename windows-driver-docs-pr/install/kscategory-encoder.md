---
title: KSCATEGORY_ENCODER
description: KSCATEGORY_ENCODER
ms.assetid: 409dbb1f-7b28-4cb3-bdba-da927cf67133
keywords: ["KSCATEGORY_ENCODER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_ENCODER
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_ENCODER


The KSCATEGORY_ENCODER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that encodes data.

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
<td align="left"><p>KSCATEGORY_ENCODER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{19689BF6-C384-48fd-AD51-90E58C79F70B}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_ENCODER to indicate to the operating system that the devices support the KSCATEGORY_ENCODER functional category.

For an example of how to register this functional category in an INF file, see the *Bdan.inf* INF file that is included with the software tuner sample in the *src/swtuner/algtuner* directory of the WDK.

For information about encoders, see [Encoder Devices](https://msdn.microsoft.com/library/windows/hardware/ff559535) and [Encoder Installation and Registration](https://msdn.microsoft.com/library/windows/hardware/ff559551).

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
<td align="left"><p>Available in Windows Vista, Windows Server 2003, Windows XP Service Pack 1 (SP1), and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

 

 





