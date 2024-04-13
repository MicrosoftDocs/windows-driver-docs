---
title: WDI_TLV_AP_BAND_CHANNEL
ms.topic: reference
description: WDI_TLV_AP_BAND_CHANNEL is a TLV that specifies access point band and channel information.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_AP_BAND_CHANNEL Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_AP\_BAND\_CHANNEL

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_AP\_BAND\_CHANNEL is a TLV that specifies access point band and channel information.

**Note**  This TLV was added in Windows 10, version 1511, WDI version 1.0.10.

 

## TLV Type


0x127

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                               | Multiple TLV instances allowed | Optional | Description                                                |
|--------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------|
| [**WDI\_TLV\_BANDID**](wdi-tlv-bandid.md)                         |                                |          | Specifies the identifier for the band.                     |
| [**WDI\_TLV\_CHANNEL\_INFO\_LIST**](wdi-tlv-channel-info-list.md) |                                | X        | Specifies a list of channels to start the access point on. |

 

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

## See also


[OID\_WDI\_TASK\_START\_AP](./oid-wdi-task-start-ap.md)

 

