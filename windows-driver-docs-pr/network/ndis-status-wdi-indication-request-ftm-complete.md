---
title: NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE
description: NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE
ms.date: 02/11/2019
keywords:
 - NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE

[!INCLUDE [WDI topic note](../includes/wdi-version-warning.md)]

Miniport drivers send the **NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE** status indication to the host as a task completion indication for [OID_WDI_TASK_REQUEST_FTM](oid-wdi-task-request-ftm.md). This notification contains a list of Fine Timing Measurement (FTM) responses received from each requested target.

## Payload data

| Type | TLV | Multiple TLV instances allowed | Optional | Description |
| --- | --- |--- | --- | --- |
| WDI_STATUS | A field in the header.  |   | The general completion status of the event. |
| [WDI_TLV_FTM_RESPONSE](wdi-tlv-ftm-response.md) | Multiple TLV\<WDI_TLV_FTM_RESPONSE> | X |   | A list of FTM responses for each target. |

## Requirements

**Minimum supported client**: Windows 10, version 1903

**Minimum supported server**: Windows Server 2016

**Header**: Dot11wdi.h

