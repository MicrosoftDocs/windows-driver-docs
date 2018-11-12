---
title: KSCATEGORY_FILESYSTEM
description: KSCATEGORY_FILESYSTEM
ms.assetid: a3d6a3dc-926a-415a-80ef-c7d2f11ed4bf
keywords: ["KSCATEGORY_FILESYSTEM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_FILESYSTEM
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_FILESYSTEM


The KSCATEGORY_FILESYSTEM [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that moves a data stream into or out of the file system.

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
<td align="left"><p>KSCATEGORY_FILESYSTEM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{760FED5E-9357-11D0-A3CC-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_FILESYSTEM to indicate to the operating system that the devices support the KSCATEGORY_FILESYSTEM functional category.

The KSCATEGORY_FILESYSTEM functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799) functional categories.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## See also


[**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799)

 

 






