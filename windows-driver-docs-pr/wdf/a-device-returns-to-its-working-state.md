---
title: A Device Returns to Its Working State
description: Learn what happens when a device returns to its working state. For example, when an external event triggers a wake signal.
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

-   The device detects an external event and triggers a wake signal on its bus. The bus driver that detects the wake signal calls [**WdfDeviceIndicateWakeStatus**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceindicatewakestatus). As a result, the framework calls the bus driver's [*EvtDeviceDisableWakeAtBus*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_disable_wake_at_bus) callback function.

-   The device has been idle and a driver calls [**WdfDeviceStopIdle**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicestopidle).

-   The system's power state has changed from a low-power state to its working (S0) state.

In each of these situations, the framework calls the bus driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function, which then restores the device (a child device of the bus) to its working (D0) state.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function (if it exists).

2.  The framework calls the driver's [*EvtInterruptEnable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) callback function (if it exists) for each interrupt, and then it calls the driver's [*EvtDeviceD0EntryPostInterruptsEnabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) callback function (if it exists), so that the driver can enable device interrupts.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill), [*EvtDmaEnablerEnable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable), and [*EvtDmaEnablerSelfManagedIoStart*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start) callback functions (if they exist) for each DMA channel that was created.

4.  If the driver is the device's power policy owner, the framework calls its [*EvtDeviceDisarmWakeFromS0*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_s0) or [*EvtDeviceDisarmWakeFromSx*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_disarm_wake_from_sx) callback function.

5.  The framework calls the driver's [*EvtChildListScanForChildren*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_scan_for_children) callback function (if it exists).

6.  The framework restarts all of the driver's power-managed I/O queues and calls their [*EvtIoResume*](/windows-hardware/drivers/ddi/wdfio/nc-wdfio-evt_wdf_io_queue_io_resume) callback functions (if necessary).

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoRestart*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart) callback function.

 

