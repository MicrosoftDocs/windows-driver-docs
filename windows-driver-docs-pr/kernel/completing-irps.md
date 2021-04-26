---
title: Completing IRPs
description: Completing IRPs
keywords: ["IRPs WDK kernel , completing", "completing IRPs WDK kernel", "finished IRPs WDK kernel", "I/O WDK kernel , operation completed", "completing IRPs WDK kernel , about completing IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Completing IRPs





"Completing an IRP" is a shorthand phrase that means "allowing all members of the driver stack to complete an I/O operation." After the IRP has been completed, the I/O manager notifies the initiating application that the requested I/O operation has finished.

When a driver has finished processing an IRP, it calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) (typically from within a [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine). This causes the I/O manager to determine whether any higher-level drivers have set up [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routines for the IRP. If so, each *IoCompletion* routine is called, in turn, until every layered driver in the chain has completed the IRP.

When all drivers have completed the IRP, the I/O manager returns status to the original requester of the operation. Note that a higher-level driver that sets up a driver-created IRP must supply an *IoCompletion* routine to release the IRP it created.

This section contains the following topics:

[When to Complete an IRP](when-to-complete-an-irp.md)

[Completing IRPs in Dispatch Routines](how-to-complete-an-irp-in-a-dispatch-routine.md)

[Using IoCompletion Routines](using-iocompletion-routines.md)

 

