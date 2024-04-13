---
title: WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS
ms.topic: reference
description: WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS is a TLV that contains initial association parameters for Fast Transition.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_FT_INITIAL_ASSOC_PARAMETERS Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_FT\_INITIAL\_ASSOC\_PARAMETERS

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_FT\_INITIAL\_ASSOC\_PARAMETERS is a TLV that contains initial association parameters for Fast Transition.

## TLV Type


0x105

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                        | Description                |
|---------------------------------------------|----------------------------|
| [**WDI\_TLV\_FT\_MDE**](wdi-tlv-ft-mde.md) | The MDIE of the BSS entry. |

 

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

 

 




