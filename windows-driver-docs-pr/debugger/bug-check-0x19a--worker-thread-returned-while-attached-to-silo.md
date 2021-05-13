---
title: Bug Check 0x19A WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO
description: The WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO bug check has a value of 0x0000019A. This indicates that a worker thread attached to a silo and did not detach before returning.
keywords: ["Bug Check 0x19A WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO", "WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- WORKER_THREAD_RETURNED_WHILE_ATTACHED_TO_SILO
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x19A: WORKER\_THREAD\_RETURNED\_WHILE\_ATTACHED\_TO\_SILO


The WORKER\_THREAD\_RETURNED\_WHILE\_ATTACHED\_TO\_SILO bug check has a value of 0x0000019A. This indicates that a worker thread attached to a silo and did not detach before returning.

> [!IMPORTANT]
> This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## WORKER\_THREAD\_RETURNED\_WHILE\_ATTACHED\_TO\_SILO Parameters


| Parameter | Description               |
|-----------|---------------------------|
| 1         | Address of worker routine |
| 2         | Workitem parameter        |
| 3         | Workitem address          |
| 4         | Reserved                  |

 

## Cause

To investigate use the [**ln (List Nearest Symbols)**](ln--list-nearest-symbols-.md)command on parameter 1 to help identify the mis-behaving driver.

 

 




