---
title: UMDF Driver Host Process
author: windows-driver-content
description: This topic describes the User-Mode Driver Framework (UMDF) driver host process and how it works with other UMDF components. It applies to both UMDF versions 1 and 2.
ms.assetid: 8b469c91-d33d-4fb0-8c7d-e90f86a1e339
keywords: ["driver host process WDK UMDF", "User-Mode Driver Framework WDK , architecture", "UMDF WDK , architecture", "user-mode drivers WDK UMDF , architecture", "architecture WDK UMDF"]
---

# UMDF Driver Host Process


This topic describes the User-Mode Driver Framework (UMDF) driver host process and how it works with other UMDF components. It applies to both UMDF versions 1 and 2.

The driver host process (Wudfhost.exe) is a child process of the driver manager service. Wudfhost.exe usually runs in the *LocalService* account, which has minimum privileges on the local computer. An instance of Wudfhost.exe loads one or more UMDF driver DLLs, in addition to the framework DLLs. The driver host process provides a runtime environment that handles interprocess communication (IPC) between the driver manager and the reflector, as well as I/O dispatching, driver loading, driver layering, and thread pool management.

The driver manager can create multiple concurrent instances of Wudfhost.exe, as follows:

-   If your UMDF driver was built with version 1.11 and is running on Windows 8 or later, by default the driver manager creates a single instance of Wudfhost that can host multiple device stacks. This technique is called *device pooling*.

    If your UMDF driver was built with version 2.0 and is running on Windows 8.1, pooling is also on by default.

-   If your driver was built with UMDF version 1.9 or earlier, the framework creates a separate instance of the host process (Wudfhost) for each device stack.

For more about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

Within Wudfhost.exe, each UMDF driver runs in its own address space, and is therefore isolated from the application process and other instances of the driver host.

You can load drivers built with UMDF versions 1 and 2 concurrently, either in the same host process or in different host processes. For example, by default, the driver manager would load a UMDF 1.11 driver and a UMDF 2.0 driver in the same host process on a computer running Windows 8.1.

However, you cannot load UMDF version 1 and 2 drivers in the same device stack. For example, you cannot load a UMDF version 1 filter driver above a UMDF version 2 function driver.

For a diagram that shows how the driver host relates to other UMDF components, see [Overview of UMDF](overview-of-the-umdf.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20UMDF%20Driver%20Host%20Process%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




