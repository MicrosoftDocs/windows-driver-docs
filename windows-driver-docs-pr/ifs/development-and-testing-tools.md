---
title: Development and Testing Tools
description: Development and Testing Tools
keywords:
- filter manager WDK file system minifilter , tools
- Fltmc.exe WDK file system minifilter
- fltkd debugger extension WDK file system minifilter
- Filter Verifier WDK file system minifilter
- Verifier utility
ms.date: 08/21/2020
---

# Development and Testing Tools

Several filter manager tools are available for use. Minifilter driver developers are also encouraged to use general-purpose kernel-mode development and testing tools, such as PREfast with driver-specific rules.

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

Filter Verifier is an [I/O Verification](../devtest/i-o-verification.md) option in [Driver Verifier](../devtest/driver-verifier.md) that validates minifilter driver usage of filter manager functions. Filter Verifier is installed with the filter manager. Developers should always develop minifilter drivers with Driver Verifier and Filter Verifier enabled.

To use Filter Verifier, specify the minifilter driver's name and enable the I/O Verification option in Driver Verifier (*Verifier.exe*). Verification starts when the minifilter driver registers with the filter manager.

Filter Verifier validates the following usage in a minifilter driver:

* Correct use of parameters and calling context
* Correct return values from preoperation and postoperation callback routines
* Consistent and coherent changes to parameters in callback data

Filter Verifier tracks the following filter manager objects:

* Contexts
* Callback Data structures
* Queued Work Items
* NameInformation structures
* File Objects
* Filter Objects
* Instance Objects
* Volume Objects

In a command prompt, type ```verifier /?``` to see syntax and a full list of parameters.
