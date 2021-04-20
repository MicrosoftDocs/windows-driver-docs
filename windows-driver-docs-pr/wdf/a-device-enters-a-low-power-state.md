---
title: A Device Enters a Low-Power State
description: Learn what happens to a device when it enters a low-power state. For example, when a device is idle while the system is still in its working state.
keywords:
- power management WDK KMDF , low-power states
- low-power states WDK KMDF
- power states WDK KMDF
- device power states WDK KMDF
- sleep power management WDK KMDF
- idle power-down WDK KMDF
- power management WDK KMDF , idle power-down
- system sleeping states WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A Device Enters a Low-Power State


A device leaves its working (D0) state and enters a low-power state if one of the following occurs:

-   The device is idle (that is, not being accessed) and is capable of entering a low-power idle state while the system remains in its working (S0) state.

-   The system's power state has changed from its working (S0) state to a low-power state. (Drivers can call [**WdfDeviceGetSystemPowerAction**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicegetsystempoweraction) to determine the reason that a system's power state is changing.)

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) callback function.

2.  The framework stops all of the driver's power-managed I/O queues and calls their [*EvtIoStop*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_stop) callback functions (if they exist).

3.  If the driver is the device's power policy owner, the framework calls its [*EvtDeviceArmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_s0), [*EvtDeviceArmWakeFromSx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx), or [*EvtDeviceArmWakeFromSxWithReason*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_arm_wake_from_sx_with_reason) callback function.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop), [*EvtDmaEnablerFlush*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush), and [*EvtDmaEnablerDisable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable) callback functions (if they exist) for each DMA channel created.

5.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) callback function (if it exists), and then it calls the driver's [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback function (if it exists) for each interrupt, so that the driver can disable device interrupts.

6.  The framework calls the driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function (if it exists).

The bus driver is the driver in the stack that is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function, the callback function sets the power state of the device (a child device of the bus) to a low-power state. The framework specifies the D3 low-power state unless the power policy owner has specified a different low-power state.

> [!NOTE]
> The method used by the bus driver to set the power state of the child device is bus-specific. For example, the PCI bus power management specification defines a 16-bit Power Management Control / Status register (PMCSR). The lowest two bits ("PowerState") both determine the current power state of the device and are used to set the device into a new power state. When the `pci.sys` PDO receives IRP_MN_SET_POWER/D3, it reads the PMCSR, changes the PowerState bits to 11b (power level D3), and writes back the PMCSR.

