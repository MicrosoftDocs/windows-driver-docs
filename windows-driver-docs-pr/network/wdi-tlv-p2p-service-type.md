---
title: WDI_TLV_P2P_SERVICE_TYPE
description: WDI_TLV_P2P_SERVICE_TYPE is a TLV that contains the Service Type of the service.
ms.assetid: D9C3F099-DED1-400E-9D3F-7AF6D2D286DF
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_SERVICE_TYPE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_SERVICE\_TYPE


WDI\_TLV\_P2P\_SERVICE\_TYPE is a TLV that contains the Service Type of the service.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x129

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                    |
|-----------|----------------------------------------------------------------|
| UINT8\[\] | The Service Type of the service in UTF-8, up to 21 bytes long. |

 

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

 

 




