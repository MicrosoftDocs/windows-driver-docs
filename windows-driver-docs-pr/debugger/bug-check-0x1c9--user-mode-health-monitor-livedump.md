---
title: Bug Check 0x1C9 USER_MODE_HEALTH_MONITOR_LIVEDUMP
description: The USER_MODE_HEALTH_MONITOR_LIVEDUMP bug check has a value of 0x000001C9. It indicates that one or more critical user mode components failed to satisfy a health check.
keywords: ["Bug Check 0x1C9 USER_MODE_HEALTH_MONITOR_LIVEDUMP", "USER_MODE_HEALTH_MONITOR_LIVEDUMP"]
ms.date: 01/10/2019
topic_type:
- apiref
api_name:
- USER_MODE_HEALTH_MONITOR_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1C9: USER\_MODE\_HEALTH\_MONITOR\_LIVEDUMP

The USER\_MODE\_HEALTH\_MONITOR\_LIVEDUMP bug check has a value of 0x000001C9. It indicates that one or more critical user mode components failed to satisfy a health check.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).
 

## USER\_MODE\_HEALTH\_MONITOR\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Process that failed to satisfy a health check within the configured timeout.| 
|2| Health monitoring timeout (seconds).| 
|3| Watchdog source. In combination with process address this helps to identify the source. See below for possible values. These values are shared with  [USER_MODE_HEALTH_MONITOR](bug-check-0x9e--user-mode-health-monitor.md).| 
|4| Reserved. |

**Watchdog Source Values**

## Cause
-----
One or more critical user mode components failed to satisfy a health check. 
Hardware mechanisms such as watchdog timers can detect that basic kernel 
services are not executing. However, resource starvation issues, including 
memory leaks, lock contention, and scheduling priority misconfiguration, 
may block critical user mode components without blocking DPCs or 
draining the nonpaged pool. 

Kernel components can extend watchdog timer functionality to user mode 
by periodically monitoring critical applications. This livedump indicates 
that a user mode health check failed in a manner such that we will attempt 
to terminate this application and will keep monitoring if termination completes 
in time. If termination does not complete in time, then the machine will be bugchecked 
It restores critical services by rebooting and/or allowing application failover 
to other servers. 

(This code can never be used for a real bugcheck; it is used to identify live dumps.)


## See Also
----------

[Bug Check Code Reference](bug-check-code-reference2.md)

