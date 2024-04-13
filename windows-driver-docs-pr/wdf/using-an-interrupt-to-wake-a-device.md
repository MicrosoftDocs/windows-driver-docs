---
title: Using an Interrupt to Wake a Device
description: When a device transitions to a low-power state, the framework disconnects (or reports as inactive) interrupts that are used for I/O handling.
ms.date: 04/20/2017
---

# Using an Interrupt to Wake a Device


When a device transitions to a low-power state, the framework disconnects (or reports as inactive) interrupts that are used for I/O handling. Starting with KMDF 1.13 and UMDF 2.0 running on Windows 8.1, a WDF driver can create a framework interrupt object that remains active when the device transitions to a low-power state, and can then be used to awaken the device and restore it to its fully on D0 state.

If you are developing a WDF driver for a System on a Chip (SoC) platform, you can use such an interrupt to awaken a device that does not provide a traditional wake signaling mechanism. To use this functionality, the device must have hardware support for wake interrupts, as exposed through ACPI. The driver that creates the interrupt must be the device's power policy owner.

When the device transitions to a low-power state, the framework does not disconnect an interrupt that has been identified as wake-capable. When the device interrupts, the framework calls the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) and [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback routines at IRQL = PASSIVE\_LEVEL.

If your driver already creates a [passive-level interrupt object](supporting-passive-level-interrupts.md) for I/O handling, we recommend sharing that same interrupt object for wake functionality. In this scenario, the driver's [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback routine implements conditional logic to perform handling for I/O-related interrupts, as well as wake handling.

However, if your driver uses an interrupt that requires handling at the device's IRQL (DIRQL), we recommend creating an additional framework interrupt object to provide wake functionality.

Follow these steps to create a wake-capable interrupt object in your KMDF or UMDF driver:

1.  Call [**WdfDeviceAssignS0IdleSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassigns0idlesettings), typically from [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add), specifying **IdleCanWakeFromS0** in the *IdleCaps* parameter.
2.  Optionally, call [**WdfDeviceInitSetPowerPolicyEventCallbacks**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks) to register event callback functions described in [Supporting System Wake-Up](supporting-system-wake-up.md).
3.  Call [**WDF\_INTERRUPT\_CONFIG\_INIT**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdf_interrupt_config_init) to initialize a [**WDF\_INTERRUPT\_CONFIG**](/windows-hardware/drivers/ddi/wdfinterrupt/ns-wdfinterrupt-_wdf_interrupt_config) structure. Provide an [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback function, to be called at passive level. In the configuration structure, set **PassiveHandling** and **CanWakeDevice** to **TRUE**. Then call [**WdfInterruptCreate**](/windows-hardware/drivers/ddi/wdfinterrupt/nf-wdfinterrupt-wdfinterruptcreate) from your driver's [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function to create the framework interrupt object.
4.  Call [**WdfDeviceAssignSxWakeSettings**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceassignsxwakesettings) to configure the device to wake the system from a low-power state.
    ```cpp
    WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT(&wakeSettings);
    wakeSettings.DxState = PowerDeviceD3;
    wakeSettings.UserControlOfWakeSettings = WakeDoNotAllowUserControl;
    wakeSettings.Enabled = WdfTrue;

    status = WdfDeviceAssignSxWakeSettings(Device, &wakeSettings);
    if (!NT_SUCCESS(status)) {
        Trace(TRACE_LEVEL_ERROR,"WdfDeviceAssignSxWakeSettings failed %x\n", status);
        return status;
    }
    ```

5.  When the device transitions to a low-power state, the framework does not call [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) for the wake-capable interrupt. The framework does call [*EvtDeviceArmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0) if the driver has provided one.
6.  When the device signals the wake interrupt, the framework calls the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback routine.
7.  If the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback returns success, the framework calls the driver's [*EvtInterruptIsr*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_isr) callback at passive level. Before the interrupt handler returns, it must silence the interrupt in the interrupt controller. If the driver returns a failure code from *EvtDeviceD0Entry*, the framework disconnects the interrupt and calls the driver's [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback, if the driver has provided one.
8.  The framework calls the following wake event callback routines, if the driver has provided any:
    -   [*EvtDeviceDisarmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0)
    -   [*EvtDeviceDisarmWakeFromSx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx)
    -   [*EvtDeviceWakeFromS0Triggered*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_s0_triggered)
    -   [*EvtDeviceWakeFromSxTriggered*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_wake_from_sx_triggered)

9.  The framework continues with the normal power-up callback sequence, as described in [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md).

You can use the [**!wdfkd.wdfinterrupt**](../debuggercmds/-wdfkd-wdfinterrupt.md) debugger extension to show whether a specific interrupt has been configured to be wake-capable.

Wake interrupt functionality cannot be used in conjunction with USB selective suspend.

 

