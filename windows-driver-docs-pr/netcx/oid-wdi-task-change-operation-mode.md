---
title: OID_WDI_TASK_CHANGE_OPERATION_MODE (dot11wificxintf.h)
description: The OID_WDI_TASK_CHANGE_OPERATION_MODE command configures the operation mode for the port.
ms.date: 07/31/2021
keywords:
 - OID_WDI_TASK_CHANGE_OPERATION_MODE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WDI\_TASK\_CHANGE\_OPERATION\_MODE (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]


OID\_WDI\_TASK\_CHANGE\_OPERATION\_MODE configures the operation mode for the port.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 4                                     | 1                               |

 

## Task parameters


| TLV                                                              | Multiple TLV instances allowed | Optional | Description                 |
|------------------------------------------------------------------|--------------------------------|----------|-----------------------------|
| [**WDI\_TLV\_OPERATION\_MODE**](./wdi-tlv-operation-mode.md) |                                |          | The desired operation mode. |

 

## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_CHANGE\_OPERATION\_MODE\_COMPLETE](ndis-status-wdi-indication-change-operation-mode-complete.md)

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

 

