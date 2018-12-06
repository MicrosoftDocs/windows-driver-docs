---
title: KSCATEGORY_DATACOMPRESSOR
description: KSCATEGORY_DATACOMPRESSOR
ms.assetid: 7e4bf7b3-b3be-4a76-bc9e-0b1b020a7044
keywords: ["KSCATEGORY_DATACOMPRESSOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DATACOMPRESSOR
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_DATACOMPRESSOR


The KSCATEGORY_DATACOMPRESSOR [device interface class](https://msdn.microsoft.com/library/windows/hardware/ff541339) is defined for the [kernel streaming](https://msdn.microsoft.com/library/windows/hardware/ff568277) (KS) functional category that compresses a data stream.

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
<td align="left"><p>KSCATEGORY_DATACOMPRESSOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{1E84C900-7E70-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Drivers for KS devices register instances of KSCATEGORY_DATACOMPRESSOR to indicate to the operating system that the devices support the KSCATEGORY_DATACOMPRESSOR functional category.

The KSCATEGORY_DATACOMPRESSOR functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799).

For information about the device interface class that is defined for the KS functional category that decompresses a data stream, see [**KSCATEGORY_DATADECOMPRESSOR**](kscategory-datadecompressor.md).

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


[**KSCATEGORY_DATADECOMPRESSOR**](kscategory-datadecompressor.md)

[**KSPROPERTY_TOPOLOGY_CATEGORIES**](https://msdn.microsoft.com/library/windows/hardware/ff565799)

 

 






