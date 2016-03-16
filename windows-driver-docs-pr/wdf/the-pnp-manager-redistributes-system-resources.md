---
title: The PnP Manager Redistributes System Resources
description: The PnP Manager Redistributes System Resources
ms.assetid: fc88ae0a-5b78-4292-a101-29d2fc383555
keywords: ["PnP WDK KMDF redistributing resources", "Plug and Play WDK KMDF redistributing resources", "resource redistribution WDK KMDF", "redistributing resources WDK KMDF", "power down sequence WDK KMDF", "power up sequence WDK KMDF"]
---

# The PnP Manager Redistributes System Resources


If a user adds a device to a system, and if the device requires system resources that the PnP manager has already assigned to another device, the PnP manager attempts to reassign resources.

During this process, the PnP manager stops devices and takes them out of their working (D0) states. It then delivers new resource lists to the devices so that they can restart, using the new resources.

When redistributing resources, the PnP manager will not alter a device's resource assignment if one of the device's drivers has:

-   Called [**WdfDeviceSetSpecialFileSupport**](https://msdn.microsoft.com/library/windows/hardware/ff546903) and a special file is open on the device.

-   Called [**WdfDeviceSetStaticStopRemove**](https://msdn.microsoft.com/library/windows/hardware/ff546915).

-   Supplied an [*EvtDeviceQueryStop*](https://msdn.microsoft.com/library/windows/hardware/ff540885) callback function, and the callback function has vetoed the reassignment.

### Power-Down Sequence

For each function and filter driver that supports the device being stopped, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function.

2.  The framework stops all of the device's power-managed I/O queues.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541677), [*EvtDmaEnablerFlush*](https://msdn.microsoft.com/library/windows/hardware/ff541655), and [*EvtDmaEnablerDisable*](https://msdn.microsoft.com/library/windows/hardware/ff540927) callback functions for each DMA channel that was created.

4.  Calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) and [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback functions (if they exist) so that the driver can disable device interrupts.

5.  The framework calls the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function (if it exists).

6.  The framework calls the driver's [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function (if it exists) passing the list of hardware resources that the PnP manager has assigned to the device.

The bus driver is the lowest driver in the stack and is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function, it passes a handle to the framework device object representing the device's PDO and a *TargetState* value of **WdfPowerDeviceD3Final**. The bus driver can control when the framework calls its [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function by calling [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](https://msdn.microsoft.com/library/windows/hardware/hh706196).

### Power-Up Sequence

The first driver called is the bus driver. When the framework calls the bus driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function, the callback function restores the device (a child device of the bus) to its working (D0) state.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function (if it exists), passing the list of hardware resources that the PnP manager has assigned to the device.

2.  The framework calls the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function (if it exists).

3.  The framework calls the driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) and [*EvtDeviceD0EntryPostInterruptsEnabled*](https://msdn.microsoft.com/library/windows/hardware/ff540853) callback functions (if they exist) so that the driver can enable device interrupts.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](https://msdn.microsoft.com/library/windows/hardware/ff540932), [*EvtDmaEnablerEnable*](https://msdn.microsoft.com/library/windows/hardware/ff540929), and [*EvtDmaEnablerSelfManagedIoStart*](https://msdn.microsoft.com/library/windows/hardware/ff541663) callback functions for each DMA channel that was created.

5.  The framework calls the driver's [*EvtChildListScanForChildren*](https://msdn.microsoft.com/library/windows/hardware/ff540838) callback function (if it exists).

6.  The framework restarts all of the device's power-managed I/O queues.

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoRestart*](https://msdn.microsoft.com/library/windows/hardware/ff540905) callback function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20The%20PnP%20Manager%20Redistributes%20System%20Resources%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




