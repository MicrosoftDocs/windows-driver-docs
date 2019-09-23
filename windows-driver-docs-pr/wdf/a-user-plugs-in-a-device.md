---
title: A User Plugs in a Device
description: A User Plugs in a Device
ms.assetid: cc047c05-f3aa-4423-98fc-cafd7777e104
keywords:
- PnP WDK KMDF , plugging in devices
- Plug and Play WDK KMDF , plugging in devices
- plugging in devices WDK KMDF
- adding devices WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# A User Plugs in a Device


In the following scenario, the device node includes a KMDF bus driver and one or more KMDF function or filter drivers that support a PnP device.

When a user plugs the device into the bus while the system is running, the device's bus driver and the framework perform the following tasks:

-   The bus driver for the device detects the device and calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfchildlist/nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent). (This process is known as "dynamic enumeration.")

-   The framework calls the bus driver's [*EvtChildListCreateDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_create_device) callback function, so the bus driver can call [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object for the physical device (a PDO).

-   The framework calls the bus driver's [*EvtDeviceResourcesQuery*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfpdo/nc-wdfpdo-evt_wdf_device_resources_query) and [*EvtDeviceResourceRequirementsQuery*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfpdo/nc-wdfpdo-evt_wdf_device_resource_requirements_query) callback functions to determine the system hardware resources that the device requires.

For more information about the power-up sequence for a KMDF bus driver, see [Power-Up Sequence for a Bus Driver](power-up-sequence-for-a-bus-driver.md).

Next, the PnP manager determines which additional drivers (function drivers and filter drivers) the device requires. If these drivers are not already loaded, the PnP manager loads them and calls their [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/wdf/driverentry-for-kmdf-drivers) routines. For each function or filter driver, the following actions occur:

-   The framework calls each additional driver's [*EvtDriverDeviceAdd*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function so that the driver can call [**WdfDeviceCreate**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nf-wdfdevice-wdfdevicecreate) to create a framework device object that represents the device for the driver. Function drivers create a functional device object (FDO), and filter drivers create a filter device object (Filter DO).

-   The framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function and then each driver's [*EvtDeviceFilterAddResourceRequirements*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nc-wdffdo-evt_wdf_device_filter_resource_requirements) callback function. Immediately before the device is started, the framework calls the [*EvtDeviceRemoveAddedResources*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdffdo/nc-wdffdo-evt_wdf_device_remove_added_resources) callback function. These three callback functions allow the filter and function drivers to modify the list of hardware resources that the device requires, before the PnP manager assigns resources to the device. For more information, see [Hardware Resources for Framework-Based Drivers](hardware-resources-for-kmdf-drivers.md)

-   The framework ensures that the device has reached its working (D0) power state.

-   For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:
    1.  The framework calls the driver's [*EvtDevicePrepareHardware*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback function (if it exists) and passes the list of hardware resources that the PnP manager has assigned to the device.
    2.  The framework calls the driver's [*EvtDeviceD0Entry*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) callback function (if it exists).
    3.  The framework calls the driver's [*EvtInterruptEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfinterrupt/nc-wdfinterrupt-evt_wdf_interrupt_enable) callback function (if it exists) for each interrupt, and then it calls the driver's [*EvtDeviceD0EntryPostInterruptsEnabled*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry_post_interrupts_enabled) callback function (if it exists), so that the driver can enable device interrupts.
    4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_fill), [*EvtDmaEnablerEnable*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_enable), and [*EvtDmaEnablerSelfManagedIoStart*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdmaenabler/nc-wdfdmaenabler-evt_wdf_dma_enabler_selfmanaged_io_start) callback functions (if they exist) for each DMA channel that was created.
    5.  The framework calls the driver's [*EvtChildListScanForChildren*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfchildlist/nc-wdfchildlist-evt_wdf_child_list_scan_for_children) callback function (if it exists).
    6.  The framework starts all of the device's power-managed I/O queues.
    7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoInit*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdfdevice/nc-wdfdevice-evt_wdf_device_self_managed_io_init) callback function.

For more information about the power-up sequence for KMDF function or filter drivers, [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md).

 

 





