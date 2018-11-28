---
title: When to Complete an IRP
description: When to Complete an IRP
ms.assetid: 6986b24c-e7e5-43f2-861d-b84e4c131a8a
keywords: ["completing IRPs WDK kernel , when to complete"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When to Complete an IRP





A driver should initiate IRP completion when any of the following conditions is met:

-   The driver determines that IRP processing cannot progress because of invalid parameters or other conditions.

-   The driver is able to handle the requested I/O operation without passing the IRP down the driver stack, and the operation has finished.

-   The IRP is being canceled. (See [Canceling IRPs](canceling-irps.md).)

If these conditions are not met, a driver's dispatch routine must pass the IRP down to the next-lower driver, or it must handle processing of the I/O request. If one of the conditions is met, the driver must call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

If a driver completes a request because processing cannot progress, or if it completes a request by handling the requested operation without actually accessing the device, it typically calls **IoCompleteRequest** from one of its dispatch routines. For more information, see [Completing IRPs in Dispatch Routines](completing-irps-in-dispatch-routines.md).

If a driver must access a device to satisfy the request, it typically calls **IoCompleteRequest** from a [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine. These routines are discussed extensively in [Servicing Interrupts](servicing-interrupts.md).

 

 




