---
title: WDI_TLV_VIRTUALIZATION_ATTRIBUTES
description: WDI_TLV_VIRTUALIZATION_ATTRIBUTES is a TLV that contains virtualization attributes.
ms.assetid: BFB21903-2532-46FB-97E3-6AF254B6BB1E
ms.date: 07/18/2017
keywords:
 - WDI_TLV_VIRTUALIZATION_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_VIRTUALIZATION\_ATTRIBUTES


WDI\_TLV\_VIRTUALIZATION\_ATTRIBUTES is a TLV that contains virtualization attributes.

## TLV Type


0x24

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                  | Multiple TLV instances allowed | Optional | Description                      |
|---------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------|
| [**WDI\_TLV\_VIRTUALIZATION\_CAPABILITIES**](wdi-tlv-virtualization-capabilities.md) |                                |          | The virtualization capabilities. |

 

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

 

 




