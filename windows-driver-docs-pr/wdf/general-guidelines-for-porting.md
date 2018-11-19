---
title: Preparing for Porting
description: Preparing for Porting
ms.assetid: 355CD834-6B64-4E6F-AA17-AE1145F269CA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preparing for Porting


In some ways, converting a driver from WDM to Windows Driver Frameworks (WDF) is more reimplementation than porting. This is neither as difficult nor as time-consuming as you might expect. Most of the WDM driver’s hardware-specific code can remain relatively intact, although it will use some different object types. WDF defaults replace much of the boilerplate code that a WDM driver requires—particularly for Plug and Play—and WDF provides built-in support for many tricky aspects of driver implementation, such as I/O cancellation (and the associated race conditions) and system power state transitions.

The following general guidelines apply to porting a driver:

-   Refer to the [samples](http://go.microsoft.com/fwlink/p/?linkid=256387). WDF ships with a rich set of samples, most of which are ports of the similarly named WDM drivers.
-   Work incrementally. Because the framework implements default behavior for I/O, Plug and Play, power management, and WMI requests, you can code and debug one device or driver feature at a time.
-   For Kernel-Mode Driver Framework (KMDF), implement WMI event tracing to provide detailed trace logs for use in debugging.
-   In many situations, the WDF defaults provide greater functionality than the existing WDM driver might have implemented. Before trying to port complicated code—particularly for synchronization or queue management—be certain what WDF provides. It might save a considerable amount of time spent porting the driver.
-   Use the WDF-specific [debugger extensions](debugger-extensions-for-kmdf-drivers.md) that are included in the Windows Driver Kit (WDK).
-   Enable the [KMDF verifier](using-kmdf-verifier.md) or [UMDF verifier](using-umdf-verifier.md) while debugging.

## WDM Driver Analysis


Regardless of the type of device and driver involved, the most important issue in porting a driver is to understand the I/O flow through the driver. Before you start writing code, carefully analyze the existing WDM driver. You should be able to answer these questions:

-   How many device objects does the driver require, and what driver roles (FDO, PDO, filter DO) do they represent? In nearly all cases, the WDF driver will use the same type and number of device objects as the WDM driver.
-   Which I/O requests must the driver support?
-   How many queues does the driver require for those requests? What are the characteristics of those queues?
-   Which aspects of I/O processing can take place concurrently, and which must be serialized?
-   Which I/O requests does the driver complete, and which does it pass down the stack?

The answers to these questions determine how the core of the WDF driver is structured, where and when the I/O processing takes place, what type of synchronization the driver requires, and which WDF objects the driver must create to perform I/O. If the driver supports hardware, you must also thoroughly understand the device:

-   Does the device generate interrupts?
-   Which DMA model (if any) does the hardware support? Note that if your driver requires DMA, you must write a KMDF driver.
-   Does the driver manage power policy for the device stack?

Finally, if the driver supports WMI (also KMDF only), you must understand how to gather the data it exports and which WMI callbacks the driver requires.

 

 





