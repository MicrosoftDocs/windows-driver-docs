---
title: Bug Check 0x16B CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP
description: The CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP bug check has a value of 0x0000016B. This indicates thatthe Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.
keywords: ["Bug Check 0x16B CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP", "CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
api_name:
- CLUSTER_CSV_CLUSTER_WATCHDOG_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x16B: CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP

The CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP bug check has a value of 0x0000016B. This indicates that the Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



## CLUSTER\_CSV\_CLUSTER\_WATCHDOG\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Cluster Service PID.|
|2| Id of the thread that is stuck.|
|3| Reserved.|
|4| Reserved.|

## ## Cause

The Cluster service user mode watchdog detected that a thread is not making forward progress for a long time.

The system generated a live dump for analysis of the delay.

(This code can never be used for a real bugcheck.)

## ## Resolution
 

## ## See Also-

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




