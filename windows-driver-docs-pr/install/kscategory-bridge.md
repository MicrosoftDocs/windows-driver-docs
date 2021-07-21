---
title: KSCATEGORY_BRIDGE
description: KSCATEGORY_BRIDGE
keywords: ["KSCATEGORY_BRIDGE Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_BRIDGE
api_location:
- Ks.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_BRIDGE


The KSCATEGORY_BRIDGE [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category that supports a software interface between the KS subsystem and another software component.

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
<td align="left"><p>KSCATEGORY_BRIDGE</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{085AFF00-62CE-11CF-A5D6-28DB04C10000}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for KS audio adapter devices register instances of KSCATEGORY_BRIDGE to indicate to the operating system that the devices support the KSCATEGORY_BRIDGE functional category.

For more information about KSCATEGORY_BRIDGE functional category, see [**KSPROPERTY_TOPOLOGY_CATEGORIES**](../stream/ksproperty-topology-categories.md).

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

 

