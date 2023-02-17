---
title: A User Plugs in a Device
description: Learn what happens when a user plugs in a device. In the example scenario, the device node includes a KMDF bus driver.
keywords:
- PnP WDK KMDF , plugging in devices
- Plug and Play WDK KMDF , plugging in devices
- plugging in devices WDK KMDF
- adding devices WDK KMDF
ms.date: 04/20/2017
---

# A User Plugs in a Device


In the following scenario, the device node includes a KMDF bus driver and one or more KMDF function or filter drivers that support a PnP device.

When a user plugs the device into the bus while the system is running, the device's bus driver and the framework perform the following tasks:

-   The bus driver for the device detects the device and calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](/windows-hardware/drivers/ddi/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent). (This process is known as "dynamic enumeration.")

-   The framework calls the bus driver's [*EvtChildListCreateDevice*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function, so the bus driver can call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object for the physical device (a PDO).

-   The framework calls the bus driver's [*EvtDeviceResourcesQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query) and [*EvtDeviceResourceRequirementsQuery*](/windows-hardware/drivers/ddi/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query) callback functions to determine the system hardware resources that the device requires.

For more information about the power-up sequence for a KMDF bus driver, see [Power-Up Sequence for a Bus Driver](power-up-sequence-for-a-bus-driver.md).

Next, the PnP manager determines which additional drivers (function drivers and filter drivers) the device requires. If these drivers are not already loaded, the PnP manager loads them and calls their [**DriverEntry**](./driverentry-for-kmdf-drivers.md) routines. For each function or filter driver, the following actions occur:

-   The framework calls each additional driver's [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function so that the driver can call [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object that represents the device for the driver. Function drivers create a functional device object (FDO), and filter drivers create a filter device object (Filter DO).

-   The framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function and then each driver's [*EvtDeviceFilterAddResourceRequirements*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function. Immediately before the device is started, the framework calls the [*EvtDeviceRemoveAddedResources*](/windows-hardware/drivers/ddi/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources) callback function. These three callback functions allow the filter and function drivers to modify the list of hardware resources that the device requires, before the PnP manager assigns resources to the device. For more information, see [Hardware Resources for Framework-Based Drivers](/windows-hardware/drivers/wdf/introduction-to-hardware-resources)

-   The framework ensures that the device has reached its working (D0) power state.

-   For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:
    1.  The framework calls the driver's [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function (if it exists) and passes the list of hardware resources that the PnP manager has assigned to the device.
    2.  The framework calls the driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function (if it exists).
    3.  The framework calls the driver's [*EvtInterruptEnable*](/windows-hardware/drivers/ddi/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) callback function (if it exists) for each interrupt, and then it calls the driver's [*EvtDeviceD0EntryPostInterruptsEnabled*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) callback function (if it exists), so that the driver can enable device interrupts.
    4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill), [*EvtDmaEnablerEnable*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable), and [*EvtDmaEnablerSelfManagedIoStart*](/windows-hardware/drivers/ddi/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start) callback functions (if they exist) for each DMA channel that was created.
    5.  The framework calls the driver's [*EvtChildListScanForChildren*](/windows-hardware/drivers/ddi/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_scan_for_children) callback function (if it exists).
    6.  The framework starts all of the device's power-managed I/O queues.
    7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoInit*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init) callback function.

For more information about the power-up sequence for KMDF function or filter drivers, [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md).

