---
title: KSCATEGORY_COMMUNICATIONSTRANSFORM
description: KSCATEGORY_COMMUNICATIONSTRANSFORM
keywords: ["KSCATEGORY_COMMUNICATIONSTRANSFORM Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_COMMUNICATIONSTRANSFORM
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_COMMUNICATIONSTRANSFORM


The KSCATEGORY_COMMUNICATIONSTRANSFORM [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a communication transform device.

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
<td align="left"><p>KSCATEGORY_COMMUNICATIONSTRANSFORM</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{CF1DDA2C-9743-11D0-A3EE-00A0C9223196}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS devices register instances of KSCATEGORY_COMMUNICATIONSTRANSFORM to indicate to the operating system that the devices support the KSCATEGORY_COMMUNICATIONSTRANSFORM functional category.

The KSCATEGORY_COMMUNICATIONSTRANSFORM functional category is one of the [**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md).

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

 

