---
title: Bug Check 0x9E USER_MODE_HEALTH_MONITOR
description: The USER_MODE_HEALTH_MONITOR bug check has a value of 0x0000009E. This bug check indicates that one or more critical user-mode components failed to satisfy a health check.
keywords: ["Bug Check 0x9E USER_MODE_HEALTH_MONITOR", "USER_MODE_HEALTH_MONITOR"]
ms.date: 12/22/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- USER_MODE_HEALTH_MONITOR
api_type:
- NA
---

# Bug Check 0x9E: USER\_MODE\_HEALTH\_MONITOR

The USER\_MODE\_HEALTH\_MONITOR bug check has a value of 0x0000009E. This bug check indicates that one or more critical user-mode components failed to satisfy a health check.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## USER\_MODE\_HEALTH\_MONITOR Parameters


|Parameter|Description|
|--- |--- |
|1|The process that failed to satisfy a health check in the configured time-out|
|2|The health monitoring time-out, in seconds|
|3|Watchdog source. In combination with process address helps to identify what sub-component has created this watchdog. Values listed below.|
|4|Reserved|

## VALUES

<pre>
0  : WatchdogSourceDefault
      Source was not specified
1  : WatchdogSourceRhsCleanup
      Monitors that RHS (Resource Hosting Subsystem) process goes away when
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

## Cause

Hardware mechanisms, such as watchdog timers, can detect that basic kernel services are not executing. However, resource starvation issues (including memory leaks, lock contention, and scheduling priority misconfiguration) can block critical user-mode components without blocking deferred procedure calls (DPCs) or draining the non-paged pool.

Kernel components can extend watchdog timer functionality to user mode by periodically monitoring critical applications. This bug check indicates that a user-mode health check failed in a way that prevents graceful shutdown. This bug check restores critical services by restarting or enabling application failover to other servers.

Like all bug checks, use the system event log to look for events that precede the stop code in time. Events in the log that immediately proceed the bug check should be examined for information on possible causes.

## See Also

[Troubleshooting a Failover Cluster using Windows Error Reporting](/windows-server/failover-clustering/troubleshooting-using-wer-reports)

[Failover Clustering system log events](/windows-server/failover-clustering/system-events)

[Bug Check 0x1C9 USER_MODE_HEALTH_MONITOR_LIVEDUMP](bug-check-0x1c9--user-mode-health-monitor-livedump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
