---
title: Dispatch Routines and IRQLs
description: Dispatch Routines and IRQLs
ms.assetid: fe64e0f7-3906-470a-86c5-03460e652eed
keywords: ["dispatch routines WDK kernel , IRQLs", "IRQLs WDK dispatch routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Dispatch Routines and IRQLs





Most drivers' dispatch routines are called in an arbitrary thread context at IRQL = PASSIVE\_LEVEL, with the following exceptions:

-   Any highest-level driver's dispatch routines are called in the context of the thread that originated the I/O request, which is commonly a user-mode application thread.

    In other words, the dispatch routines of file system drivers and other highest-level drivers are called in a nonarbitrary thread context at IRQL = PASSIVE\_LEVEL.

-   The [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376), [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034), and [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routines of lowest-level device drivers, and of intermediate drivers layered above them in the system paging path, can be called at IRQL = APC\_LEVEL and in an arbitrary thread context.

    The *DispatchRead* and/or *DispatchWrite* routines, and any other routine that also processes read and/or write requests in such a lowest-level device or intermediate driver, must be resident at all times. These driver routines can neither be pageable nor be part of a driver's pageable-image section; they must not access any pageable memory. Furthermore, they should not be dependent on any blocking calls (such as [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) with a nonzero time-out).

-   The [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine of drivers in the hibernation and/or paging paths can be called at IRQL = DISPATCH\_LEVEL. The [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routines of such drivers must be prepared to handle PnP [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](https://msdn.microsoft.com/library/windows/hardware/ff550841) requests.

-   The *DispatchPower* routine of drivers that require inrush power at start-up can be called at IRQL = DISPATCH\_LEVEL.

For additional information, see [Managing Hardware Priorities](managing-hardware-priorities.md).

 

 




