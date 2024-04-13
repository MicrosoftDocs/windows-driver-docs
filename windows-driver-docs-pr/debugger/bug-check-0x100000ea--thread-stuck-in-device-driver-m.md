---
title: Bug Check 0x100000EA THREAD_STUCK_IN_DEVICE_DRIVER_M
description: The THREAD_STUCK_IN_DEVICE_DRIVER_M bug check has a value of 0x100000EA. This indicates that a device driver thread is endlessly spinning.This has the same meaning/parameters as bug check 0xEA.
keywords: ["Bug Check 0x100000EA THREAD_STUCK_IN_DEVICE_DRIVER_M", "THREAD_STUCK_IN_DEVICE_DRIVER_M"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- THREAD_STUCK_IN_DEVICE_DRIVER_M
api_type:
- NA
---

# Bug Check 0x100000EA: THREAD\_STUCK\_IN\_DEVICE\_DRIVER\_M


The THREAD\_STUCK\_IN\_DEVICE\_DRIVER\_M bug check has a value of 0x100000EA. This indicates that a thread in a device driver is endlessly spinning.

Bug check 0x100000EA has the same meaning and parameters as [**bug check 0xEA**](bug-check-0xea--thread-stuck-in-device-driver.md) (THREAD\_STUCK\_IN\_DEVICE\_DRIVER).

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## Resolution

The [!analyze](../debuggercmds/-analyze.md) debug extension displays information about the bug check and can be helpful in determining the root cause.

 

 




