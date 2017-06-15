---
title: Writing a Bug Check Callback Routine
author: windows-driver-content
description: Writing a Bug Check Callback Routine
MS-HAID:
- 'Other\_fa98de4f-1264-4b2b-b0e2-0713d1de5422.xml'
- 'kernel.writing\_a\_bug\_check\_callback\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 62aefe67-e197-4c45-b994-19bd7369dbc1
keywords: ["bug check callback routines WDK kernel", "callback routines WDK bug checks", "registering callback routines", "KeRegisterBugCheckCallback", "BugCheckCallback"]
---

# Writing a Bug Check Callback Routine


## <a href="" id="ddk-writing-a-bug-check-callback-routine-kg"></a>


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

A driver's bug check callback routine can safely use the **READ\_PORT\_*XXX***, **READ\_REGISTER\_*XXX***, **WRITE\_PORT\_*XXX***, and **WRITE\_REGISTER\_*XXX*** routines to communicate with the driver's device. (For information about these routines, see [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644).)

For more information about bug check callbacks, see [*BugCheckCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540674), [*BugCheckAddPagesCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540669), [*BugCheckDumpIoCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540677), [*BugCheckSecondaryDumpDataCallback*](https://msdn.microsoft.com/library/windows/hardware/ff540679), and [Reading Bug Check Callback Data](https://msdn.microsoft.com/library/windows/hardware/ff553558).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20a%20Bug%20Check%20Callback%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


