---
title: OID_WDI_SET_FLUSH_BSS_ENTRY
ms.topic: reference
description: OID_WDI_SET_FLUSH_BSS_ENTRY is sent to the device to flush the list of BSS entries maintained by the adapter. This command can only be sent on the station port.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_FLUSH_BSS_ENTRY Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_FLUSH\_BSS\_ENTRY is sent to the device to flush the list of BSS entries maintained by the adapter. This command can only be sent on the station port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

## Set property parameters


No additional parameters. The data in the header is sufficient.
## Set property results


No additional data. The data in the header is sufficient.

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
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>

 

 




