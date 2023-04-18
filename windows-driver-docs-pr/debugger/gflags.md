---
title: GFlags
description: Learn how GFlags (the Global Flags Editor), gflags.exe, enables and disables advanced debugging, diagnostic, and troubleshooting features. 
keywords: GFlags, Global Flags Editor, gflags.exe
ms.date: 03/08/2023
---

# GFlags

GFlags, the Global Flags Editor, enables and disables advanced debugging, diagnostic, and troubleshooting features. It's most often used to turn on indicators that other tools track, count, and log.

## Where to get GFlags

GFlags is included in the [Debugging Tools for Windows 10 (WinDbg)](debugger-download-tools.md).

After the debugging tools are installed, the 64-bit version of gflags.exe is installed by default in the following directory.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
```

If you're running a 32-bit version of Windows, use the 32-bit version of gflags.exe located here:

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86
```

## Overview of GFlags

Driver developers and testers often use GFlags to turn on debugging, logging, and test features either directly, or by including GFlags commands in a test script. The page heap verification features can help you to identify memory leaks and buffer errors in kernel-mode drivers.

GFlags has both a dialog box and a command-line interface. Most features are available from both interfaces, but some features are accessible from only one of the interfaces. For more information, see [GFlags details](gflags-details.md).

### Features

- Page heap verification. GFlags now includes the functions of `PageHeap` (pageheap.exe), a tool that enables heap allocation monitoring. `PageHeap` was included in previous versions of Windows.

- No reboot required for the *Special Pool* feature. On Windows Vista and later versions of Windows, you can enable, disable, and configure the Special Pool feature without restarting ("rebooting") the computer. For more information, see [Special Pool](special-pool.md).

- Object Reference Tracing. A new flag enables tracing of object referencing and object dereferencing in the kernel. This feature detects when an object reference count is decremented too many times or not decremented even though an object is no longer used. This flag is supported only in Windows Vista and later versions of Windows.

- New dialog box design. The GFlags dialog box has tabbed pages for easier navigation.

### Requirements

To use most GFlags features, including setting flags in the registry or in kernel mode, or enabling page heap verification, you must be a member of the Administrators group on the computer. However, prior to Windows Vista, users with at least Guest account access can launch a program from the **Global Flags** dialog box.

When features don't work, or work differently, on particular operating system versions, the differences are explained in the description of the feature.

This section includes:

[GFlags overview](gflags-overview.md)

[GFlags details](gflags-details.md)

[GFlags commands](gflags-commands.md)

[GFlags flag table](gflags-flag-table.md)

[GFlags and PageHeap](gflags-and-pageheap.md)

[Global Flags Dialog Box](global-flags-dialog-box.md)

[GFlags Examples](gflags-examples.md)

[Global Flag Reference](global-flag-reference.md)

> [!NOTE]
> Incorrect use of this tool can degrade system performance or prevent Windows from starting, requiring you to reinstall Windows.

> [!IMPORTANT]
> Pool tagging is permanently enabled on Windows Server 2003 and later versions of Windows, including Windows Vista. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed, and commands to enable or disable pool tagging fail.

## See also

[Tools Included in Debugging Tools for Windows](extra-tools.md)

[GFlags examples](gflags-examples.md)

[Global flag reference](global-flag-reference.md)

[Tools included in Debugging Tools for Windows](extra-tools.md)
