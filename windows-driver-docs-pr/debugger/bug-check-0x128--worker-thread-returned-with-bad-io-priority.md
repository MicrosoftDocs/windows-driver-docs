---
title: Bug Check 0x128 WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY
description: The WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY bug check has a value of 0x00000128. This indicates that a worker threads IOPriority was wrongly modified by the called worker routine.
ms.assetid: 2659491F-2257-4553-A7A4-ECA39DD0A0F7
keywords: ["Bug Check 0x128 WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY", "WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WORKER_THREAD_RETURNED_WITH_BAD_IO_PRIORITY
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x128: WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY


The WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY bug check has a value of 0x00000128. This indicates that a worker threads IOPriority was wrongly modified by the called worker routine.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## WORKER\_THREAD\_RETURNED\_WITH\_BAD\_IO\_PRIORITY Parameters


| Parameter | Description                                                                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1         | Address of worker routine (Use the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md) command on this address to find the offending driver) |
| 2         | Current IoPrioirity value                                                                                                                               |
| 3         | Workitem parameter                                                                                                                                      |
| 4         | Workitem address                                                                                                                                        |

 

 

 




