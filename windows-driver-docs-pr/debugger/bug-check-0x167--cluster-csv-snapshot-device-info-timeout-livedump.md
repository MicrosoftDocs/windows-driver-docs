---
title: Bug Check 0x167 CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP
description: The CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP bug check has a value of 0x00000167. This indicates that a Cluster  Service call to the volsnap to query snapshot information took too long.
keywords: ["Bug Check 0x167 CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP", "CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP"]
ms.date: 01/03/2019
topic_type:
- apiref
api_name:
- CLUSTER_CSV_SNAPSHOT_DEVICE_INFO_TIMEOUT_LIVEDUMP
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x167: CLUSTER\_CSV\_SNAPSHOT\_DEVICE\_INFO\_TIMEOUT\_LIVEDUMP

The CLUSTER\_CSV\_SNAPSHOT\_DEVICE\_INFO\_TIMEOUT\_LIVEDUMPP bug check has a value of 0x00000167. This indicates that a Cluster Service call to the volsnap to query snapshot information took too long.


> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



## CLUSTER\_CSV\_SNAPSHOT\_DEVICE\_INFO\_TIMEOUT\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1| Cluster Service PID.|
|2| TID of the thread that handles volsnap query.|
|3| This parameter has a value of 1 if we timeout out while CSV volume is active and 2 if we timeout out even after taking CSV volume down.|
|4| Reserved.|


## ## Cause

A Cluster Service call to the volsnap to query snapshot information took too long.

(This code can never be used for a real bugcheck.)

## ## Resolution
 

## ## See Also-

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




