---
title: A Device Returns to Its Working State
description: A Device Returns to Its Working State
ms.assetid: 0a5bdaf5-ed9e-44d0-bc8a-876ceb342520
keywords: ["device power states WDK KMDF", "working states WDK KMDF", "power states WDK KMDF", "system wake-up WDK KMDF", "power management WDK KMDF , wake-up capabilities", "wake-up capabilities WDK KMDF", "sleep power management WDK KMDF"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20A%20Device%20Returns%20to%20Its%20Working%20State%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




