---
title: Bug Check 0x192 KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL
description: The KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL bug check indicates that a lock tracked by AutoBoost was acquired while executing at DISPATCH_LEVEL or above.
ms.assetid: D88EF2CC-26DC-44D8-80CB-18D058C6A413
keywords: ["Bug Check 0x192 KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL", "KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_AUTO_BOOST_LOCK_ACQUISITION_WITH_RAISED_IRQL
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x192: KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL


The KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL bug check has a value of 0x00000192. This indicates that a lock tracked by AutoBoost was acquired while executing at DISPATCH\_LEVEL or above.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_AUTO\_BOOST\_LOCK\_ACQUISITION\_WITH\_RAISED\_IRQL Parameters


| Parameter | Description                             |
|-----------|-----------------------------------------|
| 1         | The address of the thread               |
| 2         | The lock address                        |
| 3         | The IRQL at which the lock was acquired |
| 4         | Reserved                                |

 

Cause
-----

The caller cannot be blocking on a lock above APC\_LEVEL because the lock may be held exclusively by the interrupted thread, which would cause a deadlock.

 

 




