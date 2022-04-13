---
title: Supporting multiple operating system versions
description: This page describes how to make a driver package support different functionality on multiple operating system versions.
ms.date: 04/12/2022
---

# Supporting multiple operating system versions

[Driver packages](../install/driver-packages.md) generally will support many versions of the Windows operating system. As part of supporting multiple versions of the operating system, the driver package may need to have different behavior on different versions of the operating system in order to make use of new features or to meet new requirements of the new operating system version. For example, a driver package may want to have different behavior on operating systems after a certain version in order to meet the requirements of [Windows Drivers](getting-started-with-windows-drivers.md). The following sections describe how you can have different behaviors both in the driver package's [INF file](../install/overview-of-inf-files.md) and in the runtime behavior of binaries in the driver package.

## INF support

*TargetOSVersion* decorations on [INF models sections](../install/inf-models-section.md) in the INF allow the INF author to provide different installation instructions and settings for different versions of the operating system.  

See [Combining platform extensions with operating system versions](../install/combining-platform-extensions-with-operating-system-versions.md) for more information.

## Runtime support

When trying to alter behavior at runtime to support multiple operating system versions, it is recommended you check for feature or API availability whenever possible instead of trying to check if the code is running on a certain operating system version or later.  For example, if there is an API that you want to use if it is available, you can attempt to dynamically locate it instead of statically linking to it.  If you are able to locate it, you can use it, however, if it is not present in your current running environment, you can fall back to some alternative behavior.

### Kernel mode

For kernel mode, see [Writing drivers for different versions of Windows](../gettingstarted/platforms-and-driver-versions.md) for more information on how to support multiple versions of Windows from a single driver.

### User mode

In user mode, you can use [LoadLibraryEx](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexw) along with [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to check if a particular API you want to use is available in your current running environment and to get a function pointer to use in order to call that API. See [Run-time dynamic linking](/windows/win32/dlls/run-time-dynamic-linking) and [Using run-time dynamic linking](/windows/win32/dlls/using-run-time-dynamic-linking) for more information.
