---
title: NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST (dot11wificxintf.h)
description: WiFiCx drivers use NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST to request that the Microsoft component queue an IHV task.ObjectPort .
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


WiFiCx drivers use NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST to request that the Microsoft component queue an IHV task.

| Object |
|--------|
| Port   |

 

## Payload data


| Type                                                                                         | Multiple TLV instances allowed | Optional | Description                                                                                                                                  |
|----------------------------------------------------------------------------------------------|--------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS**](./wdi-tlv-ihv-task-request-parameters.md) |                                |          | The IHV-requested priority for this task. Refer to the [**WDI\_IHV\_TASK\_PRIORITY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ihv_task_priority) enum for valid values. |
| [**WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT**](./wdi-tlv-ihv-task-device-context.md)         |                                | X        | The IHV-provided context information that is forwarded to [OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md).                                       |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|


## See also


[OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md)

 

