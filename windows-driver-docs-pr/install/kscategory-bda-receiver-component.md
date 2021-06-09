---
title: KSCATEGORY_BDA_RECEIVER_COMPONENT
description: KSCATEGORY_BDA_RECEIVER_COMPONENT
keywords: ["KSCATEGORY_BDA_RECEIVER_COMPONENT Device and Driver Installation"]
topic_type:
- apiref
api_name:
- KSCATEGORY_BDA_RECEIVER_COMPONENT
api_location:
- Bdamedia.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# KSCATEGORY_BDA_RECEIVER_COMPONENT


The KSCATEGORY_BDA_RECEIVER_COMPONENT [device interface class](./overview-of-device-interface-classes.md) is defined for the [kernel streaming](../stream/streaming-minidrivers2.md) (KS) functional category for a receiver in the [broadcast driver architecture](/windows-hardware/drivers/ddi/_stream/index) (BDA).

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
<td align="left"><p>KSCATEGORY_BDA_RECEIVER_COMPONENT</p></td>
</tr>
<tr class="even">
<td align="left"><p>Class GUID</p></td>
<td align="left"><p>{FD0A5AF4-B41D-11d2-9C95-00C04F7971E0}</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Drivers for BDA devices register instances of KSCATEGORY_BDA_RECEIVER_COMPONENT to indicate to the operating system that the devices support a BDA receiver filter.

For more information about the KS functional category for a BDA receiver filters, see [Common Control Nodes and Filters](../stream/common-control-nodes-and-filters.md), [Starting a BDA Minidriver](../stream/starting-a-bda-minidriver.md), and [BDA Filter Category GUIDs](../stream/bda-filter-category-guids.md).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows XP, Windows 2000 with DirectX 9.0A installed, and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Bdamedia.h (include Bdamedia.h)</td>
</tr>
</tbody>
</table>

 

