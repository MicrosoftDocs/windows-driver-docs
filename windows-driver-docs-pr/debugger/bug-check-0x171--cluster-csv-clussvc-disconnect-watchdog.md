---
title: Bug Check 0x171 CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG
description: The CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG bug check has a value of 0x00000171. This indicates that the Cluster disconnect is not making forward progress.
keywords: ["Bug Check 0x171 CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG", "CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG"]
ms.date: 01/03/2019
topic_type:
- apiref
api_name:
- CLUSTER_CSV_CLUSSVC_DISCONNECT_WATCHDOG
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x171: CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG

The CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG bug check has a value of 0x00000171. This indicates that Cluster disconnect is not making forward progress.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).



## CLUSTER\_CSV\_CLUSSVC\_DISCONNECT\_WATCHDOG Parameters

|Parameter|Description|
|--- |--- |
|1| Id of the thread that is handling cluster disconnect.|
|2| Timeout in milliseconds. |
|3| Reserved |
|4| Reserved |

## ## Cause

The Cluster disconnect is not making forward progress.


## ## Resolution
 

## ## See Also-

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Bug Check Code Reference](bug-check-code-reference2.md)




