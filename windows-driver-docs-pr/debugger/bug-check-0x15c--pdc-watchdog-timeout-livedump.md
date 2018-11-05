---
title: Bug Check 0x15C PDC_WATCHDOG_TIMEOUT_LIVEDUMP
description: The PDC_WATCHDOG_TIMEOUT_LIVEDUMP bug check has a value of 0x0000015C that indicates that a system component failed to respond, preventing entering or exiting connected standby.
ms.assetid: 4FBB884D-99B5-4564-95D5-396323651C5A
keywords: ["Bug Check 0x15C PDC_WATCHDOG_TIMEOUT_LIVEDUMP", "PDC_WATCHDOG_TIMEOUT_LIVEDUMP"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- PDC_WATCHDOG_TIMEOUT_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x15C: PDC\_WATCHDOG\_TIMEOUT\_LIVEDUMP


The PDC\_WATCHDOG\_TIMEOUT\_LIVEDUMP bug check has a value of 0x0000015C. This indicates that a system component failed to respond within the allocated time period, preventing the system from entering or exiting connected standby.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## PDC\_WATCHDOG\_TIMEOUT\_LIVEDUMP Parameters


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
0x1 : A notification client failed to respond.
<p>3 - Pointer to the notification client (pdc!_PDC_NOTIFICATION_CLIENT).</p>
<p>4 - Pointer to a pdc!PDC_14F_TRIAGE structure.</p>
0x2 : A resiliency client failed to respond.
<p>3 - Pointer to the resiliency client (pdc!_PDC_RESILIENCY_CLIENT).</p>
<p>4 - Pointer to a pdc!PDC_14F_TRIAGE structure.</p>
0x3 : An activator client held a reference for too long
<p>3 - Pointer to the activation client (pdc!_PDC_ACTIVATOR_CLIENT).</p>
<p>4 - Pointer to a pdc!PDC_14F_TRIAGE structure.</p></td>
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

 

 

 




