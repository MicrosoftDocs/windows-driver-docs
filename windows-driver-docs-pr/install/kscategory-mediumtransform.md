---
title: KSCATEGORY_MEDIUMTRANSFORM
description: KSCATEGORY_MEDIUMTRANSFORM
keywords: ["KSCATEGORY_MEDIUMTRANSFORM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_MEDIUMTRANSFORM
api_location:
- Ks.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_MEDIUMTRANSFORM


The KSCATEGORY_MEDIUMTRANSFORM [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that transforms the type of medium that is being used.

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
<td align="left"><p>KSCATEGORY_MEDIUMTRANSFORM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{CF1DDA2E-9743-11D0-A3EE-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register an instance of KSCATEGORY_MEDIUMTRANSFORM to indicate to the operating system that the devices support the KSCATEGORY_MEDIUMTRANSFORM functional category.

The KSCATEGORY_MEDIUMTRANSFORM functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md) functional categories.

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


[**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md)

 

