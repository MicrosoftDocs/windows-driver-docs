---
title: Bug Check 0x162 KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE
description: The KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE bug check has a value of 0x00000162. This indicates that a lock tracked by AutoBoost was released by a thread that did not own the lock.
keywords: ["Bug Check 0x162 KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE", "KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- KERNEL_AUTO_BOOST_INVALID_LOCK_RELEASE
api_type:
- NA
---

# Bug Check 0x162: KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE


The KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE bug check has a value of 0x00000162. This indicates that a lock tracked by AutoBoost was released by a thread that did not own the lock.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## KERNEL\_AUTO\_BOOST\_INVALID\_LOCK\_RELEASE Parameters


| Parameter | Description                  |
|-----------|------------------------------|
| 1         | The address of the thread    |
| 2         | The lock address             |
| 3         | The session ID of the thread |
| 4         | Reserved                     |

 

## Cause

This is typically caused when some thread releases a lock on behalf of another thread (which is not legal with AutoBoost tracking enabled) or when some thread tries to release a lock it no longer owns.

 

 




