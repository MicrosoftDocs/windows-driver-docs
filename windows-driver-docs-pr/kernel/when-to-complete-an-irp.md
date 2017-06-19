---
title: When to Complete an IRP
author: windows-driver-content
description: When to Complete an IRP
ms.assetid: 6986b24c-e7e5-43f2-861d-b84e4c131a8a
keywords: ["completing IRPs WDK kernel , when to complete"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# When to Complete an IRP


## <a href="" id="ddk-when-to-complete-an-irp-kg"></a>


A driver should initiate IRP completion when any of the following conditions is met:

-   The driver determines that IRP processing cannot progress because of invalid parameters or other conditions.

-   The driver is able to handle the requested I/O operation without passing the IRP down the driver stack, and the operation has finished.

-   The IRP is being canceled. (See [Canceling IRPs](canceling-irps.md).)

If these conditions are not met, a driver's dispatch routine must pass the IRP down to the next-lower driver, or it must handle processing of the I/O request. If one of the conditions is met, the driver must call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343).

If a driver completes a request because processing cannot progress, or if it completes a request by handling the requested operation without actually accessing the device, it typically calls **IoCompleteRequest** from one of its dispatch routines. For more information, see [Completing IRPs in Dispatch Routines](completing-irps-in-dispatch-routines.md).

If a driver must access a device to satisfy the request, it typically calls **IoCompleteRequest** from a [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine. These routines are discussed extensively in [Servicing Interrupts](servicing-interrupts.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20When%20to%20Complete%20an%20IRP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


