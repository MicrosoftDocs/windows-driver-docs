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

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## USER\_MODE\_HEALTH\_MONITOR\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Process that failed to satisfy a health check within the configured timeout.| 
|2| Health monitoring timeout (seconds).| 
|3| Watchdog source. In combination with process address this helps to identify the source. See below for possible values. These values are shared with  [USER_MODE_HEALTH_MONITOR](bug-check-0x9e--user-mode-health-monitor.md).| 
|4| Reserved. |

**Watchdog Source Values**

<pre>
0  : WatchdogSourceDefault
     Source was not specified
1  : WatchdogSourceRhsCleanup
     Monitors that RHS process goes away when
     terminating on graceful exit
2  : WatchdogSourceRhsResourceDeadlockBugcheckNow
     RHS was asked to immediately bugcheck machine
      on resource deadlock
3  : WatchdogSourceRhsExceptionFromResource
      Resource has leaked unhandled exception from an entry point,
      RHS is terminating and this watchdog monitors that
      process will go away
4  : WatchdogSourceRhsUnhandledException
      Unhandled exception in RHS.
      RHS is terminating and this watchdog monitors that
      process will go away
5  : WatchdogSourceRhsResourceDeadlock
      Monitors that RHS process goes away when
      terminating on resource deadlock
6  : WatchdogSourceRhsResourceTypeDeadlock
      Monitors that RHS process goes away when
      terminating on resource type deadlock
7  : WatchdogSourceClussvcUnhandledException
      Unhandled exception in clussvc.
      clussvc is terminating and this watchdog monitors that
      process will go away
8  : WatchdogSourceClussvcBugcheckMessageRecieved
      Another cluster node has sent message asking to bugcheck this node.
9  : WatchdogSourceClussvcWatchdogBugcheck
      User mode watchdog has expired and created netft watchdog
      to bugchecked the node.
       0xA : WatchdogSourceClussvcIsAlive
      Cluster service sends heartbeat to netft every 500 millseconds.
      By default, netft expects at least 1 heartbeat per second.
      If this watchdog was triggered that means clussvc is not getting
      CPU to send heartbeats.
      0x65 : WatchdogSourceRhsResourceDeadlockPhysicalDisk
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x66 : WatchdogSourceRhsResourceDeadlockStoragePool
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x67 : WatchdogSourceRhsResourceDeadlockFileServer
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x68 : WatchdogSourceRhsResourceDeadlockSODAFileServer
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x69 : WatchdogSourceRhsResourceDeadlockStorageReplica
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x6A : WatchdogSourceRhsResourceDeadlockStorageQOS
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0x6B : WatchdogSourceRhsResourceDeadlockStorageNFSV2
       A subclass of WatchdogSourceRhsResourceDeadlock.
      0xC9 : WatchdogSourceRhsResourceTypeDeadlockPhysicalDisk
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCA : WatchdogSourceRhsResourceTypeDeadlockStoragePool
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCB : WatchdogSourceRhsResourceTypeDeadlockFileServer
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCC : WatchdogSourceRhsResourceTypeDeadlockSODAFileServer
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCD : WatchdogSourceRhsResourceTypeDeadlockStorageReplica
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCE : WatchdogSourceRhsResourceTypeDeadlockStorageQOS
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
      0xCF : WatchdogSourceRhsResourceTypeDeadlockStorageNFSV2
       A subclass of WatchdogSourceRhsResourceTypeDeadlock.
</pre>

## ## Cause
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


## ## See Also-

[Troubleshooting a Failover Cluster using Windows Error Reporting](/windows-server/failover-clustering/troubleshooting-using-wer-reports)

[Failover Clustering system log events](/windows-server/failover-clustering/system-events)

[Bug Check 0x1C9 USER_MODE_HEALTH_MONITOR](bug-check-0x9e--user-mode-health-monitor.md)

[Bug Check Code Reference](bug-check-code-reference2.md)

