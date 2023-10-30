---
title: Bug Check 0x170 CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG
description: The CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG bug check has a value of 0x00000170. This indicates that the Cluster disconnect is not making forward progress.
keywords: ["Bug Check 0x170 CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG", "CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG"]
ms.date: 01/03/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG
api_type:
- NA
---

# Bug Check 0x170: CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG

The CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG bug check has a value of 0x00000170. This indicates that Cluster disconnect is not making forward progress.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



## CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG Parameters

|Parameter|Description|
|--- |--- |
|1| Id of the thread that is handling cluster disconnect.|
|2| Timeout in milliseconds. |
|3| Reserved |
|4| Reserved |

## Cause

The Cluster disconnect is not making forward progress.


## Resolution
 

## See Also

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




