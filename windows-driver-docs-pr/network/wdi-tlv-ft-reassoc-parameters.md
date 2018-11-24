---
title: WDI_TLV_FT_REASSOC_PARAMETERS
description: WDI_TLV_FT_REASSOC_PARAMETERS is a TLV that contains reassociation parameters for Fast Transition.
ms.assetid: 36F260FF-E80A-4EFF-B009-B06446229470
ms.date: 07/18/2017
keywords:
 - WDI_TLV_FT_REASSOC_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_FT\_REASSOC\_PARAMETERS


WDI\_TLV\_FT\_REASSOC\_PARAMETERS is a TLV that contains reassociation parameters for Fast Transition.

## TLV Type


0x106

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                    | Description                                                                                                                            |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_FT\_MDE**](wdi-tlv-ft-mde.md)             | The MDIE of the BSS entry.                                                                                                             |
| [**WDI\_TLV\_FT\_PMKR0NAME**](wdi-tlv-ft-pmkr0name.md) | The PMKR0Name. This is needed during Fast Transition. The STA needs to send the PMKR0Name during the authentication request to the AP. |
| [**WDI\_TLV\_FT\_FTE**](wdi-tlv-ft-fte.md)             | The Fast Transition Element that contains the R0KHID and SNonce.                                                                       |

 

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

 

 




