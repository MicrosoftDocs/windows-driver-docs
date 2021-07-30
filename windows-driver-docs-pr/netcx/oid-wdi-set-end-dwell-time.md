---
title: OID_WDI_SET_END_DWELL_TIME (dot11wificxintf.h)
description: The OID_WDI_SET_END_DWELL_TIME command is typically sent during an Action Frame exchange, either when WDI has to wait some time before sending a followup Action Frame, or when the protocol sequence is complete.
ms.date: 07/31/2021
keywords:
 - OID_WDI_SET_END_DWELL_TIME Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_SET\_END\_DWELL\_TIME (dot11wificxintf.h)


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

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


 

 




