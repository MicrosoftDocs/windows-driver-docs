---
title: UMDF Driver Host Process
description: This topic describes the User-Mode Driver Framework (UMDF) driver host process and how it works with other UMDF components. It applies to both UMDF versions 1 and 2.
ms.assetid: 8b469c91-d33d-4fb0-8c7d-e90f86a1e339
keywords:
- driver host process WDK UMDF
- User-Mode Driver Framework WDK , architecture
- UMDF WDK , architecture
- user-mode drivers WDK UMDF , architecture
- architecture WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UMDF Driver Host Process


This topic describes the User-Mode Driver Framework (UMDF) driver host process and how it works with other UMDF components. It applies to both UMDF versions 1 and 2.

The driver host process (Wudfhost.exe) is a child process of the driver manager service. Wudfhost.exe usually runs in the *LocalService* account, which has minimum privileges on the local computer. An instance of Wudfhost.exe loads one or more UMDF driver DLLs, in addition to the framework DLLs. The driver host process provides a runtime environment that handles interprocess communication (IPC) between the driver manager and the reflector, as well as I/O dispatching, driver loading, driver layering, and thread pool management.

The driver manager can create multiple concurrent instances of Wudfhost.exe, as follows:

-   If your UMDF driver was built with version 1.11 and is running on Windows 8, by default the driver manager creates a single instance of Wudfhost that can host multiple device stacks. This technique is called *device pooling*.

    If your UMDF driver was built with version 2 and is running on Windows 8.1 or Windows 10, pooling is also on by default.

-   If your driver was built with UMDF version 1.9 or earlier, the framework creates a separate instance of the host process (Wudfhost) for each device stack.

For more about device pooling, see [Using Device Pooling in UMDF Drivers](using-device-pooling-in-umdf-drivers.md).

Within Wudfhost.exe, each UMDF driver runs in its own address space, and is therefore isolated from the application process and other instances of the driver host.

You can load drivers built with UMDF versions 1 and 2 concurrently, either in the same host process or in different host processes. For example, by default, the driver manager would load a UMDF 1.11 driver and a UMDF 2 driver in the same host process on a computer running Windows 8.1 or later.

However, you cannot load UMDF version 1 and 2 drivers in the same device stack. For example, you cannot load a UMDF version 1 filter driver above a UMDF version 2 function driver.

For a diagram that shows how the driver host relates to other UMDF components, see [Overview of UMDF](overview-of-the-umdf.md).

 

 





