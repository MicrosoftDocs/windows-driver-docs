---
title: Bug Check 0x4000008A THREAD_TERMINATE_HELD_MUTEX
description: The THREAD_TERMINATE_HELD_MUTEX bug check has a value of 0x4000008A.
keywords: ["Bug Check 0x4000008A THREAD_TERMINATE_HELD_MUTEX", "THREAD_TERMINATE_HELD_MUTEX"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- THREAD_TERMINATE_HELD_MUTEX
api_type:
- NA
---

# Bug Check 0x4000008A: THREAD\_TERMINATE\_HELD\_MUTEX


The THREAD\_TERMINATE\_HELD\_MUTEX bug check has a value of 0x4000008A. This indicates that a driver acquired a mutex on a thread that exited before the mutex could be released. This can be caused by a driver returning to user mode without releasing a mutex or by a driver acquiring a mutex and then causing an exception that results in the thread it is running on, being terminated.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## THREAD\_TERMINATE\_HELD\_MUTEX Parameters


| Parameter | Description                                      |
|-----------|--------------------------------------------------|
| 1         | The address of the KTHREAD that owns the KMUTEX. |
| 2         | The address of the KMUTEX that is owned.         |
| 3         | Reserved                                         |
| 4         | Reserved                                         |

 

## Cause

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

To investigate, look at the callstack. If there is a driver on the stack that is directly followed by system exception handling routines and then thread termination routines, this driver is at fault and needs to be fixed so that it does not cause an unhandled exception while holding a kernel mutex. If the stack just shows normal thread termination code and no driver is implicated, run [**!pool**](../debuggercmds/-pool.md) or use [**ln (List Nearest Symbols)**](../debuggercmds/ln--list-nearest-symbols-.md) on the address of the mutex (parameter 2) and see if you can discover who owns the it. This bug will almost certainly be in the code of the owner of that mutex.

 

 




