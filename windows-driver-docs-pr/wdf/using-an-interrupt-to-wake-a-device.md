---
title: Using an Interrupt to Wake a Device
author: windows-driver-content
description: When a device transitions to a low-power state, the framework disconnects (or reports as inactive) interrupts that are used for I/O handling.
ms.assetid: 6A4E62BD-B10F-4F01-B4B4-1FF5086710D4
---

# Using an Interrupt to Wake a Device


When a device transitions to a low-power state, the framework disconnects (or reports as inactive) interrupts that are used for I/O handling. Starting with KMDF 1.13 and UMDF 2.0 running on Windows 8.1, a WDF driver can create a framework interrupt object that remains active when the device transitions to a low-power state, and can then be used to awaken the device and restore it to its fully on D0 state.

If you are developing a WDF driver for a System on a Chip (SoC) platform, you can use such an interrupt to awaken a device that does not provide a traditional wake signaling mechanism. To use this functionality, the device must have hardware support for wake interrupts, as exposed through ACPI. The driver that creates the interrupt must be the device's power policy owner.

When the device transitions to a low-power state, the framework does not disconnect an interrupt that has been identified as wake-capable. When the device interrupts, the framework calls the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) and [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback routines at IRQL = PASSIVE\_LEVEL.

If your driver already creates a [passive-level interrupt object](supporting-passive-level-interrupts.md) for I/O handling, we recommend sharing that same interrupt object for wake functionality. In this scenario, the driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback routine implements conditional logic to perform handling for I/O-related interrupts, as well as wake handling.

However, if your driver uses an interrupt that requires handling at the device's IRQL (DIRQL), we recommend creating an additional framework interrupt object to provide wake functionality.

Follow these steps to create a wake-capable interrupt object in your KMDF or UMDF driver:

1.  Call [**WdfDeviceAssignS0IdleSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545903), typically from [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693), specifying **IdleCanWakeFromS0** in the *IdleCaps* parameter.
2.  Optionally, call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](https://msdn.microsoft.com/library/windows/hardware/ff546774) to register event callback functions described in [Supporting System Wake-Up](supporting-system-wake-up.md).
3.  Call [**WDF\_INTERRUPT\_CONFIG\_INIT**](https://msdn.microsoft.com/library/windows/hardware/ff552348) to initialize a [**WDF\_INTERRUPT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552347) structure. Provide an [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, to be called at passive level. In the configuration structure, set **PassiveHandling** and **CanWakeDevice** to **TRUE**. Then call [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) from your driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function to create the framework interrupt object.
4.  Call [**WdfDeviceAssignSxWakeSettings**](https://msdn.microsoft.com/library/windows/hardware/ff545909) to configure the device to wake the system from a low-power state.
    ```
    WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT(&amp;wakeSettings);
    wakeSettings.DxState = PowerDeviceD3;
    wakeSettings.UserControlOfWakeSettings = WakeDoNotAllowUserControl;
    wakeSettings.Enabled = WdfTrue;

    status = WdfDeviceAssignSxWakeSettings(Device, &amp;wakeSettings);
    if (!NT_SUCCESS(status)) {
        Trace(TRACE_LEVEL_ERROR,"WdfDeviceAssignSxWakeSettings failed %x\n", status);
        return status;
    }
    ```

5.  When the device transitions to a low-power state, the framework does not call [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) for the wake-capable interrupt. The framework does call [*EvtDeviceArmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540843) if the driver has provided one.
6.  When the device signals the wake interrupt, the framework calls the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback routine.
7.  If the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback returns success, the framework calls the driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback at passive level. Before the interrupt handler returns, it must silence the interrupt in the interrupt controller. If the driver returns a failure code from *EvtDeviceD0Entry*, the framework disconnects the interrupt and calls the driver's [*EvtInterruptDisable*](https://msdn.microsoft.com/library/windows/hardware/ff541714) callback, if the driver has provided one.
8.  The framework calls the following wake event callback routines, if the driver has provided any:
    -   [*EvtDeviceDisarmWakeFromS0*](https://msdn.microsoft.com/library/windows/hardware/ff540860)
    -   [*EvtDeviceDisarmWakeFromSx*](https://msdn.microsoft.com/library/windows/hardware/ff540862)
    -   [*EvtDeviceWakeFromS0Triggered*](https://msdn.microsoft.com/library/windows/hardware/ff540919)
    -   [*EvtDeviceWakeFromSxTriggered*](https://msdn.microsoft.com/library/windows/hardware/ff540923)

9.  The framework continues with the normal power-up callback sequence, as described in [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md).

You can use the [**!wdfkd.wdfinterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff565787) debugger extension to show whether a specific interrupt has been configured to be wake-capable.

Wake interrupt functionality cannot be used in conjunction with USB selective suspend.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20an%20Interrupt%20to%20Wake%20a%20Device%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




