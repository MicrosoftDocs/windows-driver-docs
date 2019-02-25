---
title: WDM Concepts for WDF Drivers
description: WDM Concepts for WDF Drivers
ms.assetid: 164b4882-a5a3-45d3-a2f5-53367b396439
keywords:
- kernel-mode drivers WDK KMDF , WDM
- KMDF WDK , WDM
- Kernel-Mode Driver Framework WDK , WDM
- framework-based drivers WDK KMDF , WDM
- WDM drivers WDK KMDF
- bus enumeration WDK KMDF
- bus drivers WDK KMDF
- function drivers WDK KMDF
- filter drivers WDK KMDF
- driver stacks WDK KMDF
- stacks WDK KMDF
- device stacks WDK KMDF
- IRPs WDK KMDF
- I/O request packets WDK KMDF
- I/O requests WDK KMDF , IRPs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDM Concepts for WDF Drivers


Windows Driver Frameworks (WDF) is a wrapper around Microsoft Windows Driver Model (WDM) interfaces. Although the framework simplifies many WDM concepts and hides others completely so that you do not have to work with them, you should still understand some of the basic concepts of WDM drivers. Specifically, you should understand [driver types](#driver-types), [driver stacks](#driver-stacks), [device stacks](#device-stacks), and [I/O request packets](#io-request-packets).

### Driver types

Windows-based drivers are divided into three types: [bus drivers](https://msdn.microsoft.com/library/windows/hardware/ff540704), [function drivers](https://msdn.microsoft.com/library/windows/hardware/ff546516), and [filter drivers](https://msdn.microsoft.com/library/windows/hardware/ff545890). Bus drivers support I/O buses by detecting child devices that are plugged into a parent bus and reporting their characteristics. (This activity is called *bus enumeration*.) Function drivers control I/O operations for devices and buses. Filter drivers receive, review, and possibly modify data that flows between user applications and drivers, or between individual drivers.

Drivers for buses are essentially function drivers that also enumerate children. A driver acts as a "bus driver" when it enumerates the child devices on a bus. Otherwise, the same driver acts as the "function driver" for the bus when it handles I/O operations that access the bus adapter's hardware.

A User-Mode Driver Framework (UMDF) driver cannot be a bus driver.

### Driver stacks

In the Windows operating system, WDM drivers are layered in a vertical calling sequence that is called a *driver stack*. The topmost driver in the stack typically receives I/O requests from user applications, after the requests have passed through the operating system's I/O manager. The lower driver layers typically communicate with computer hardware.

A simple driver stack includes a bus driver at the bottom of the stack, which handles bus-specific I/O operations and enumerates the child devices that are connected to it. Typically, one or more device-specific function drivers are above the bus driver. These function drivers handle I/O operations to the devices that are connected to the bus. Filter drivers can be above the function drivers, or they can reside between a bus driver and function driver. A running system has several driver stacks that support different types of devices.

### Device stacks

Each driver stack supports one or more *device stacks*. A device stack is a set of *device objects* that are created from WDM-defined [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147) structures. Each device stack represents one device. Each driver creates a device object for each of its devices and attaches each device object to a device stack. Device stacks are created and removed as devices are plugged in and unplugged, and each time the system is rebooted.

When a bus driver detects that child devices have been plugged in or unplugged, it informs the Plug and Play (PnP) manager. In response, the PnP manager asks the bus driver to create a physical device object (PDO) for each child device that is connected to the parent device (that is, the bus). The PDO becomes the bottom of a device stack.

Next, the PnP manager loads function and filter drivers to support each device (if they are not already loaded), and then the PnP manager calls these drivers so that each can create a device object and add it to the top of the device stack. Function drivers create functional device objects (FDOs), and filter drivers create filter device objects (filter DOs).

When the I/O manager sends an I/O request to a device's drivers, it passes the request to the driver that created the topmost device object in the device stack. If that driver asks the I/O manager to pass the request to the next-lower driver, the I/O manager uses the device stack to determine the next-lower driver. (The next-lower driver is the driver that created the next-lower device object.)

WDF creates a framework device object for each WDM device object. Framework-based drivers access these framework device objects instead of WDM device objects.

### I/O request packets

The I/O manager sends an application's I/O requests to drivers by creating I/O request packets (IRPs). An IRP can contain a request to perform an I/O operation (such as a read/write operation) or a request to perform an I/O control (IOCTL) action (such as returning status). In addition, the PnP manager creates IRPs that represent PnP and power management operations that drivers must perform, and it sends these IRPs to drivers.

Typically, the I/O manager creates a read or write IRP when a user application requests a read or write operation. The I/O manager passes the IRP to the driver at the top of the driver stack, and that driver either services the request or passes the request to the next-lower driver. Some requests travel to the bottom of the stack, and some are completely processed by higher-level drivers.

Each time a driver receives an IRP, the driver also receives a pointer to the device object that represents the device that must handle the operation. Therefore, the drivers in a driver stack use device objects to determine which of their plugged-in devices a particular request is supposed to go to.

WDF drivers typically do not directly access IRPs. The framework converts the WDM IRPs that represent read, write, and device I/O control operations to framework request objects that Kernel-Mode Driver Framework (KMDF) and UMDF drivers receive in I/O queues. The framework handles PnP and power management IRPs internally and uses event callback functions to inform the driver of PnP and power events.

 

 





