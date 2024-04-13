---
title: OID_WDI_SET_END_DWELL_TIME
ms.topic: reference
description: OID_WDI_SET_END_DWELL_TIME is typically sent during an Action Frame exchange, either when WDI has to wait some time before sending a followup Action Frame, or when the protocol sequence is complete.
ms.date: 03/02/2023
keywords:
 - OID_WDI_SET_END_DWELL_TIME Network Drivers Starting with Windows Vista
ms.custom: 19H1
---

# OID\_WDI\_SET\_END\_DWELL\_TIME

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]


OID\_WDI\_SET\_END\_DWELL\_TIME is typically sent during an Action Frame exchange, either when WDI has to wait some time before sending a followup Action Frame, or when the protocol sequence is complete. This command can be sent on the device port or station port.

| Scope | Set serialized with task | Normal execution time (seconds) |
|-------|--------------------------|---------------------------------|
| Port  | No                       | 1                               |

 

On receipt of this command, the firmware can choose to stop dwelling on the channel that had been specified when WDI sent the command to send the Action Frame. If the Dwell Time had already expired, the firmware should ignore this command.

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

 

 




