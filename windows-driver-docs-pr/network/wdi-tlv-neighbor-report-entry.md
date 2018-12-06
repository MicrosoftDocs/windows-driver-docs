---
title: WDI_TLV_NEIGHBOR_REPORT_ENTRY
description: WDI_TLV_NEIGHBOR_REPORT_ENTRY is a TLV that contains a neighbor report.
ms.assetid: 23A0AA84-3EDA-4D6F-9140-2361C0CF55AA
ms.date: 07/18/2017
keywords:
 - WDI_TLV_NEIGHBOR_REPORT_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY


WDI\_TLV\_NEIGHBOR\_REPORT\_ENTRY is a TLV that contains a neighbor report.

## TLV Type


0x123

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                          | Multiple TLV instances allowed | Optional | Description                                                         |
|---------------------------------------------------------------|--------------------------------|----------|---------------------------------------------------------------------|
| [**WDI\_TLV\_BSSID**](wdi-tlv-bssid.md)                      |                                |          | The BSSID of the AP in the neighbor report.                         |
| [**WDI\_TLV\_BSSID\_INFO**](wdi-tlv-bssid-info.md)           |                                |          | The BSSID information of the AP.                                    |
| [**WDI\_TLV\_OPERATING\_CLASS**](wdi-tlv-operating-class.md) |                                |          | The operating class of the AP indicated by this BSSID.              |
| [**WDI\_TLV\_CHANNEL\_NUMBER**](wdi-tlv-channel-number.md)   |                                |          | The last known operating channel of the AP indicated by this BSSID. |
| [**WDI\_TLV\_PHY\_TYPE**](wdi-tlv-phy-type.md)               |                                |          | The PHY type of the AP indicated by this BSSID.                     |

 

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

 

 




