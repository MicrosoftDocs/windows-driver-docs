---
title: NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE (dot11wificxintf.h)
ms.topic: reference
description: NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE indicates OID_WDI_TASK_IHV is complete.
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_IHV_TASK_COMPLETE Network Drivers Starting with Windows Vista
---

# NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE (dot11wificxintf.h)

[!INCLUDE [WiFiCx topic note](../includes/wificx-version-warning.md)]


NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_COMPLETE indicates the completion of [OID\_WDI\_TASK\_IHV](oid-wdi-task-ihv.md).

| Object |
|--------|
| Port   |

 

## Payload data


This indication contains no additional data. The data in the header is sufficient. The completion status from the message is not forwarded to anyone.

## Requirements


|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|
 

 




