---
title: KSCATEGORY_BDA_IP_SINK
description: KSCATEGORY_BDA_IP_SINK
keywords: ["KSCATEGORY_BDA_IP_SINK Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_BDA_IP_SINK
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# KSCATEGORY_BDA_IP_SINK


The KSCATEGORY_BDA_IP_SINK [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a sink filter in the [broadcast driver architecture](/windows-hardware/drivers/ddi/_stream/index) (BDA).

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
<td align="left"><p>KSCATEGORY_BDA_IP_SINK</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{71985F4A-1CA1-11d3-9CC8-00C04F7971E0}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for BDA devices register instances of KSCATEGORY_BDA_IP_SINK to indicate that the devices support a BDA IP sink filter.

For more information, see [BDA Filter Category GUIDs](../stream/bda-filter-category-guids.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Server 2003, Windows XP, Windows 2000 with DirectX 9.0A installed, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

 

