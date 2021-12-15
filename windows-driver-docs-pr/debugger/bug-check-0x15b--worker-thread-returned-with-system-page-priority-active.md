---
title: Bug Check 0x15B WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE
description: The WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE bug check has a value of 0x0000015B that indicates a worker thread's system page priority was leaked.
keywords: ["Bug Check 0x15B WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE", "WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WORKER_THREAD_RETURNED_WITH_SYSTEM_PAGE_PRIORITY_ACTIVE
api_type:
- NA
---

# Bug Check 0x15B: WORKER\_THREAD\_RETURNED\_WITH\_SYSTEM\_PAGE\_PRIORITY\_ACTIVE


The WORKER\_THREAD\_RETURNED\_WITH\_SYSTEM\_PAGE\_PRIORITY\_ACTIVE bug check has a value of 0x0000015B. This indicates that a worker thread's system page priority was leaked by the called worker routine.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## WORKER\_THREAD\_RETURNED\_WITH\_SYSTEM\_PAGE\_PRIORITY\_ACTIVE Parameters


| Parameter | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| 1         | Address of worker routine (do ln on this address to find the offending driver) |
| 2         | Current system page priority value                                             |
| 3         | WorkItem parameter                                                             |
| 4         | WorkItem address                                                               |

 

 

 




