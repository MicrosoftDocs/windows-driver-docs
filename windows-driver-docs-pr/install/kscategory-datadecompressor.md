---
title: KSCATEGORY_DATADECOMPRESSOR
description: KSCATEGORY_DATADECOMPRESSOR
keywords: ["KSCATEGORY_DATADECOMPRESSOR Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_DATADECOMPRESSOR
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_DATADECOMPRESSOR


The KSCATEGORY_DATADECOMPRESSOR [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that decompresses a data stream.

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
<td align="left"><p>KSCATEGORY_DATADECOMPRESSOR</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{2721AE20-7E70-11D0-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_DATADECOMPRESSOR to indicate to the operating system that the devices support the KSCATEGORY_DATADECOMPRESSOR functional category.

The KSCATEGORY_DATADECOMPRESSOR functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md).

For information about the device interface class that is defined for the KS functional category that compresses a data stream, see [**KSCATEGORY_DATACOMPRESSOR**](kscategory-datacompressor.md).

## Requirements

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


[**KSCATEGORY_DATACOMPRESSOR**](kscategory-datacompressor.md)

[**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md)

 

