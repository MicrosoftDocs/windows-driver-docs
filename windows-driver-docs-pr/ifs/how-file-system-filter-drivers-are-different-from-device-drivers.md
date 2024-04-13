---
title: How File System Filter Drivers Are Different from Device Drivers
description: How File System Filter Drivers Are Different from Device Drivers
keywords:
- filter drivers WDK file system , vs. device drivers
- file system filter drivers WDK , vs. device drivers
- device drivers WDK file system
ms.date: 10/16/2019
---

# How File System Filter Drivers Are Different from Device Drivers

File system filter drivers and device drivers in the Microsoft Windows operating system are different in the following ways:

- **No Power Management**

  Because file system filter drivers are not device drivers and thus do not control hardware devices directly, they do not receive [**IRP\_MJ\_POWER**](../kernel/irp-mj-power.md) requests. Instead, power IRPs are sent directly to the storage device stack. In rare circumstances, however, file system filter drivers might interfere with power management. For this reason, file system filter drivers should not register dispatch routines for IRP\_MJ\_POWER in the **DriverEntry** routine, and they should not call [PoXxx](/windows-hardware/drivers/ddi/_kernel/#power-management-routines) routines.

- **No WDM**

  File system filter drivers cannot be Windows Driver Model (WDM) drivers. The Microsoft [Windows Driver Model](../kernel/writing-wdm-drivers.md) is only for device drivers.

- **No AddDevice or StartIo**

  Because file system filter drivers are not device drivers and thus do not control hardware devices directly, they should not have [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) or [**StartIo**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routines.

- **Different Device Objects Created**

  Although file system filter drivers and device drivers both create device objects, they differ in the number and kinds of device objects that they create.

  Device drivers create physical and functional device objects to represent devices. The Plug and Play (PnP) Manager builds and maintains a global device tree that contains all device objects that are created by device drivers. The device objects that file system filter drivers create are not contained in this device tree.

  File system filter drivers do not create physical or functional device objects. Instead, they create control device objects and filter device objects. The *control device object* represents the filter driver to the system and to user-mode applications. The *filter device object* performs the actual work of filtering a specific file system or volume. A file system filter driver normally creates one control device object and one or more filter device objects.

- **Other Differences**

  - Because file system filter drivers are not device drivers, they do not perform [direct memory access (DMA)](../kernel/using-direct-i-o-with-dma.md).

  - Unlike device filter drivers, which can attach above or below a target device's function driver, file system filter drivers can attach only above a target file system driver. Thus, in device-driver terms, a file system filter driver can be only an upper filter, never a lower filter.
