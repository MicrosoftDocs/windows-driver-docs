---
title: OID_WDI_TASK_STOP_AP (dot11wificxintf.h)
description: The OID_WDI_TASK_STOP_AP command requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_STOP_AP Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_STOP\_AP (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_TASK\_STOP\_AP requests that the IHV component disconnects all connected clients on the specified port and stops beaconing and responding to probe requests. AP configuration and MIB attributes are preserved.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

## Task parameters


None
## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP\_COMPLETE](ndis-status-wdi-indication-stop-ap-complete.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

 




