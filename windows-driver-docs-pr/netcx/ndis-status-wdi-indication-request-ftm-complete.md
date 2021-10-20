---
title: NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE (dot11wificxintf.h)
description: WiFiCx drivers send the NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE indication to the host as a task completion indication for OID_WDI_TASK_REQUEST_FTM.
ms.date: 07/30/2021
keywords:
 - NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE (dot11wificxintf.h)

[!INCLUDE[WiFiCx topic note](../includes/wificx-version-warning.md)]

WiFiCx drivers send the **NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE** status indication to the host as a task completion indication for [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md). This notification contains a list of Fine Timing Measurement (FTM) responses received from each requested target.

## Payload data

| Type | TLV | Multiple TLV instances allowed | Optional | Description |
| --- | --- |--- | --- | --- |
| WDI_STATUS | A field in the header.  |   | |The general completion status of the event. |
| [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md) | Multiple TLV\<WDI_TLV_FTM_RESPONSE> | X |   | A list of FTM responses for each target. |

## Requirements

|Requirement|Value|
|--- |--- |
|Minimum supported client|Windows 11|
|Minimum supported server|Windows Server 2022|
|Header|dot11wificxintf.h|

