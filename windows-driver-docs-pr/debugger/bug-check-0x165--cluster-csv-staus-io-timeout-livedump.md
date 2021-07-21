---
title: Bug Check 0x165 CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP
description: The CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP bug check has a value of 0x00000165. This indicates that a SMB client is experiencing a timeout situation.
keywords: ["Bug Check 0x165 CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP", "CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
api_name:
- CLUSTER_CSV_STATUS_IO_TIMEOUT_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x165: CLUSTER\_CSV\_STATUS\_IO\_TIMEOUT\_LIVEDUMP

The CLUSTER\_CSV\_STATUS\_IO\_TIMEOUT\_LIVEDUMP bug check has a value of 0x00000165. This indicates that a SMB client on the non-coordinating node complains that an IO on coordinating node is taking too long and fails all IOs with STATUS_IO_TIMEOUT.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## CLUSTER\_CSV\_STATUS\_IO\_TIMEOUT\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1|Optional cluster service PID.|
|2|Cluster Node Id for the node that observed STATUS_IO_TIMEOUT.|
|3|Reserved.|
|4|Reserved.|

## ## Cause

A SMB client on the non-coordinating node complains that an IO on coordinating node is taking too long and fails all IOs with STATUS_IO_TIMEOUT.

Additional information is available in the dump's secondary data streams.

(This code can never be used for a real bugcheck; it is used to identify live dumps including Cluster Shared Volume telemetry.)


## ## Resolution
 

## ## See Also-

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




