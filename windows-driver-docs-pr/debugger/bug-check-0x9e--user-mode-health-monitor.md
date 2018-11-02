---
title: Bug Check 0x9E USER_MODE_HEALTH_MONITOR
description: The USER_MODE_HEALTH_MONITOR bug check has a value of 0x0000009E. This bug check indicates that one or more critical user-mode components failed to satisfy a health check.
ms.assetid: 5ad56234-5150-4acb-828d-198c2e5fb9b6
keywords: ["Bug Check 0x9E USER_MODE_HEALTH_MONITOR", "USER_MODE_HEALTH_MONITOR"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- USER_MODE_HEALTH_MONITOR
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x9E: USER\_MODE\_HEALTH\_MONITOR


The USER\_MODE\_HEALTH\_MONITOR bug check has a value of 0x0000009E. This bug check indicates that one or more critical user-mode components failed to satisfy a health check.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## USER\_MODE\_HEALTH\_MONITOR Parameters


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
<td align="left"><p>1</p></td>
<td align="left"><p>The process that failed to satisfy a health check in the configured time-out</p></td>
</tr>
<tr class="even">
<td align="left"><p>2</p></td>
<td align="left"><p>The health monitoring time-out, in seconds</p></td>
</tr>
<tr class="odd">
<td align="left"><p>3</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
<tr class="even">
<td align="left"><p>4</p></td>
<td align="left"><p>Reserved</p></td>
</tr>
</tbody>
</table>

 

Cause
-----

Hardware mechanisms, such as watchdog timers, can detect that basic kernel services are not executing. However, resource starvation issues (including memory leaks, lock contention, and scheduling priority misconfiguration) can block critical user-mode components without blocking deferred procedure calls (DPCs) or draining the non-paged pool.

Kernel components can extend watchdog timer functionality to user mode by periodically monitoring critical applications. This bug check indicates that a user-mode health check failed in a way that prevents graceful shutdown. This bug check restores critical services by restarting or enabling application failover to other servers.

On the Microsoft Windows Server 2003, Enterprise Edition, Windows Server 2003, Datacenter Edition, and Windows 2000 with Service Pack 4 (SP4) operating systems, a user-mode hang can also cause this bug check. The bug check occurs in this situation only if the user has set **HangRecoveryAction** to a value of 3.

 

 




