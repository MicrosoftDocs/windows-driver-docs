---
title: Bug Check 0x14F PDC_WATCHDOG_TIMEOUT
description: The PDC_WATCHDOG_TIMEOUT bug check has a value of 0x0000014F. This indicates that a system component failed to respond within the allocated time period.
ms.assetid: 347D31C2-7027-44BD-A0E8-60C6EC3A2030
keywords: ["Bug Check 0x14F PDC_WATCHDOG_TIMEOUT", "PDC_WATCHDOG_TIMEOUT"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PDC_WATCHDOG_TIMEOUT
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x14F: PDC\_WATCHDOG\_TIMEOUT


The PDC\_WATCHDOG\_TIMEOUT bug check has a value of 0x0000014F. This indicates that a system component failed to respond within the allocated time period, preventing the system from exiting connected standby.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PDC\_WATCHDOG\_TIMEOUT Parameters


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Parameter</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">1</td>
<td align="left">Client ID of the hung component.</td>
</tr>
<tr class="even">
<td align="left">2</td>
<td align="left"><p>Client type of the hung component.</p>
<p>0x1 : A notification client failed to respond.</p>
Parameter 3: Pointer to the notification client (PDC_NOTIFICATION_CLIENT).
Parameter 4: Pointer to a pdc!PDC_14F_TRIAGE structure.
<p>0x2 : A resiliency client failed to respond.</p>
Parameter 3: Pointer to the resiliency client (PDC_RESILIENCY_CLIENT).
Parameter 4: Pointer to a pdc!PDC_14F_TRIAGE structure.
<p>0x3 : An activator client held a reference for too long.</p>
Parameter 3: Pointer to the activation client (pdc!_PDC_ACTIVATOR_CLIENT).
Parameter 4: Pointer to a pdc!PDC_14F_TRIAGE structure.
<p>0x100 : Win32k did not complete a monitor-on request in a timely manner.</p>
Parameter 3: The most recent POWER_MONITOR_REQUEST_REASON value for this request.
Parameter 4: A value indicating the internal path taken to initiate the request.</td>
</tr>
<tr class="odd">
<td align="left">3</td>
<td align="left">See parameter 2</td>
</tr>
<tr class="even">
<td align="left">4</td>
<td align="left">See parameter 2</td>
</tr>
</tbody>
</table>

 

 

 




