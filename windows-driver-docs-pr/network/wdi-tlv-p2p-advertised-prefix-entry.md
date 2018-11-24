---
title: WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY
description: WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY is a TLV that contains a Wi-Fi Direct advertised prefix entry.
ms.assetid: 484A7784-EDD5-46F0-91E0-060D23ADC0BD
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_ADVERTISED_PREFIX_ENTRY Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_ADVERTISED\_PREFIX\_ENTRY


WDI\_TLV\_P2P\_ADVERTISED\_PREFIX\_ENTRY is a TLV that contains a Wi-Fi Direct advertised prefix entry.

## TLV Type


0x110

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                        | Multiple TLV instances allowed | Optional | Description                                                      |
|-----------------------------------------------------------------------------|--------------------------------|----------|------------------------------------------------------------------|
| [**WDI\_TLV\_P2P\_SERVICE\_NAME**](wdi-tlv-p2p-service-name.md)            |                                |          | Name of the service, in UTF-8, with a maximum size of 255 bytes. |
| [**WDI\_TLV\_P2P\_SERVICE\_NAME\_HASH**](wdi-tlv-p2p-service-name-hash.md) |                                |          | Hash of Service Name.                                            |

 

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

 

 




