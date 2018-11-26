---
title: WDI_TLV_CIPHER_KEY_TKIP_INFO
description: WDI_TLV_CIPHER_KEY_TKIP_INFO is a TLV that contains TKIP information.
ms.assetid: 330A93F5-43E7-4A4A-A6BD-EF276D6F09A1
ms.date: 07/18/2017
keywords:
 - WDI_TLV_CIPHER_KEY_TKIP_INFO Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_CIPHER\_KEY\_TKIP\_INFO


WDI\_TLV\_CIPHER\_KEY\_TKIP\_INFO is a TLV that contains TKIP information.

## TLV Type


0x4B

## Length


The sum (in bytes) of the sizes of all contained TLVs.

## Values


| Type                                                                    | Multiple TLV instances allowed | Optional | Description                      |
|-------------------------------------------------------------------------|--------------------------------|----------|----------------------------------|
| [**WDI\_TLV\_CIPHER\_KEY\_TKIP\_KEY**](wdi-tlv-cipher-key-tkip-key.md) |                                |          | Specifies the TKIP key material. |
| [**WDI\_TLV\_CIPHER\_KEY\_TKIP\_MIC**](wdi-tlv-cipher-key-tkip-mic.md) |                                |          | Specifies the TKIP MIC material. |

 

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

 

 




