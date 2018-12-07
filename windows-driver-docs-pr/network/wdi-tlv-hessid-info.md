---
title: WDI_TLV_HESSID_INFO
description: WDI_TLV_HESSID_INFO is a TLV that contains HESSID information, which includes a list of HESSIDs, the Access Network Type, and Hotspot Indication Element.
ms.assetid: 60D130AC-8249-4B60-B46C-8B83FDDB148F
ms.date: 07/18/2017
keywords:
 - WDI_TLV_HESSID_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_HESSID\_INFO


WDI\_TLV\_HESSID\_INFO is a TLV that contains HESSID information, which includes a list of HESSIDs, the Access Network Type, and Hotspot Indication Element.

## TLV Type


0xFF

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                                 | Multiple TLV instances allowed | Optional | Description                                                                              |
|--------------------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_ACCESS\_NETWORK\_TYPE**](wdi-tlv-access-network-type.md)               |                                |          | The Access Network Type to be used in probe requests for the network being connected to. |
| [**WDI\_TLV\_HESSID**](wdi-tlv-hessid.md)                                           |                                |          | The list of HESSIDs that the port is allowed to connect to.                              |
| [**WDI\_TLV\_HOTSPOT\_INDICATION\_ELEMENT**](wdi-tlv-hotspot-indication-element.md) |                                |          | The Hotspot Indication Element to be used in the Association Request.                    |

 

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

 

 




