---
title: Bug Check 0x1D6 WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS
description: The WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS bug check has a value of 0x000001D6. It indicates that a worker thread changed its workload class and did not revert it before returning.
keywords: ["Bug Check 0x1D6 WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS", "WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS"]
ms.date: 01/11/2019
topic_type:
- apiref
api_name:
- WORKER_THREAD_RETURNED_WITH_NON_DEFAULT_WORKLOAD_CLASS
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x1D6: WORKER\_THREAD\_RETURNED\_WITH\_NON\_DEFAULT\_WORKLOAD\_CLASS

The WORKER\_THREAD\_RETURNED\_WITH\_NON\_DEFAULT\_WORKLOAD\_CLASS bug check has a value of 0x000001D6. It indicates that a worker thread changed its workload class and did not revert it before returning.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

 

## WORKER\_THREAD\_RETURNED\_WITH\_NON\_DEFAULT\_WORKLOAD\_CLASS Parameters

|Parameter|Description|
|-------- |---------- |
|1| Address of worker routine (use ln on this to find the responsible driver) |
|2| Current workload class value. |
|3| WorkItem parameter. |
|4| WorkItem address. |

## ## Cause

A worker thread changed its workload class and did not revert it before returning.


## ## See Also-

[Bug Check Code Reference](bug-check-code-reference2.md)

