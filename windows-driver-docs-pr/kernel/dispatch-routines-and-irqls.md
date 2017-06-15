---
title: Dispatch Routines and IRQLs
author: windows-driver-content
description: Dispatch Routines and IRQLs
MS-HAID:
- 'DrvComps\_ad832782-3e63-409b-ba57-d4451978c135.xml'
- 'kernel.dispatch\_routines\_and\_irqls'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: fe64e0f7-3906-470a-86c5-03460e652eed
keywords: ["dispatch routines WDK kernel , IRQLs", "IRQLs WDK dispatch routines"]
---

# Dispatch Routines and IRQLs


## <a href="" id="ddk-dispatch-routines-and-irqls-kg"></a>


Most drivers' dispatch routines are called in an arbitrary thread context at IRQL = PASSIVE\_LEVEL, with the following exceptions:

-   Any highest-level driver's dispatch routines are called in the context of the thread that originated the I/O request, which is commonly a user-mode application thread.

    In other words, the dispatch routines of file system drivers and other highest-level drivers are called in a nonarbitrary thread context at IRQL = PASSIVE\_LEVEL.

-   The [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376), [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034), and [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routines of lowest-level device drivers, and of intermediate drivers layered above them in the system paging path, can be called at IRQL = APC\_LEVEL and in an arbitrary thread context.

    The *DispatchRead* and/or *DispatchWrite* routines, and any other routine that also processes read and/or write requests in such a lowest-level device or intermediate driver, must be resident at all times. These driver routines can neither be pageable nor be part of a driver's pageable-image section; they must not access any pageable memory. Furthermore, they should not be dependent on any blocking calls (such as [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) with a nonzero time-out).

-   The [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine of drivers in the hibernation and/or paging paths can be called at IRQL = DISPATCH\_LEVEL. The [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routines of such drivers must be prepared to handle PnP [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) requests.

-   The *DispatchPower* routine of drivers that require inrush power at start-up can be called at IRQL = DISPATCH\_LEVEL.

For additional information, see [Managing Hardware Priorities](managing-hardware-priorities.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Dispatch%20Routines%20and%20IRQLs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


