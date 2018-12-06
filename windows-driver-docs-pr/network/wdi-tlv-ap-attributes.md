---
title: WDI_TLV_AP_ATTRIBUTES
description: WDI_TLV_AP_ATTRIBUTES is a TLV that contains the attributes of an access point.
ms.assetid: FD6F635C-85FF-4668-AA17-12677A61F84D
ms.date: 07/18/2017
keywords:
 - WDI_TLV_AP_ATTRIBUTES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_AP\_ATTRIBUTES


WDI\_TLV\_AP\_ATTRIBUTES is a TLV that contains the attributes of an access point.

## TLV Type


0x23

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                        | Multiple TLV instances allowed | Optional | Description                              |
|---------------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------|
| [**WDI\_TLV\_AP\_CAPABILITIES**](wdi-tlv-ap-capabilities.md)                               |                                |          | The access point capabilities.           |
| [**WDI\_TLV\_UNICAST\_ALGORITHM\_LIST**](wdi-tlv-unicast-algorithm-list.md)                |                                |          | The supported unicast algorithms.        |
| [**WDI\_TLV\_MULTICAST\_DATA\_ALGORITHM\_LIST**](wdi-tlv-multicast-data-algorithm-list.md) |                                |          | The supported multicast data algorithms. |

 

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

 

 




