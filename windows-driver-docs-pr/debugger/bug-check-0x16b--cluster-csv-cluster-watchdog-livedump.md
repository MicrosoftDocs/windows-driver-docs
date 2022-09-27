---
title: Bug Check 0x16B CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP
description: The CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP live dump has a value of 0x0000016B. This indicates thatthe Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.
keywords: ["Bug Check 0x16B CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP", "CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
api_name:
- CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x16B: CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP

The CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP live dump has a value of 0x0000016B. This indicates that the Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.

## CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Cluster Service PID.|
|2| Id of the thread that is stuck.|
|3| Reserved.|
|4| Reserved.|

## Cause

The Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.

The system generated a live dump for analysis of the delay.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## Resolution
 

## See Also

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




