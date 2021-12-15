---
title: The PnP Manager Redistributes System Resources
description: Learn how the PnP manager redistributes system resources. This occurs when a user adds a device that requires resources already assigned elsewhere.
keywords:
- PnP WDK KMDF , redistributing resources
- Plug and Play WDK KMDF , redistributing resources
- resource redistribution WDK KMDF
- redistributing resources WDK KMDF
- power-down sequence WDK KMDF
- power-up sequence WDK KMDF
ms.date: 04/20/2017
---

# The PnP Manager Redistributes System Resources


If a user adds a device to a system, and if the device requires system resources that the PnP manager has already assigned to another device, the PnP manager attempts to reassign resources.

During this process, the PnP manager stops devices and takes them out of their working (D0) states. It then delivers new resource lists to the devices so that they can restart, using the new resources.

When redistributing resources, the PnP manager will not alter a device's resource assignment if one of the device's drivers has:

-   Called [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) and a special file is open on the device.

-   Called [**WdfDeviceSetStaticStopRemove**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetstaticstopremove).

-   Supplied an [*EvtDeviceQueryStop*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_stop) callback function, and the callback function has vetoed the reassignment.

### Power-Down Sequence

For each function and filter driver that supports the device being stopped, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) callback function.

2.  The framework stops all of the device's power-managed I/O queues.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop), [*EvtDmaEnablerFlush*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush), and [*EvtDmaEnablerDisable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable) callback functions for each DMA channel that was created.

4.  Calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) and [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback functions (if they exist) so that the driver can disable device interrupts.

5.  The framework calls the driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function (if it exists).

6.  The framework calls the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function (if it exists) passing the list of hardware resources that the PnP manager has assigned to the device.

The bus driver is the lowest driver in the stack and is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function, it passes a handle to the framework device object representing the device's PDO and a *TargetState* value of **WdfPowerDeviceD3Final**. The bus driver can control when the framework calls its [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function by calling [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure).

### Power-Up Sequence

The first driver called is the bus driver. When the framework calls the bus driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function, the callback function restores the device (a child device of the bus) to its working (D0) state.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:

1.  The framework calls the driver's [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function (if it exists), passing the list of hardware resources that the PnP manager has assigned to the device.

2.  The framework calls the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function (if it exists).

3.  The framework calls the driver's [*EvtInterruptEnable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) and [*EvtDeviceD0EntryPostInterruptsEnabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) callback functions (if they exist) so that the driver can enable device interrupts.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill), [*EvtDmaEnablerEnable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable), and [*EvtDmaEnablerSelfManagedIoStart*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start) callback functions for each DMA channel that was created.

5.  The framework calls the driver's [*EvtChildListScanForChildren*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_scan_for_children) callback function (if it exists).

6.  The framework restarts all of the device's power-managed I/O queues.

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoRestart*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_restart) callback function.

 

