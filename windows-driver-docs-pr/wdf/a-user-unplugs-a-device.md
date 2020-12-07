---
title: A User Unplugs a Device
description: Learn what happens when a user unplugs a device by 'orderly removal' (using Unplug or Eject Hardware) or 'surprise removal'.
keywords:
- PnP WDK KMDF , unplugging devices
- Plug and Play WDK KMDF , unplugging devices
- orderly device removal WDK KMDF
- unplugging devices WDK KMDF
- surprise device removal WDK KMDF
- unexpected device removal WDK KMDF
- removing devices WDK KMDF
- ejecting devices WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A User Unplugs a Device


While a system is running, a user can remove a device in one of two ways: by *orderly removal*, which means that the user informs the system that the device is about to be removed (for example, by using the Unplug or Eject Hardware program); or by *surprise removal*, which means that the user unplugs the device without informing the system. If the bus supports surprise removal (for example, USB), the device's drivers must be able to handle the device's sudden disappearance.

### <a href="" id="orderly-removal"></a> Orderly Removal

The user requests removal by using the system's Unplug or Eject Hardware program, by disabling the device by using Device Manager, or by pushing an [ejectable](supporting-ejectable-devices.md) device's eject button. The framework allows the device to be removed or disabled, unless the driver has:

-   Called [**WdfDeviceSetSpecialFileSupport**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetspecialfilesupport) and a special file is open on the device.

-   Called [**WdfDeviceSetStaticStopRemove**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetstaticstopremove).

-   Supplied an [*EvtDeviceQueryRemove*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_query_remove) callback function, and the callback function has vetoed the removal.

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) callback function.

2.  The framework stops all of the driver's power-managed I/O queues.

3.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop), [*EvtDmaEnablerFlush*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush), and [*EvtDmaEnablerDisable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable) callback functions (if they exist) for each DMA channel that was created.

4.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) callback function (if it exists), and then calls the driver's [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback function (if it exists) for each interrupt so that the driver can disable device interrupts.

5.  The framework calls the driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function (if it exists).

6.  The framework calls the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function (if it exists), passing it the list of hardware resources that the PnP manager has assigned to the device.

7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoFlush*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush) callback function.

8.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoCleanup*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup) callback function.

The bus driver is the driver in the stack that is called last. When the framework calls the bus driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function, the callback function sets the power state of the device (a child device of the bus) to D3. The bus driver can control when the framework calls its [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function by calling [**WdfDeviceInitSetReleaseHardwareOrderOnFailure**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure).

### <a href="" id="surprise-removal"></a> Surprise Removal

A user unplugs a device unexpectedly. The bus driver for the device's bus discovers that the device is missing and calls [**WdfChildListUpdateChildDescriptionAsMissing**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistupdatechilddescriptionasmissing).

For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  The framework calls the driver's [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function (if it exists).

2.  If the device was in its working (D0) state when it was unplugged, the framework stops all of the driver's power-managed I/O queues.

3.  If the device was in its working (D0) state when it was unplugged, and if the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoSuspend*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_suspend) callback function.

4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerSelfManagedIoStop*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_stop), [*EvtDmaEnablerFlush*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_flush), and [*EvtDmaEnablerDisable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_disable) callback functions (if they exist) for each DMA channel that was created.

5.  The framework calls the driver's [*EvtDeviceD0ExitPreInterruptsDisabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit_pre_interrupts_disabled) and [*EvtInterruptDisable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_disable) callback functions (if they exist) so that the driver can disable device interrupts.

6.  The framework calls the driver's [*EvtDeviceD0Exit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_exit) callback function (if it exists).

7.  The framework calls the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function (if it exists), passing the list of hardware resources that the PnP manager has assigned to the device.

8.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoFlush*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_flush) callback function.

9.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoCleanup*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_cleanup) callback function.

Note that a device can be unexpectedly removed at any time. Therefore, the framework might call the driver's [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function at a time other than that shown in the previous steps. For example, if a user unexpectedly unplugs the device while it is [entering a low-power state](a-device-enters-a-low-power-state.md), the framework might call the [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function after it calls the [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function. You must not code an [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function in a manner that assumes that it and other callback functions are called in a particular sequence.

In addition, the framework does not synchronize a device's [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function with any of the callback functions listed in the previous steps for that device. Therefore, the [*EvtDeviceSurpriseRemoval*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_surprise_removal) callback function might run while another of the previously listed callback functions is also running.

 

