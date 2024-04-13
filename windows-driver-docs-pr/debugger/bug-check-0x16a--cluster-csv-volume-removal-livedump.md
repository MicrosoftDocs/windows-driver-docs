---
title: Bug Check 0x16A CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP
description: The CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP live dump has a value of 0x0000016A. This indicates that a Cluster Shared Volume Manager volume removal request has timed out.
keywords: ["Bug Check 0x16A CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP", "CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- CLUSTER_CSV_VOLUME_REMOVAL_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x16A: CLUSTER\_CSV\_VOLUME\_REMOVAL\_LIVEDUMP

The CLUSTER\_CSV\_VOLUME\_REMOVAL\_LIVEDUMP live dump has a value of 0x0000016A. This indicates that a Cluster Shared Volume Manager volume removal request has timed out.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## CLUSTER\_CSV\_VOLUME\_REMOVAL\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Cluster Service PID|
|2| Reserved.|
|3| Reserved.|
|4| Reserved.|

## Cause
A Cluster Shared Volume Manager volume removal request has timed out.

The system generated a live dump for analysis of the delay.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## Resolution
 

## See Also

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)