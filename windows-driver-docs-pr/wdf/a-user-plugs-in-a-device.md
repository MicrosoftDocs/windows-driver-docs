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

-   The bus driver for the device detects the device and calls [**WdfChildListAddOrUpdateChildDescriptionAsPresent**](https://msdn.microsoft.com/library/windows/hardware/ff545591). (This process is known as "dynamic enumeration.")

-   The framework calls the bus driver's [*EvtChildListCreateDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540828) callback function, so the bus driver can call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object for the physical device (a PDO).

-   The framework calls the bus driver's [*EvtDeviceResourcesQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540895) and [*EvtDeviceResourceRequirementsQuery*](https://msdn.microsoft.com/library/windows/hardware/ff540894) callback functions to determine the system hardware resources that the device requires.

For more information about the power-up sequence for a KMDF bus driver, see [Power-Up Sequence for a Bus Driver](power-up-sequence-for-a-bus-driver.md).

Next, the PnP manager determines which additional drivers (function drivers and filter drivers) the device requires. If these drivers are not already loaded, the PnP manager loads them and calls their [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff540807) routines. For each function or filter driver, the following actions occur:

-   The framework calls each additional driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function so that the driver can call [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) to create a framework device object that represents the device for the driver. Function drivers create a functional device object (FDO), and filter drivers create a filter device object (Filter DO).

-   The framework calls each function and filter driver's [*EvtDeviceFilterRemoveResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540872) callback function and then each driver's [*EvtDeviceFilterAddResourceRequirements*](https://msdn.microsoft.com/library/windows/hardware/ff540870) callback function. Immediately before the device is started, the framework calls the [*EvtDeviceRemoveAddedResources*](https://msdn.microsoft.com/library/windows/hardware/ff540892) callback function. These three callback functions allow the filter and function drivers to modify the list of hardware resources that the device requires, before the PnP manager assigns resources to the device. For more information, see [Hardware Resources for Framework-Based Drivers](hardware-resources-for-kmdf-drivers.md)

-   The framework ensures that the device has reached its working (D0) power state.

-   For each function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is lowest in the driver stack:
    1.  The framework calls the driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function (if it exists) and passes the list of hardware resources that the PnP manager has assigned to the device.
    2.  The framework calls the driver's [*EvtDeviceD0Entry*](https://msdn.microsoft.com/library/windows/hardware/ff540848) callback function (if it exists).
    3.  The framework calls the driver's [*EvtInterruptEnable*](https://msdn.microsoft.com/library/windows/hardware/ff541730) callback function (if it exists) for each interrupt, and then it calls the driver's [*EvtDeviceD0EntryPostInterruptsEnabled*](https://msdn.microsoft.com/library/windows/hardware/ff540853) callback function (if it exists), so that the driver can enable device interrupts.
    4.  If the hardware and driver support DMA, the framework calls the driver's [*EvtDmaEnablerFill*](https://msdn.microsoft.com/library/windows/hardware/ff540932), [*EvtDmaEnablerEnable*](https://msdn.microsoft.com/library/windows/hardware/ff540929), and [*EvtDmaEnablerSelfManagedIoStart*](https://msdn.microsoft.com/library/windows/hardware/ff541663) callback functions (if they exist) for each DMA channel that was created.
    5.  The framework calls the driver's [*EvtChildListScanForChildren*](https://msdn.microsoft.com/library/windows/hardware/ff540838) callback function (if it exists).
    6.  The framework starts all of the device's power-managed I/O queues.
    7.  If the driver is using self-managed I/O, the framework calls the driver's [*EvtDeviceSelfManagedIoInit*](https://msdn.microsoft.com/library/windows/hardware/ff540902) callback function.

For more information about the power-up sequence for KMDF function or filter drivers, [Power-Up Sequence for a Function or Filter Driver](power-up-sequence-for-a-function-or-filter-driver.md).

 

 





