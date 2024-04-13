---
title: Bug Check 0x192 KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL
description: The KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL bug check indicates that a lock tracked by AutoBoost was acquired while executing at DISPATCH_LEVEL or above.
keywords: ["Bug Check 0x192 KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL", "KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL
api_type:
- NA
---

# Bug Check 0x192: KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL


The KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL bug check has a value of 0x00000192. This indicates that a lock tracked by AutoBoost was acquired while executing at DISPATCH\_LEVEL or above.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL Parameters


| Parameter | Description                             |
|-----------|-----------------------------------------|
| 1         | The address of the thread               |
| 2         | The lock address                        |
| 3         | The IRQL at which the lock was acquired |
| 4         | Reserved                                |

 

## Cause

The caller cannot be blocking on a lock above APC\_LEVEL because the lock may be held exclusively by the interrupted thread, which would cause a deadlock.

 

 




