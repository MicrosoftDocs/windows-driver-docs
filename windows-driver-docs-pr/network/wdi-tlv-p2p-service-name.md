---
title: WDI_TLV_P2P_SERVICE_NAME
ms.topic: reference
description: WDI_TLV_P2P_SERVICE_NAME is a TLV that contains the name of a service.
ms.date: 03/02/2023
keywords:
 - WDI_TLV_P2P_SERVICE_NAME Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_P2P\_SERVICE\_NAME

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


WDI\_TLV\_P2P\_SERVICE\_NAME is a TLV that contains the name of a service.

## TLV Type


0xEC

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                         |
|-----------|-----------------------------------------------------|
| UINT8\[\] | The name of the service, in UTF-8, up to 255 bytes. |

 

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

 

 




