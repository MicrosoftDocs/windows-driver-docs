---
title: Writing SynchCritSection Routines
description: Writing SynchCritSection Routines
keywords: ["SynchCritSection", "critical section routines WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing SynchCritSection Routines





Drivers use their [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routines for either of two basic purposes:

[Programming a device for an I/O operation](programming-a-device-for-an-i-o-operation.md)

[Accessing shared state information](accessing-shared-state-information.md)

Like an ISR, a *SynchCritSection* routine must execute as quickly as possible, doing only what is necessary to set up device registers or update context data, before returning.

Because [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) holds a device driver's interrupt spin lock while its *SynchCritSection* routine runs, the driver's ISR cannot execute until the *SynchCritSection* routine returns control.

For any received IRP, a device driver should do as much I/O processing as possible either at IRQL PASSIVE\_LEVEL in its dispatch routines (or possibly [device-dedicated threads](device-dedicated-threads.md)), or at IRQL DISPATCH\_LEVEL in its [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine and DPC routines.

For additional information about how critical sections are synchronized, see [Using Spin Locks: An Example](using-spin-locks--an-example.md).

 

