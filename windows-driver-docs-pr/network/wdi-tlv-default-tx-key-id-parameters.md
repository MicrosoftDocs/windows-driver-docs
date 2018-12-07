---
title: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS
description: WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS is a TLV that contains the default key ID for packet transmission on a port for OID_WDI_SET_DEFAULT_KEY_ID.
ms.assetid: 24E7E758-FEED-4D2A-BAA8-6DBC08726FBA
ms.date: 07/18/2017
keywords:
 - WDI_TLV_DEFAULT_TX_KEY_ID_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS


WDI\_TLV\_DEFAULT\_TX\_KEY\_ID\_PARAMETERS is a TLV that contains the default key ID for packet transmission on a port for [OID\_WDI\_SET\_DEFAULT\_KEY\_ID](https://msdn.microsoft.com/library/windows/hardware/dn925928).

## TLV Type


0x54

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                     |
|--------|-----------------------------------------------------------------|
| UINT32 | Specifies the default key ID for packet transmission on a port. |

 

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

 

 




