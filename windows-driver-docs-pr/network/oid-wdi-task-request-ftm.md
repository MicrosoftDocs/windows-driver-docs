---
title: OID_WDI_TASK_REQUEST_FTM
description: OID_WDI_TASK_REQUEST_FTM is issued to the LE to initiate Fine Timing Measurement (FTM) procedures with the listed BSS targets.
ms.date: 05/07/2021
keywords:
 - OID_WDI_TASK_REQUEST_FTM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
ms.custom: 19H1
---

# OID_WDI_TASK_REQUEST_FTM

**OID_WDI_TASK_REQUEST_FTM** is issued to the LE to initiate Fine Timing Measurement (FTM) procedures with the listed BSS targets. The number of targets is less than or equal to the value of **FTMNumberOfSupportedTargets**, obtained from the station attributes.

This task should be completed as soon as all the FTM sessions with the targets are completed, the timeout has expired, or the host has aborted the operation.

When this task is completed, the driver should send an [NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE](ndis-status-wdi-indication-request-ftm-complete.md) status indication that contains a list of FTM responses for each of the targets requested.

After this task is completed, the port should be in a good state and should be ready to process a new FTM request, because the host might immediately re-attempt the task with a new set of targets.

If the LE maintains a station BSS list cache, it can use this cache to obtain the parameters needed to issue FTM request to the targets and ignore the provided data. However, if the target BSSID is not found in the cache the LE needs to use the provided data to attempt the FTMs.

For each target, it is indicated if a Location Configuration Information (LCI) report should be requested. If indicated, the LE should request one from the target. 

## Task parameters

| TLV | Type | Multiple TLV instances allowed | Optional | Description |
| --- | --- | --- | --- | --- |
| [WDI_TLV_FTM_REQUEST_TIMEOUT](wdi-tlv-ftm-request-timeout.md) | UINT32 |   |   | The maximum time, in milliseconds, to complete the FTM. The timeout is set to 150 ms multiplied by the number of targets. |
| [WDI_TLV_FTM_TARGET_BSS_ENTRY](wdi-tlv-ftm-target-bss-entry.md) | WDI_FTM_TARGET_BSS_ENTRY | X |   | A list of the BSS targets with which FTM procedures should be completed. |

## Task completion indication

[NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE](ndis-status-wdi-indication-request-ftm-complete.md)

## Requirements

| &nbsp; | &nbsp; |
| ------ | ------ |
| **Minimum supported client** | Windows 10, version 1903 |
| **Minimum supported server** | Windows Server 2016 |
| **Header** | Dot11wdi.h |
