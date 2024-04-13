---
title: WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE
ms.topic: reference
description: WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE is a TLV that contains the requested Association Parameter TLV types.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ASSOCIATION_PARAMETERS_REQUESTED_TYPE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ASSOCIATION\_PARAMETERS\_REQUESTED\_TYPE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ASSOCIATION\_PARAMETERS\_REQUESTED\_TYPE is a TLV that contains the requested Association Parameter TLV types.

## TLV Type


0xBB

## Length


The size (in bytes) of the array of UINT16 elements. The array must contain 1 or more elements.

## Values


| Type       | Description                                                                                                                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT16\[\] | The list of Association Parameters TLV types that are requested. Valid TLV types are [**WDI\_TLV\_PMKID**](wdi-tlv-pmkid.md) (0x9F) and [**WDI\_TLV\_EXTRA\_ASSOCIATION\_REQUEST\_IES**](wdi-tlv-extra-association-request-ies.md) (0x40). |

 

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

 

 




