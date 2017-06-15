---
title: Canceling IRPs
author: windows-driver-content
description: Canceling IRPs
MS-HAID:
- 'IRPs\_0389dd54-106e-487d-bab3-0cb681377bc7.xml'
- 'kernel.canceling\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: da199435-f6c3-44f4-b1ed-0280f39ee452
keywords: ["IRPs WDK kernel , canceling", "canceling IRPs", "Cancel routines", "user-canceled I/O requests WDK kernel", "completing IRPs WDK kernel , canceling IRPs", "unprocessed IRP cancellations WDK kernel"]
---

# Canceling IRPs


## <a href="" id="ddk-canceling-irps-kg"></a>


Drivers in which IRPs might remain queued for an indefinite interval (so a user could cancel a previously submitted I/O request) must have one or more [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routines to complete user-canceled I/O requests. For example, keyboard, mouse, parallel, serial, and sound device drivers (or drivers layered over them) and file system drivers should have *Cancel* routines.

Drivers for Microsoft Windows XP and later operating systems can use [cancel-safe IRP queues](cancel-safe-irp-queues.md) rather than implement their own *Cancel* routines.

To "cancel an IRP" means to complete the IRP as quickly as possible while still maintaining system integrity. For a general discussion of IRP completion, see [Completing IRPs](completing-irps.md).

The cancellation process begins when either the system or a driver calls [**IoCancelIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548338). This routine is called for each IRP that is associated with the thread that has not yet fully completed. The system cancels unprocessed IRPs if the thread that initiated the I/O request exits. Drivers can cancel only IRPs that they have created (see [Creating IRPs for Lower-Level Drivers](creating-irps-for-lower-level-drivers.md).)

If an IRP is not completed within 5 minutes, the I/O manager considers the IRP timed out. Such IRPs are disassociated from the thread, and an error is logged for the device that currently owns the IRP. You should ensure that any requests that might take a long time to complete in your driver are cancelable. To ensure that potentially long requests are cancelable, you can use [cancel-safe IRP queues](cancel-safe-irp-queues.md) or [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/dn265580), which abstracts cancellation away from the driver developer.

This section provides the following topics:

[Introduction to Cancel Routines](introduction-to-cancel-routines.md)

[Registering a Cancel Routine](registering-a-cancel-routine.md)

[Synchronizing IRP Cancellation](synchronizing-irp-cancellation.md)

[Implementing a Cancel Routine](implementing-a-cancel-routine.md)

[Points to Consider When Canceling IRPs](points-to-consider-when-canceling-irps.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Canceling%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


