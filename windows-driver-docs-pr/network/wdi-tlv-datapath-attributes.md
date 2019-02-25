---
title: WDI_TLV_DATAPATH_ATTRIBUTES
description: WDI_TLV_DATAPATH_ATTRIBUTES is a TLV that contains datapath attributes.
ms.assetid: 3477054B-01CE-4D08-8A58-49FD8840B237
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DATAPATH_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DATAPATH\_ATTRIBUTES


WDI\_TLV\_DATAPATH\_ATTRIBUTES is a TLV that contains datapath attributes.

## TLV Type


0xB8

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                      | Multiple TLV instances allowed | Optional | Description                |
|---------------------------------------------------------------------------|--------------------------------|----------|----------------------------|
| [**WDI\_TLV\_DATAPATH\_CAPABILITIES**](wdi-tlv-datapath-capabilities.md) |                                | X        | The datapath capabilities. |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




