---
title: Writing a Bug Check Callback Routine
description: Writing a Bug Check Callback Routine
ms.assetid: 62aefe67-e197-4c45-b994-19bd7369dbc1
keywords: ["bug check callback routines WDK kernel", "callback routines WDK bug checks", "registering callback routines", "KeRegisterBugCheckCallback", "BugCheckCallback"]
ms.date: 04/25/2019
ms.localizationpriority: medium
---

# Writing a Bug Check Callback Routine

Drivers can register callback routines that the system executes when it issues a bug check. Drivers can use a bug check callback routine to reset their device to a known state.

In Windows the system calls the [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function after the crash dump file is written. A [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://msdn.microsoft.com/library/windows/hardware/ff540679) routine can be used to write secondary data to the crash dump file.
 
A driver can implement a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine) routine to add pages of driver-specific data to the crash dump file. 

Drivers use the [**KeRegisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keregisterbugcheckcallback) and [**KeDeregisterBugCheckReasonCallback**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kederegisterbugcheckcallback) routines to register these three types of *BugCheckXxxCallback* callback routines.

A bug check callback routine executes at IRQL = HIGH\_LEVEL, which imposes strong restrictions on what it can do.

A bug check callback routine cannot:

- Allocate memory

- Access pageable memory

- Use any synchronization mechanisms

- Call any routine that must execute at IRQL = DISPATCH\_LEVEL or below

Bug check callback routines are guaranteed to run without interruption, so no synchronization is required. (If the bug check routine does use any synchronization mechanisms, the system will deadlock.)

A driver's bug check callback routine can safely use the <strong>READ\_PORT\_*XXX</strong><em>, **READ\_REGISTER\_</em>XXX<strong><em>, *</em>WRITE\_PORT\_*XXX</strong><em>, and **WRITE\_REGISTER\_</em>XXX*** routines to communicate with the driver's device. (For information about these routines, see [Hardware Abstraction Layer Routines](https://msdn.microsoft.com/library/windows/hardware/ff546644).)

For more information about bug check callbacks, see:
- [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine) 
- [*KBUGCHECK_CALLBACK_REASON enumeration*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ne-wdm-_kbugcheck_callback_reason)
- [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nc-wdm-kbugcheck_reason_callback_routine)
- [*KBUGCHECK_ADD_PAGES structure*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_kbugcheck_add_pages)
- [Reading Bug Check Callback Data](https://docs.microsoft.com/windows-hardware/drivers/debugger/reading-bug-check-callback-data)

 