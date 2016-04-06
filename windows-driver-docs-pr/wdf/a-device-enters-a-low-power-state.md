---
title: A Device Enters a Low-Power State
description: A Device Enters a Low-Power State
ms.assetid: 07d7c460-4316-40a9-b502-f7c1bd1182c2
keywords: ["power management WDK KMDF , low-power states", "low-power states WDK KMDF", "power states WDK KMDF", "device power states WDK KMDF", "sleep power management WDK KMDF", "idle power-down WDK KMDF", "power management WDK KMDF , idle power-down", "system sleeping states WDK KMDF"]
---

# A Device Enters a Low-Power State


A device leaves its working (D0) state and enters a low-power state if one of the following occurs:

-   The device is idle (that is, not being accessed) and is capable of entering a low-power idle state while the system remains in its working (S0) state.

-   The system's power state has changed from its working (S0) state to a low-power state. (Drivers can call [**WdfDeviceGetSystemPowerAction**](https://msdn.microsoft.com/library/windows/hardware/ff546022) to determine the reason that a system's power state is changing.)

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](https://msdn.microsoft.com/library/windows/hardware/ff540907) callback function.

2.  The framework stops all of the driver's power-managed I/O queues and calls their [*EvtIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541788) callback functions (if they exist).

3.  If the driver is the device's power policy owner, the framework calls its [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843), [*EvtDeviceArmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540844), or [*EvtDeviceArmWakeFromSxWithReason*](https://msdn.microsoft.com/library/windows/hardware/ff540846) callback function.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](https://msdn.microsoft.com/library/windows/hardware/ff541677), [*EvtDmaEnablerFlush*](https://msdn.microsoft.com/library/windows/hardware/ff541655), and [*EvtDmaEnablerDisable*](https://msdn.microsoft.com/library/windows/hardware/ff540927) callback functions (if they exist) for each DMA channel created.

5.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](https://msdn.microsoft.com/library/windows/hardware/ff540856) callback function (if it exists), and then it calls the driver's [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback function (if it exists) for each interrupt, so that the driver can disable device interrupts.

6.  The framework calls the driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function (if it exists).

The bus driver is the driver in the stack that is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](https://msdn.microsoft.com/library/windows/hardware/ff540855) callback function, the callback function sets the power state of the device (a child device of the bus) to a low-power state. The framework specifies the D3 low-power state unless the power policy owner has specified a different low-power state.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20A%20Device%20Enters%20a%20Low-Power%20State%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




