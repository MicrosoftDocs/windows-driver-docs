---
title: WDI_TLV_IHV_TASK_REQUEST_PARAMETERS (dot11wificxtypes.hpp)
description: WDI_TLV_IHV_TASK_REQUEST_PARAMETERS is a WiFiCx TLV that contains the requested priority for NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST.
ms.date: 07/31/2021
keywords:
 - WDI_TLV_IHV_TASK_REQUEST_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS (dot11wificxtypes.hpp)


WDI\_TLV\_IHV\_TASK\_REQUEST\_PARAMETERS is a TLV that contains the requested priority for [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](./ndis-status-wdi-indication-ihv-task-request.md).

## TLV Type


0xDF

## Length


The size (in bytes) of a UINT32.

## Values


| Type   | Description                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------|
| UINT32 | The IHV-requested priority for this task. See [**WDI\_IHV\_TASK\_PRIORITY**](/windows-hardware/drivers/ddi/dot11wificxtypes/ne-dot11wificxtypes-wdi_ihv_task_priority) for valid priority values. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.hpp|

 

