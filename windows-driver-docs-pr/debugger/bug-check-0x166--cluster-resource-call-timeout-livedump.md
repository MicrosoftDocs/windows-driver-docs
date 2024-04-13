---
title: Bug Check 0x166 CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP
description: The CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP live dump has a value of 0x00000166. This indicates that a Cluster Resource call took longer than configured timeout.
keywords: ["Bug Check 0x166 CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP", "CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP"]
ms.date: 12/27/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- CLUSTER_RESOURCE_CALL_TIMEOUT_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x166: CLUSTER\_RESOURCE\_CALL\_TIMEOUT\_LIVEDUMP

The CLUSTER\_RESOURCE\_CALL\_TIMEOUT\_LIVEDUMP live dump has a value of 0x00000166. This indicates that a Cluster Resource call took longer than configured timeout.

## CLUSTER\_RESOURCE\_CALL\_TIMEOUT\_LIVEDUMP Parameters

|Parameter|Description|
|--- |--- |
|1|Resource Host Monitor PID.|
|2|TID of the thread that handles resource call.|
|3|Resource call type - listed below.|
|4|Subcode. When parameter 3 equals 8 then this parameter contains cluster resource control code. When parameter 3 equals 9 then this parameter contains cluster resource type control code.|

**Resource call type**

1  OPEN

2  CLOSE

3  ONLINE

4  OFFLINE

5  TERMINATE

6  ARBITRATE

7  RELEASE

8  RESOURCE CONTROL

9  RESOURCE TYPE CONTROL

10 LOOKS ALIVE

11 IS ALIVE

12 FAILURE NOTIFICATION

13 SHUTDOWN PROCESS

14 CANCEL


## Cause

A Cluster Resource call took longer than configured timeout. The system generated a live dump for analysis of the delay.

(This code can never be used for a real bug check; it is used to identify live dumps.)

## Resolution
 

## See Also

[Troubleshooting Hangs Using Live Dump (Blog)](https://techcommunity.microsoft.com/t5/Failover-Clustering/bg-p/FailoverClustering)

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)




