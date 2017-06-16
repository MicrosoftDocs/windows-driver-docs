---
title: Thread Priorities
author: windows-driver-content
description: Thread Priorities
ms.assetid: 87a9641c-0569-45c1-acb8-adf5856dc60d
keywords: ["thread objects WDK kernel", "thread priorities WDK kernel", "priorities WDK threads"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Thread Priorities


## <a href="" id="ddk-thread-priorities-kg"></a>


Some drivers create their own driver- or device-dedicated system threads and set their thread's base priority to the lowest real-time priority value. Other highest-level drivers, particularly file system drivers, use system worker threads with a base priority that is usually set to the highest variable priority value. The kernel schedules a thread with the lowest real-time priority to run ahead of every thread with a variable priority, which includes almost every user-mode thread in the system.

Most standard driver routines are run in an arbitrary thread context, ahead of all threads that are currently in the ready state.

Threads, whatever their respective run-time priorities, are run at IRQL = PASSIVE\_LEVEL. Many standard driver routines are run at an IRQL &gt; PASSIVE\_LEVEL, such as DISPATCH\_LEVEL or DIRQL.

For more information about thread priorities, see the [Scheduling, Thread Context, and IRQL](http://go.microsoft.com/fwlink/p/?linkid=59757) white paper that is available on the Microsoft Windows Hardware Developer Central (WHDC) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Thread%20Priorities%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


