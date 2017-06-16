---
title: Avoid Polling Devices
author: windows-driver-content
description: Avoid Polling Devices
ms.assetid: c50c9c6f-c8eb-4e52-854a-3ebc4fdc874c
keywords: ["I/O WDK kernel , device polling", "device polling WDK I/O", "polling devices WDK I/O", "loop counters WDK I/O", "counters WDK I/O"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Avoid Polling Devices


## <a href="" id="ddk-polling-a-device-kg"></a>


A device driver should avoid polling its device unless absolutely necessary, and should never use a whole time-slice for polling. Polling a device is an expensive operation that makes any operating system compute-bound within the polling driver. A device driver that does much polling interferes with I/O operations on other devices and can make the system slow and unresponsive to users.

Recently developed devices, which are as technologically advanced as the processors on which Windows is designed to run, seldom require a driver to poll its device, either to ensure that the device is ready to start an I/O operation or that an operation is complete.

Nevertheless, some devices still in use were designed to work with old processors, which had narrow data buses, slow clock rates, and single-user, single-tasking operating systems that did synchronous I/O. Such devices might require polling or some other means of waiting for the device to update its registers.

Although it might seem logical to solve a slow-device problem by coding a simple loop that increments a counter, thereby "wasting" a minimum interval while the device updates registers, such a driver is unlikely to be portable across Windows platforms. The loop counter maximum would require customization for each platform. Furthermore, if the driver is compiled with a good optimizing compiler, the compiler might remove the driver's counter variable and the loop(s) where it is incremented.

**Note**   Follow this implementation guideline if the driver must stall while the device hardware updates state:
A driver can call [**KeStallExecutionProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff553295) before it reads device registers. The driver should minimize the interval it stalls and should, in general, specify a stall interval no longer than 50 microseconds.

The granularity of a **KeStallExecutionProcessor** interval is one microsecond.

If the device frequently requires more than 50 microseconds to update state, consider setting up a [device-dedicated thread](device-dedicated-threads.md) in the driver.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Avoid%20Polling%20Devices%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


