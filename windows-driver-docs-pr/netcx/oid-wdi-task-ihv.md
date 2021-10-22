---
title: OID_WDI_TASK_IHV (dot11wificxintf.h)
description: The OID_WDI_TASK_IHV command is used to start an IHV-initiated task.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_IHV Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_IHV (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_TASK\_IHV is used to start an IHV-initiated task.

| Object | Abort capable                                           | Default priority (host driver policy)       | Normal execution time (seconds) |
|--------|---------------------------------------------------------|---------------------------------------------|---------------------------------|
| Port   | Yes. The port must be in a clean state after the abort. | Priority depends on IHV-requested settings. | 10                              |

 

The task is initiated by the sending [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](ndis-status-wdi-indication-ihv-task-request.md), and is prioritized based on the value requested by the IHV.

## Task parameters


| TLV                                                                                  | Multiple TLV instances allowed | Optional | Description                                                                                                                                                                   |
|--------------------------------------------------------------------------------------|--------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT**](./wdi-tlv-ihv-task-device-context.md) |                                | X        | The context data provided by the IHV component. This is forwarded from [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_ TASK\_REQUEST](ndis-status-wdi-indication-ihv-task-request.md). |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE](ndis-status-wdi-indication-ihv-task-complete.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

