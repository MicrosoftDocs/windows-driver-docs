---
title: Bug Check 0x128 WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY
description: The WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY bug check has a value of 0x00000128. This indicates that a worker threads IOPriority was wrongly modified by the called worker routine.
keywords: ["Bug Check 0x128 WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY", "WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY
api_type:
- NA
---

# Bug Check 0x128: WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY


The WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY bug check has a value of 0x00000128. This indicates that a worker threads IOPriority was wrongly modified by the called worker routine.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY Parameters


| Parameter | Description                                                                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1         | Address of worker routine (Use the [**ln (List Nearest Symbols)**](../debuggercmds/ln--list-nearest-symbols-.md) command on this address to find the offending driver) |
| 2         | Current IoPrioirity value                                                                                                                               |
| 3         | Workitem parameter                                                                                                                                      |
| 4         | Workitem address                                                                                                                                        |

 

 

 




