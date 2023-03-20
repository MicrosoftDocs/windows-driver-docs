---
title: Tools for minifilter development and testing
description: Development and Testing Tools
keywords:
- filter manager WDK file system minifilter , tools
- Fltmc.exe WDK file system minifilter
- fltkd debugger extension WDK file system minifilter
- Filter Verifier WDK file system minifilter
- Verifier utility
ms.date: 03/10/2022
ms.custom: contperf-fy22q3
---

# Tools for minifilter development and testing

This page lists a few tools that are specifically for developing a minifilter. Minifilter driver developers are also encouraged to use other [driver development tools](../devtest/index.md) available through the Windows Driver Kit (WDK).

## Fltmc.exe Command

The *Fltmc.exe* program is a system-supplied command line utility for common minifilter driver management operations. Developers can use *Fltmc.exe* to load and unload minifilter drivers, attach or detach minifilter drivers from volumes, and enumerate minifilter drivers, instances, and volumes. In a command prompt with administrator privileges, type ```fltmc help``` to see the full list of commands.

## Fsutil.exe Command

The [*Fsutil.exe*](/windows-server/administration/windows-commands/fsutil-file) program is a system-supplied command line utility that performs various operations on files. Developers can type ```fsutil file layout foo.md``` to pretty-print all the details of a file, such as its attributes, time stamps, streams, and so forth.

## !fltkd Debugger Extension

The !fltkd debugger extension is provided in the [Windows Debugging](../debugger/index.md) tools. Commonly used commands include the following:

| Command | Description |
| ------- | ----------- |
| **!cbd** | The filter manager equivalent of !irp |
| **!filter** | Lists detailed information about the specified filter |
| **!filters** | Lists all attached minifilter drivers |
| **!frames** | Lists all filter manager frames and attached minifilter drivers |
| **!instance** | Lists detailed information about the specified instance |
| **!volume** | Lists detailed information about the specified volume |
| **!volumes** | Lists all volumes and attached minifilter driver instances |

In WinDbg, type **!fltkd.help** for a full list of commands.

## Filter Verifier

Filter Verifier is an option in [Driver Verifier](../devtest/driver-verifier.md) that validates minifilter driver usage of filter manager functions. Filter Verifier is installed with the filter manager. Developers are strongly recommended to always develop minifilter drivers with Filter Verifier enabled.

For information on how to enable Filter Verifier and what it validates, please see [File System Filter Verification](../devtest/file-system-filter-verification.md).
