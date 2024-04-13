---
title: WDI_TLV_IHV_DATA
ms.topic: reference
description: WDI_TLV_IHV_DATA is a TLV that contains IHV-specific information that is used by the IHV extensibility module.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_IHV_DATA Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_IHV\_DATA

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_IHV\_DATA is a TLV that contains IHV-specific information that is used by the IHV extensibility module.

## TLV Type


0xBD

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                            |
|-----------|------------------------------------------------------------------------|
| UINT8\[\] | IHV specific information that is used by the IHV extensibility module. |

 

## Requirements

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

 

 




