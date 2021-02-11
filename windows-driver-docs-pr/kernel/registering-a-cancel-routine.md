---
title: Registering a Cancel Routine
description: Registering a Cancel Routine
keywords: ["canceling IRPs, registering Cancel routines", "Cancel routines, registering", "registering Cancel routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering a Cancel Routine





If a device driver has a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, its dispatch routines can register a [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine by supplying its address as input to [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket).

If a driver does not have a *StartIo* routine, its dispatch routines must do the following before queuing an IRP for further processing by other driver routines:

1.  Call [**IoAcquireCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff548196(v=vs.85)).

2.  Call [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) with the input IRP and the entry point for a driver-supplied *Cancel* routine.

3.  Call [**IoReleaseCancelSpinLock**](/previous-versions/windows/hardware/drivers/ff549550(v=vs.85)).

For information about the cancel spin lock, see [Using the System's Cancel Spin Lock](using-the-system-s-cancel-spin-lock.md).

Drivers that manage their own queues of IRPs, rather than using the I/O manager-supplied device queue, do not need to acquire the cancel spin lock when calling **IoSetCancelRoutine**. However, these drivers should check the *Cancel* routine pointer that **IoSetCancelRoutine** returns to determine whether the *Cancel* routine has already started.

 

