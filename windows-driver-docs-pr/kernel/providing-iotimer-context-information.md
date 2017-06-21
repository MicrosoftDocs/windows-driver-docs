---
title: Providing IoTimer Context Information
author: windows-driver-content
description: Providing IoTimer Context Information
ms.assetid: a92a7c3d-1602-430b-8ae1-c79bfc9ac7f9
keywords: ["IoTimer", "IoInitializeTimer"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Providing IoTimer Context Information


## <a href="" id="ddk-providing-iotimer-context-information-kg"></a>


The *Context* pointer passed to [**IoInitializeTimer**](https://msdn.microsoft.com/library/windows/hardware/ff549344) identifies a context area where other driver routines, and the [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine itself, can maintain state about timed operations. The I/O manager passes the *Context* pointer whenever it calls the *IoTimer* routine.

Because an *IoTimer* routine is run at IRQL = DISPATCH\_LEVEL, its context area must be in resident, system-space memory. Most drivers that have *IoTimer* routines use the [device extension](device-extensions.md) of the associated device object as a *Context*-accessible area, but the context can instead be in a controller extension if the driver uses a [controller object](using-controller-objects.md) or in nonpaged pool allocated by the driver.

**Follow these guidelines for an** *IoTimer***routine's context area:**

-   If the *IoTimer* routine shares its context area with the driver's ISR, it must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that accesses the context area in a multiprocessor-safe manner. For more information, see [Using Critical Sections](using-critical-sections.md).

-   If the *IoTimer* routine does not share its context area with an ISR, but does share it with another driver routine, the driver must protect the shared context area with an initialized executive spin lock, in order to access the context information in a multiprocessor-safe manner. For more information, see [Spin Locks](spin-locks.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Providing%20IoTimer%20Context%20Information%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


