---
title: IoCompletion Routines for Wait/Wake IRPs
description: IoCompletion Routines for Wait/Wake IRPs
keywords: ["receiving wait/wake IRPs", "wait/wake IRPs WDK power management , receiving", "IoCompletion routines"]
ms.date: 06/16/2017
---

# IoCompletion Routines for Wait/Wake IRPs





The I/O manager calls a driver's wait/wake [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine after the next-lower driver in the device stack has completed the wait/wake IRP. Each function and filter (FDO) driver that handles a wait/wake IRP should set an *IoCompletion* routine for the IRP.

Each function or filter driver sets an *IoCompletion* routine as it handles the wait/wake IRP on its way down the device stack. The device power policy owner, which sends the IRP, might therefore have an *IoCompletion* routine in addition to a callback routine. Keep in mind that the callback routine is invoked after the *IoCompletion* routine and that the two have different requirements. For more information, see [Wait/Wake Callback Routines](wait-wake-callback-routines.md).

The actions required in a wait/wake *IoCompletion* routine depend on the device and the type of driver. The following are some actions a driver might need to perform in its wait/wake *IoCompletion* routine:

1.  Reset any relevant fields in the device extension. For example, when a wait/wake IRP is pending, most drivers set a flag and keep a pointer to the IRP in the device extension.

2.  Reset the [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine, if any, for the IRP by calling [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine), specifying a **NULL** pointer for the routine.

3.  Call **IoCompleteRequest**, specifying IO\_NO\_INCREMENT, to complete the IRP.

As each successive driver completes the IRP, the I/O manager passes control to the *IoCompletion* routine of the next-higher driver going back up the stack.

After calling the *IoCompletion* routines set by drivers as they passed the wait/wake IRP down the device stack, the I/O manager calls the callback routine passed to [**PoRequestPowerIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-porequestpowerirp) by the driver that sent the IRP. For further information, see [Wait/Wake Callback Routines](wait-wake-callback-routines.md).

 

