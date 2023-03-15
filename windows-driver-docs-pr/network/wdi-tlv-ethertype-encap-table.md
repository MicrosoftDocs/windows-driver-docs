---
title: WDI_TLV_ETHERTYPE_ENCAP_TABLE
ms.topic: reference
description: WDI_TLV_ETHERTYPE_ENCAP_TABLE is a TLV that contains the Ethertype encapsulations for the association.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_ETHERTYPE_ENCAP_TABLE Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_ETHERTYPE\_ENCAP\_TABLE is a TLV that contains the Ethertype encapsulations for the association.

## TLV Type


0x31

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type                                                                                       | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](/windows-hardware/drivers/ddi/wditypes/ns-wditypes-_wdi_ethertype_encapsulation_entry)\[\] | An array of [**WDI\_ETHERTYPE\_ENCAPSULATION\_ENTRY**](/windows-hardware/drivers/ddi/wditypes/ns-wditypes-_wdi_ethertype_encapsulation_entry) elements that specifies the Ethertype encapsulations for the association. |

 

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

 

