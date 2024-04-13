---
title: Bug Check 0x179 CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP
description: The CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP live dump has a value of 0x00000179. This indicates that SMB client on the initiator node complains that an IO on target node is taking too long and fails all IOs with STATUS_IO_TIMEOUT.
keywords: ["Bug Check 0x179 CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP", "CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- CLUSTER_CLUSPORT_STATUS_IO_TIMEOUT_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x179: CLUSTER\_CLUSPORT\_STATUS\_IO\_TIMEOUT\_LIVEDUMP

The CLUSTER\_CLUSPORT\_STATUS\_IO\_TIMEOUT\_LIVEDUMP live dump has a value of 0x00000179. This indicates that SMB client on the initiator node complains that an IO to a target node is taking too long and fails all IOs with STATUS_IO_TIMEOUT.

## CLUSTER\_CLUSPORT\_STATUS\_IO\_TIMEOUT\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--------------- |
|1| IRP that ran into the timeout.|
|2| Reserved. |
|3| Reserved. |
|4| Reserved. |


## Cause

SMB client on the initiator node complains that an IO on target node is taking too long and fails all IOs with STATUS_IO_TIMEOUT.

In response to that, the cluster initiator captures live dump on the initiator node so we can analyze what IO is taking time.

Additional information is available in the dump's secondary data streams.

(This code can never be used for a real bug check; it is used to identify live dumps.)


## Resolution
 

## See Also

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)




