---
title: GFlags - Overview
description: Learn how GFlags, the Global Flags Editor (gflags.exe), enables and disables advanced debugging, diagnostic, and troubleshooting features. 
keywords: GFlags, Global Flags Editor, gflags.exe
ms.date: 07/10/2025
---

# GFlags

**GFlags**, the Global Flags Editor, enables and disables advanced debugging, diagnostic, and troubleshooting features. The tool is often used to turn on indicators that other tools track, count, and log. 

The _gflags.exe_ file is included in the [Debugging Tools for Windows 10 (WinDbg)](debugger-download-tools.md). When you install the debugging tools, the 64-bit version of the file is installed by default.

- **Windows 64-bit**: Access GFlags in the default x64 location, _C:\Program Files (x86)\Windows Kits\10\Debuggers\x64_.

- **Windows 32-bit**: Access GFlags in the x86 location, _C:\Program Files (x86)\Windows Kits\10\Debuggers\x86_.

## Overview of GFlags

Driver developers and testers often use GFlags to turn on debugging, logging, and test features either directly, or by including GFlags commands in a test script. The page heap verification features can help you identify memory leaks and buffer errors in **kernel-mode** drivers.

GFlags provides a dialog UI experience and also a command-line prompt. Most features are available from both the UI and the command line, but some features are accessible in one interface only. For more information, see [GFlags details](gflags-details.md).

### Features

GFlags supports the following features:

- Page heap verification. GFlags includes the functions of `PageHeap` (_pageheap.exe_ file), a tool that enables heap allocation monitoring. 

- No reboot is required for the **Special Pool** feature. You can enable, disable, and configure the Special Pool feature without restarting (_rebooting_) the computer. For more information, see [Special Pool](special-pool.md).

- Object Reference Tracing. A flag enables tracing of object referencing and object dereferencing in the kernel. This feature detects when an object reference count is decremented too often or not decremented, even though an object is no longer used. 

- The GFlags dialog has tabbed pages for easy navigation.

> [!IMPORTANT]
> Pool tagging is permanently enabled on Windows. The **Enable pool tagging** check box on the **Global Flags** dialog is unavailable, and commands to enable or disable pool tagging fail.

### Requirements

To use most GFlags features, you must be a member of the Administrator's group on the computer. For example, to set flags in the registry or in kernel mode, or enable page heap verification.

> [!NOTE]
> Incorrect use of the GFlags tool can degrade system performance or prevent Windows from starting, which might require you to reinstall Windows.

This section includes:

- [GFlags overview](gflags-overview.md)

- [GFlags details](gflags-details.md)

- [GFlags commands](gflags-commands.md)

- [GFlags flag table](gflags-flag-table.md)

- [GFlags and PageHeap](gflags-and-pageheap.md)

- [Global Flags dialog](global-flags-dialog-box.md)

- [GFlags examples](gflags-examples.md)

- [Global Flag reference](global-flag-reference.md)

## Related articles

- [GFlags examples](gflags-examples.md)
- [Global flag reference](global-flag-reference.md)
- [Tools included in Debugging Tools for Windows](extra-tools.md)