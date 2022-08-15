---
title: Canceling IRPs
description: Canceling IRPs
keywords: ["IRPs WDK kernel , canceling", "canceling IRPs", "Cancel routines", "user-canceled I/O requests WDK kernel", "completing IRPs WDK kernel , canceling IRPs", "unprocessed IRP cancellations WDK kernel"]
ms.date: 06/16/2017
---

# Canceling IRPs





Drivers in which IRPs might remain queued for an indefinite interval (so a user could cancel a previously submitted I/O request) must have one or more [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routines to complete user-canceled I/O requests. For example, keyboard, mouse, parallel, serial, and sound device drivers (or drivers layered over them) and file system drivers should have *Cancel* routines.

Drivers for Microsoft Windows XP and later operating systems can use [cancel-safe IRP queues](cancel-safe-irp-queues.md) rather than implement their own *Cancel* routines.

To "cancel an IRP" means to complete the IRP as quickly as possible while still maintaining system integrity. For a general discussion of IRP completion, see [Completing IRPs](completing-irps.md).

The cancellation process begins when either the system or a driver calls [**IoCancelIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp). This routine is called for each IRP that is associated with the thread that has not yet fully completed. The system cancels unprocessed IRPs if the thread that initiated the I/O request exits. Drivers can cancel only IRPs that they have created (see [Creating IRPs for Lower-Level Drivers](creating-irps-for-lower-level-drivers.md).)

If an IRP is not completed within 5 minutes, the I/O manager considers the IRP timed out. Such IRPs are disassociated from the thread, and an error is logged for the device that currently owns the IRP. You should ensure that any requests that might take a long time to complete in your driver are cancelable. To ensure that potentially long requests are cancelable, you can use [cancel-safe IRP queues](cancel-safe-irp-queues.md) or [Kernel-Mode Driver Framework](../wdf/index.md), which abstracts cancellation away from the driver developer.

This section provides the following topics:

[Introduction to Cancel Routines](introduction-to-cancel-routines.md)

[Registering a Cancel Routine](registering-a-cancel-routine.md)

[Synchronizing IRP Cancellation](synchronizing-irp-cancellation.md)

[Implementing a Cancel Routine](implementing-a-cancel-routine.md)

[Points to Consider When Canceling IRPs](points-to-consider-when-canceling-irps.md)

 

