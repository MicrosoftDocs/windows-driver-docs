---
title: Avoid Polling Devices
description: Avoid Polling Devices
ms.assetid: c50c9c6f-c8eb-4e52-854a-3ebc4fdc874c
keywords: ["I/O WDK kernel , device polling", "device polling WDK I/O", "polling devices WDK I/O", "loop counters WDK I/O", "counters WDK I/O"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Avoid Polling Devices





A device driver should avoid polling its device unless absolutely necessary, and should never use a whole time-slice for polling. Polling a device is an expensive operation that makes any operating system compute-bound within the polling driver. A device driver that does much polling interferes with I/O operations on other devices and can make the system slow and unresponsive to users.

Recently developed devices, which are as technologically advanced as the processors on which Windows is designed to run, seldom require a driver to poll its device, either to ensure that the device is ready to start an I/O operation or that an operation is complete.

Nevertheless, some devices still in use were designed to work with old processors, which had narrow data buses, slow clock rates, and single-user, single-tasking operating systems that did synchronous I/O. Such devices might require polling or some other means of waiting for the device to update its registers.

Although it might seem logical to solve a slow-device problem by coding a simple loop that increments a counter, thereby "wasting" a minimum interval while the device updates registers, such a driver is unlikely to be portable across Windows platforms. The loop counter maximum would require customization for each platform. Furthermore, if the driver is compiled with a good optimizing compiler, the compiler might remove the driver's counter variable and the loop(s) where it is incremented.

**Note**   Follow this implementation guideline if the driver must stall while the device hardware updates state:
A driver can call [**KeStallExecutionProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff553295) before it reads device registers. The driver should minimize the interval it stalls and should, in general, specify a stall interval no longer than 50 microseconds.

The granularity of a **KeStallExecutionProcessor** interval is one microsecond.

If the device frequently requires more than 50 microseconds to update state, consider setting up a [device-dedicated thread](device-dedicated-threads.md) in the driver.

 

 

 




