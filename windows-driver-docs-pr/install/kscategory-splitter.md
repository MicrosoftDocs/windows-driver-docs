---
title: KSCATEGORY_SPLITTER
description: KSCATEGORY_SPLITTER
ms.assetid: 056b6bc0-5566-4498-959d-dbc9725aa03e
keywords: ["KSCATEGORY_SPLITTER Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_SPLITTER
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_SPLITTER


The KSCATEGORY_SPLITTER [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that splits a data stream.

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
<td align="left"><p>KSCATEGORY_SPLITTER</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{0A4252A0-7E70-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS audio adapter devices register an instance of KSCATEGORY_SPLITTER to indicate to the operating system that the devices support the KSCATEGORY_SPLITTER functional category.

The KSCATEGORY_SPLITTER functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799) functional categories.

For general information about splitters, see [AVStream Splitters](https://msdn.microsoft.com/library/windows/hardware/ff554255).

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

 

 






