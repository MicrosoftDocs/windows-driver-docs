---
title: Bug Check 0x162 KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE
description: The KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE bug check has a value of 0x00000162. This indicates that a lock tracked by AutoBoost was released by a thread that did not own the lock.
ms.assetid: 8430B461-892C-4517-B5E1-94DCDB413B21
keywords: ["Bug Check 0x162 KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE", "KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE
api_type:
- NA
ms.localizationpriority: medium
---

# Bug Check 0x162: KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE


The KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE bug check has a value of 0x00000162. This indicates that a lock tracked by AutoBoost was released by a thread that did not own the lock.

**Important** This topic is for programmers. If you are a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://windows.microsoft.com/windows-10/troubleshoot-blue-screen-errors).

## KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE Parameters


| Parameter | Description                  |
|-----------|------------------------------|
| 1         | The address of the thread    |
| 2         | The lock address             |
| 3         | The session ID of the thread |
| 4         | Reserved                     |

 

Cause
-----

This is typically caused when some thread releases a lock on behalf of another thread (which is not legal with AutoBoost tracking enabled) or when some thread tries to release a lock it no longer owns.

 

 




