---
title: Completing IRPs
author: windows-driver-content
description: Completing IRPs
MS-HAID:
- 'IRPs\_5d4f9020-8fa8-4057-8a4d-ab00a50eb6b2.xml'
- 'kernel.completing\_irps'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4b4be95e-ebf5-4726-87fc-20c3e6c94f52
keywords: ["IRPs WDK kernel , completing", "completing IRPs WDK kernel", "finished IRPs WDK kernel", "I/O WDK kernel , operation completed", "completing IRPs WDK kernel , about completing IRPs"]
---

# Completing IRPs


## <a href="" id="ddk-completing-irps-kg"></a>


"Completing an IRP" is a shorthand phrase that means "allowing all members of the driver stack to complete an I/O operation." After the IRP has been completed, the I/O manager notifies the initiating application that the requested I/O operation has finished.

When a driver has finished processing an IRP, it calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) (typically from within a [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine). This causes the I/O manager to determine whether any higher-level drivers have set up [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines for the IRP. If so, each *IoCompletion* routine is called, in turn, until every layered driver in the chain has completed the IRP.

When all drivers have completed the IRP, the I/O manager returns status to the original requester of the operation. Note that a higher-level driver that sets up a driver-created IRP must supply an *IoCompletion* routine to release the IRP it created.

This section contains the following topics:

[When to Complete an IRP](when-to-complete-an-irp.md)

[Completing IRPs in Dispatch Routines](completing-irps-in-dispatch-routines.md)

[Using IoCompletion Routines](using-iocompletion-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Completing%20IRPs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


