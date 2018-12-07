---
title: A Device Returns to Its Working State
description: A Device Returns to Its Working State
ms.assetid: 0a5bdaf5-ed9e-44d0-bc8a-876ceb342520
keywords:
- device power states WDK KMDF
- working states WDK KMDF
- power states WDK KMDF
- system wake-up WDK KMDF
- power management WDK KMDF , wake-up capabilities
- wake-up capabilities WDK KMDF
- sleep power management WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A Device Returns to Its Working State


A device that is in a low-power state returns to its working state if one of the following occurs:

-   The device detects an external event and triggers a wake signal on its bus. The bus driver that detects the wake signal calls [**WdfDeviceIndicateWakeStatus**](https://msdn.microsoft.com/library/windows/hardware/ff546025). As a result, the framework calls the bus driver's [*EvtDeviceDisableWakeAtBus*](https://msdn.microsoft.com/library/windows/hardware/ff540858) callback function.

-   The device has been idle and a driver calls [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921).

-   The system's power state has changed from a low-power state to its working (S0) state.

In each of these situations, the framework calls the bus driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function, which then restores the device (a child device of the bus) to its working (D0) state.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function (if it exists).

2.  The framework calls the driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) callback function (if it exists) for each interrupt, and then it calls the driver's [*EvtDeviceD0EntryPostInterruptsEnabled*](https://msdn.microsoft.com/library/windows/hardware/ff540853) callback function (if it exists), so that the driver can enable device interrupts.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](https://msdn.microsoft.com/library/windows/hardware/ff540932), [*EvtDmaEnablerEnable*](https://msdn.microsoft.com/library/windows/hardware/ff540929), and [*EvtDmaEnablerSelfManagedIoStart*](https://msdn.microsoft.com/library/windows/hardware/ff541663) callback functions (if they exist) for each DMA channel that was created.

4.  If the driver is the device's power policy owner, the framework calls its [*EvtDeviceDisarmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540860) or [*EvtDeviceDisarmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540862) callback function.

5.  The framework calls the driver's [*EvtChildListScanForChildren*](https://msdn.microsoft.com/library/windows/hardware/ff540838) callback function (if it exists).

6.  The framework restarts all of the driver's power-managed I/O queues and calls their [*EvtIoResume*](https://msdn.microsoft.com/library/windows/hardware/ff541779) callback functions (if necessary).

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoRestart*](https://msdn.microsoft.com/library/windows/hardware/ff540905) callback function.

 

 





