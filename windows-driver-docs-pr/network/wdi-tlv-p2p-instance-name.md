---
title: WDI_TLV_P2P_INSTANCE_NAME
description: WDI_TLV_P2P_INSTANCE_NAME is a TLV that contains the Instance Name of the service.
ms.assetid: 36CB51E2-D8CB-4C71-B2DB-77F4FDBB8B90
ms.date: 07/18/2017
keywords:
 - WDI_TLV_P2P_INSTANCE_NAME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_P2P\_INSTANCE\_NAME


WDI\_TLV\_P2P\_INSTANCE\_NAME is a TLV that contains the Instance Name of the service.

**Note**  This TLV was added in Windows 10, version 1607, WDI version 1.0.21.

 

## TLV Type


0x12B

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                     |
|-----------|-----------------------------------------------------------------|
| UINT8\[\] | The Instance Name of the service in UTF-8, up to 63 bytes long. |

 

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

 

 




