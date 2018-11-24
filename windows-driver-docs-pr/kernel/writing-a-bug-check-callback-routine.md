---
title: Writing a Bug Check Callback Routine
description: Writing a Bug Check Callback Routine
ms.assetid: 62aefe67-e197-4c45-b994-19bd7369dbc1
keywords: ["bug check callback routines WDK kernel", "callback routines WDK bug checks", "registering callback routines", "KeRegisterBugCheckCallback", "BugCheckCallback"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing a Bug Check Callback Routine





Drivers can register callback routines that the system executes when it issues a bug check.

On all NT-based operating systems, drivers can use the [**KeRegisterBugCheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553105) routine to register a [*BugCheckCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540674) routine, and [**KeDeregisterBugCheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff551992) to remove the routine. Drivers can use a *BugCheckCallback* routine to reset their device to a known state.

Prior to Windows XP Service Pack 1 (SP1) and Windows Server 2003, drivers could also use *BugCheckCallback* to store data in the crash dump file: the system called each *BugCheckCallback* routine before writing the crash dump file, so any data written to the buffer that was passed to *BugCheckCallback* was stored in the crash dump file.

In Windows XP SP1 and Windows Server 2003 and later, the system calls *BugCheckCallback*after the crash dump file is written. Instead, the system supports two additional types of bug check callback routines. A [*BugCheckSecondaryDumpDataCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540679) routine can be used to write secondary data to the crash dump file. A [*BugCheckDumpIoCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540677) routine can be used to copy the crash dump file to a device.

In Windows Server 2008 and later versions of Windows, a driver can implement a [*BugCheckAddPagesCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540669) routine to add pages of driver-specific data to the crash dump file. Unlike a *BugCheckSecondaryDumpDataCallback* routine, which appends data to the secondary crash dump region, a *BugCheckAddPagesCallback* routine adds pages of data to the crash dump region. During debugging, crash dump data is easier to access than secondary crash dump data.

Drivers use the [**KeRegisterBugCheckReasonCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553110) and [**KeDeregisterBugCheckReasonCallback**](https://msdn.microsoft.com/library/windows/hardware/ff552003) routines to register these three types of *BugCheckXxxCallback* callback routines.

A bug check callback routine executes at IRQL = HIGH\_LEVEL, which imposes strong restrictions on what it can do.

A bug check callback routine cannot:

-   Allocate memory

-   Access pageable memory

-   Use any synchronization mechanisms

-   Call any routine that must execute at IRQL = DISPATCH\_LEVEL or below

Bug check callback routines are guaranteed to run without interruption, so no synchronization is required. (If the bug check routine does use any synchronization mechanisms, the system will deadlock.)

A driver's bug check callback routine can safely use the <strong>READ\_PORT\_*XXX</strong><em>, **READ\_REGISTER\_</em>XXX<strong><em>, *</em>WRITE\_PORT\_*XXX</strong><em>, and **WRITE\_REGISTER\_</em>XXX*** routines to communicate with the driver's device. (For information about these routines, see [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644).)

For more information about bug check callbacks, see [*BugCheckCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540674), [*BugCheckAddPagesCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540669), [*BugCheckDumpIoCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540677), [*BugCheckSecondaryDumpDataCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540679), and [Reading Bug Check Callback Data](https://msdn.microsoft.com/library/windows/hardware/ff553558).

 

 




