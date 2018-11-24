---
title: Life Cycle of a Storport Driver
description: Life Cycle of a Storport Driver
ms.assetid: 6b48cf8e-83c3-4403-88fd-1bf1f285aafc
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Life Cycle of a Storport Driver


The life cycle of a Storport driver can be described in terms of the callback routines into the miniport driver from the Storport driver. The callback routines can be categorized into several main groups, as shown in Figure 1.

![figure illustrating overall storport architecture](images/storport-1.png)

Several examples of each type of callback routine are shown in Figure 2. When the system starts and the driver is first loaded, the miniport driver's **DriverEntry** routine is called. This routine fills out a data structure that provides Storport with the miniport driver's entry points, also known as its callback routines, or callbacks. Near the end of this routine, the miniport driver calls [**StorPortInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff567108). The Storport driver then calls the miniport callback routine [**HwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff557390), or in the case of a virtual miniport driver, [**VirtualHwStorFindAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff568008). After returning from that routine, the miniport driver's [**HwStorInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff557396) routine is called.

Storport then obtains the miniport driver's supported control types by calling its [**HwStorAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557365) routine with **ScsiQuerySupportedControlTypes** as a parameter.

![figure 2: storport callback routines](images/storport-2.png)

The main I/O path consists of a series of calls to [**HwStorBuildIo**](https://msdn.microsoft.com/library/windows/hardware/ff557369) (except in the case of a virtual miniport driver) and [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423). For more information, see [Unsynchronized HwStorBuildIo Routine](unsynchronized-hwstorbuildio-routine.md).

When the system is shutdown, [**HwStorStartIo**](https://msdn.microsoft.com/library/windows/hardware/ff557423) is called with an SRB of type SRB\_FUNCTION\_SHUTDOWN. When an adapter is removed or disabled while the system is running, or when the system is entering hibernate mode, [**HwStorAdapterControl**](https://msdn.microsoft.com/library/windows/hardware/ff557365) is called with **ScsiStopAdapter** as a parameter. When the system is resuming from hibernate mode, **HwStorAdapterControl** is called with **ScsiRestartAdapter** as a parameter.

 

 




