---
title: Thread Priorities
description: Thread Priorities
ms.assetid: 87a9641c-0569-45c1-acb8-adf5856dc60d
keywords: ["thread objects WDK kernel", "thread priorities WDK kernel", "priorities WDK threads"]
ms.date: 05/08/2018
ms.localizationpriority: medium
---

# Thread Priorities





Some drivers create their own driver- or device-dedicated system threads and set their thread's base priority to the lowest real-time priority value. Other highest-level drivers, particularly file system drivers, use system worker threads with a base priority that is usually set to the highest variable priority value. The kernel schedules a thread with the lowest real-time priority to run ahead of every thread with a variable priority, which includes almost every user-mode thread in the system.

Most standard driver routines are run in an arbitrary thread context, ahead of all threads that are currently in the ready state.

Threads, whatever their respective run-time priorities, are run at IRQL = PASSIVE\_LEVEL. Many standard driver routines are run at an IRQL &gt; PASSIVE\_LEVEL, such as DISPATCH\_LEVEL or DIRQL.

For more information about thread priorities, see the [Scheduling, Thread Context, and IRQL](http://go.microsoft.com/fwlink/p/?linkid=59757) white paper.

 

 




