---
title: WDI_TLV_IHV_TASK_DEVICE_CONTEXT (dot11wificxtypes.h)
description: WDI_TLV_IHV_TASK_DEVICE_CONTEXT is a WiFiCx TLV that contains IHV-provided device context for NDIS_STATUS_WDI_INDICATION_IHV_TASK_REQUEST.
ms.date: 07/18/2017
keywords:
 - WDI_TLV_IHV_TASK_DEVICE_CONTEXT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT (dot11wificxtypes.h)


WDI\_TLV\_IHV\_TASK\_DEVICE\_CONTEXT is a TLV that contains IHV-provided device context for [NDIS\_STATUS\_WDI\_INDICATION\_IHV\_TASK\_REQUEST](./ndis-status-wdi-indication-ihv-task-request.md).

## TLV Type


0xE0

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| UINT8\[\] | The IHV-provided device context information that is forwarded to the IHV task. |

 

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxtypes.h|

 

