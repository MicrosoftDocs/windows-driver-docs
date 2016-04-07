---
title: Overview of UMDF
description: This topic provides a high-level overview of User-Mode Driver Framework (UMDF) components and describes how your driver interacts with system-supplied components. It applies to both UMDF versions 1 and 2.
ms.assetid: b36c9fad-1963-4d29-a1e7-890de77fed50
keywords: ["User-Mode Driver Framework WDK , about UMDF", "UMDF WDK , about UMDF", "user-mode drivers WDK UMDF , about UMDF", "driver host process WDK UMDF", "reflectors WDK UMDF", "driver manager WDK UMDF", "stacks WDK UMDF", "device stacks WDK UMDF"]
---

# Overview of UMDF


This topic provides a high-level overview of User-Mode Driver Framework (UMDF) components and describes how your driver interacts with system-supplied components. It applies to both UMDF versions 1 and 2.

UMDF drivers abstract hardware functionality, run in the user-mode environment, and can access various services. UMDF drivers operate as part of a stack of drivers that manage a device. File system drivers, display drivers, and print drivers cannot be UMDF drivers.

A UMDF driver interacts with the following system-supplied components:

-   Driver host process

    The driver host process loads vendor-supplied UMDF drivers and framework DLLs, provides an execution environment for user-mode drivers, and routes messages between drivers in a user-mode stack. For more information, see [UMDF Driver Host Process](umdf-driver-host-process.md).

-   Driver manager

    The driver manager is a Windows service that manages all instances of the Wudfhost driver host process. The driver manager launches and tracks information about each driver host process. Each host is a child process of the driver manager. Only one driver manager exists per system. The driver manager starts during installation of the first UMDF device and runs on the system thereafter.

-   Reflector

    The reflector is a kernel-mode driver that permits an application and a driver host process (and user-mode device stacks) to communicate. The reflector creates a separate device object for each device instance and handles Plug and Play (PnP) and power I/O requests associated with each device instance. All communication between the application and the driver host process happens through the reflector. For more information, see [Architecture of UMDF](detailed-view-of-the-umdf-architecture.md).

All function and filter drivers for a given device must run in the same driver host process, but multiple host processes can be running concurrently.

The following diagram shows how driver host processes, driver manager, and reflector communicate across the user mode/kernel mode boundary.

![umdf components including up and down device objects in reflector](images/umdfarch3.gif)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Overview%20of%20UMDF%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




