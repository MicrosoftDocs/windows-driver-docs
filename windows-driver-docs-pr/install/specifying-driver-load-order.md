---
title: Specifying Driver Load Order
description: Specifying Driver Load Order
ms.assetid: 2e06671a-5664-4042-bc7a-e8ab12938cea
keywords:
- INF files WDK device installations , driver load order
- driver load order WDK INF files
- load order WDK INF files
- service-install-sections WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Driver Load Order





For most devices, the physical hierarchy of the devices on a computer determines the order in which Windows and the PnP manager load drivers. Windows and the PnP manager configure devices starting with the system root device, and then they configure the child devices of the root device (for example, a PCI adapter), the children of those devices, and so on. The PnP manager loads the drivers for each device as the device is configured, if the drivers were not previously loaded for another device.

Settings in the INF file can influence driver load order. This topic describes the relevant values that vendors should specify in the *service-install-section* referenced by a driver's [**INF AddService directive**](inf-addservice-directive.md). Specifically, this topic discusses the **StartType**, **BootFlags**, **LoadOrderGroup**, and **Dependencies** entries.

Drivers should follow these rules for specifying **StartType**:

-   PnP driver

    A PnP driver should have a start type of SERVICE_DEMAND_START (0x3), specifying that the PnP manager can load the driver when the PnP manager finds a device that the driver services.

-   Driver for a device required to start the computer

    If a device is required to start the computer, the drivers for the device should have a start type of SERVICE_BOOT_START (0x0).

-   Non-[*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) that detects device(s) that are not PnP-enumerable

    For a device that is not PnP-enumerable, a driver reports the device to the PnP manager by calling [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597). Such a driver should have the start type SERVICE_SYSTEM_START (0x01) so Windows will load the driver during system initialization.

    Only drivers that report non-PnP hardware should set this start type. If a driver services both PnP and non-PnP devices, it should set this start type.

-   Non-PnP driver that must be started by the service control manager

    Such a driver should have the start type SERVICE_AUTO_START (0x02). PnP drivers must not set this start type.

A PnP driver should be written so that it can be loaded when Windows configures a device that the driver services. Conversely, a driver should be able to be unloaded any time that the PnP manager determines that there are no longer devices present that the driver services. The only driver load orderings that PnP drivers should depend on are as follows:

1.  The drivers for a child device can depend on the fact that the drivers for the parent device are loaded.

2.  A driver in the device stack can depend on the fact that any drivers below it are loaded.

    For example, the function driver can be certain that any lower-filter drivers are loaded.

    However, be aware that a driver in the device stack cannot depend on being loaded sequentially after a device's lower drivers, because the driver might are loaded previously when another device was configured.

Filter drivers in a filter group cannot predict their load ordering. For example, if a device has three registered upper-filter drivers, those three drivers will all be loaded after the function driver but could be loaded in any order within their upper-filter group.

If a driver has an explicit load-order dependency on another driver, that dependency should be implemented through a parent/child relationship. A driver for a child device can depend on the drivers for the parent device being loaded before the child drivers are loaded.

To reinforce the importance of setting the correct **StartType** value, the following list describes how Windows and the PnP manager use the **StartType** entries in INF files:

1.  On system startup, the operating system loader loads drivers of type SERVICE_BOOT_START before it transfers control to the kernel. These drivers are in memory when the kernel gets control.

    Boot-start drivers can use INF **LoadOrderGroup** entries to order their loading. (Boot-start drivers are loaded before most of the devices are configured, so their load order cannot be determined by device hierarchy.) The operating system ignores INF **Dependencies** entries for boot-start drivers.

2.  The PnP manager calls the **DriverEntry** routines of the SERVICE_BOOT_START drivers so the drivers can service the boot devices.

    If a boot device has child devices, those devices are enumerated. The child devices are configured and started if their drivers are also boot-start drivers. If a device's drivers are not all boot-start drivers, the PnP manager creates a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) for the device but does not start the device yet.

3.  After all the boot drivers have loaded and the boot devices are started, the PnP manager configures the rest of the PnP devices and loads their drivers.

    The PnP manager walks the [device tree](https://msdn.microsoft.com/library/windows/hardware/ff543194) and loads the drivers for the [*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode) that are not yet started (that is, any nonstarted devnodes from the previous step). As each device starts, the PnP manager enumerates the children of the device, if any.

    As it configures these devices, the PnP manager loads the drivers for the devices, *regardless* of the drivers' **StartType** values (except when **StartType** is SERVICE_DISABLED) before proceeding to start the devices. Many of these drivers are SERVICE_DEMAND_START drivers.

    The PnP manager ignores registry entries that were created as a result of INF **Dependencies** entries and **LoadOrderGroup** entries for drivers that it loads in this step. The load ordering is based on the physical device hierarchy.

    At the end of this step, all the devices are configured, except devices that are not PnP-enumerable and the descendants of those devices. (The descendants might or might not be PnP-enumerable.)

4.  The PnP manager loads drivers of **StartType** SERVICE_SYSTEM_START that are not yet loaded.

    These drivers detect and report their non-PnP devices. The PnP manager processes registry entries that are the result of INF **LoadOrderGroup** entries for these drivers. It ignores registry entries that were created because of INF **Dependencies** entries for these drivers.

5.  The service control manager loads drivers of **StartType** SERVICE_AUTO_START that are not yet loaded.

    The service control manager processes the service database information with respect to the services' **DependOnGroup** and **DependOnServices**. This information is from **Dependencies** entries in INF **AddService** entries. Be aware that the **Dependencies** information is only processed for non-PnP drivers because any necessary PnP drivers were loaded in an earlier step of system startup. The service control manager ignores INF **LoadOrderGroup** information.

    See the Microsoft Windows SDK documentation for more information about the service control manager.

### Using BootFlags to Promote a Driver's StartType at Boot Depending on Boot Scenario

The operating system can promote a driver's **StartType** to be a boot start driver depending on the **BootFlags** value specified in the driver's INF. You can specify one or more (ORed) of the following numeric values in the INF file, expressed as a hexadecimal value:

-   If a driver should be promoted to be a boot start driver on network boot, specify **0x1** (CM_SERVICE_NETWORK_BOOT_LOAD).
-   If a driver should be promoted on booting from a VHD, specify **0x2** (CM_SERVICE_VIRTUAL_DISK_BOOT_LOAD)
-   If a driver should be promoted while booting from a USB disk, specify **0x4** (CM_SERVICE_USB_DISK_BOOT_LOAD).
-   If a driver should be promoted while booting from SD storage, specify **0x8** (CM_SERVICE_SD_DISK_BOOT_LOAD)
-   If a driver should be promoted while booting from a disk on a USB 3.0 controller, specify **0x10** (CM_SERVICE_USB3_DISK_BOOT_LOAD).
-   If a driver should be promoted while booting with measured boot enabled, specify **0x20** (CM_SERVICE_MEASURED_BOOT_LOAD).
-   If a driver should be promoted while booting with verifier boot enabled, specify **0x40** (CM_SERVICE_VERIFIER_BOOT_LOAD).
-   If a driver should be promoted on WinPE boot, specify **0x80** (CM_SERVICE_WINPE_BOOT_LOAD).

For more information about promoting a driver's **StartType** at boot, depending on the boot scenario, see [**INF AddService directive**](inf-addservice-directive.md).

 

 





