---
title: Types of APCs
description: Types of APCs
ms.assetid: 74ed953c-1b2a-40b9-9df3-16869b198b38
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "user APCs WDK kernel", "normal kernel APCs WDK kernel", "special kernel APCs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Types of APCs


An asynchronous procedure call (APC) is a function that executes asynchronously. APCs are similar to deferred procedure calls (DPCs), but unlike DPCs, APCs execute within the context of a particular thread. Drivers (other than file systems and file-system filter drivers) do not use APCs directly, but other parts of the operating system do, so you need to be aware of how APCs work.

The Windows operating system uses three kinds of APCs:

-   *User APCs* run strictly in user mode and only when the current thread is in an alertable wait state. The operating system uses user APCs to implement mechanisms such as overlapped I/O and the **QueueUserApc** Win32 routine.

-   *Normal kernel APCs* run in kernel mode at IRQL = PASSIVE\_LEVEL. A normal kernel APC preempts all user-mode code, including user APCs. Normal kernel APCs are generally used by file systems and file-system filter drivers.

-   *Special kernel APCs* run in kernel mode at IRQL = APC\_LEVEL. A special kernel APC preempts user-mode code and kernel-mode code that executes at IRQL = PASSIVE\_LEVEL, including both user APCs and normal kernel APCs. The operating system uses special kernel APCs to handle operations such as I/O request completion.

 

 




