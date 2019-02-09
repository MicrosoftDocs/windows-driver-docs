---
title: OID_WDI_TASK_REQUEST_FTM
description: OID_WDI_TASK_REQUEST_FTM is issued to the LE to initiate Fine Time Measurement (FTM) procedures with the listed BSS targets.
ms.assetid: 67E17BD2-9216-43B5-8D1E-C6DF8537D79E
ms.date: 02/08/2019
keywords:
 - OID_WDI_TASK_REQUEST_FTM Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID_WDI_TASK_REQUEST_FTM


OID_WDI_TASK_REQUEST_FTM is issued to the LE to initiate Fine Time Measurement (FTM) procedures with the listed BSS targets. The number of targets is less than or equal to the value of **FTMNumberOfSupportedTargets**, obtained from the station attributes.

This task should be completed as soon as all the FTM sessions with the targets are completed, the timeout has expired, or the host has aborted the operation.

When this task is completed, the driver should send an [NDIS_STATUS_WDI_INDICATION_REQUEST_FTM_COMPLETE]() status indication that contains a list of FTM responses for each of the targets requested.

After this task is completed, the port should be in a good state and should be ready to process a new FTM request, because the host might immediately re-attempt the task with a new set of targets.

For each target, it is indicated if an LCI report should be requested. If indicated, the LE should request one from the target.

| Object | Abort capable | Default priority (host driver policy) | Normal execution time (seconds) |
|--------|---------------|---------------------------------------|---------------------------------|
| Port   | No            | 2                                     | 1                               |

 

## Task parameters



## Task completion indication


[NDIS\_STATUS\_WDI\_INDICATION\_STOP\_AP\_COMPLETE](ndis-status-wdi-indication-stop-ap-complete.md)

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10, version 1903</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Dot11wdi.h</td>
</tr>
</tbody>
</table>