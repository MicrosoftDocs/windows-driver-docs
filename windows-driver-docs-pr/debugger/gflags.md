---
title: GFlags
description: GFlags (the Global Flags Editor), gflags.exe, enables and disables advanced debugging, diagnostic, and troubleshooting features. 
ms.assetid: e268af2e-90a9-411e-8e29-ab486d2aac48
keywords: GFlags, Global Flags Editor, gflags.exe
ms.author: domars
ms.date: 06/12/2018
ms.localizationpriority: medium
---

# GFlags


GFlags (the Global Flags Editor), gflags.exe, enables and disables advanced debugging, diagnostic, and troubleshooting features. It is most often used to turn on indicators that other tools track, count, and log.

## <span id="Where_to_get_GFlags"></span><span id="where_to_get_gflags"></span><span id="WHERE_TO_GET_GFLAGS"></span>Where to get GFlags


GFlags is included in the [Debugging Tools for Windows 10 (WinDbg)](debugger-download-tools.md).

After the debugging tools are installed, gflags.exe for use on 64 bit Windows is installed by default to the following directory.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x64
```

If you are running a 32 bit version of Windows, use the 32 bit version of gflags.exe located here.

```console
C:\Program Files (x86)\Windows Kits\10\Debuggers\x86
```


## <span id="ddk_gflags_dtools"></span><span id="DDK_GFLAGS_DTOOLS"></span>Overview of GFlags


Driver developers and testers often use GFlags to turn on debugging, logging and test features, either directly, or by including GFlags commands in a test script. The page heap verification features can help you to identify memory leaks and buffer errors in kernel-mode drivers.

GFlags has both a dialog box and a command-line interface. Most features are available from both interfaces, but some features are accessible from only one of the interfaces. (See [GFlags Details](gflags-details.md).)

### <span id="new_features"></span><span id="NEW_FEATURES"></span>Features

-   Page heap verification. GFlags now includes the functions of PageHeap (pageheap.exe), a tool that enables heap allocation monitoring. PageHeap was included in previous versions of Windows.

-   No reboot required for the Special Pool feature. On Windows Vista and later versions of Windows, you can enable, disable, and configure the Special Pool feature without restarting ("rebooting") the computer. For information, see [Special Pool](special-pool.md).

-   Object Reference Tracing. A new flag enables tracing of object referencing and object dereferencing in the kernel. This new feature of Windows detects when an object reference count is decremented too many times or not decremented even though an object is no longer used. This flag is supported only in Windows Vista and later versions of Windows.

-   New dialog box design. The GFlags dialog box has tabbed pages for easier navigation.

### <span id="requirements"></span><span id="REQUIREMENTS"></span>Requirements

To use most GFlags features, including setting flags in the registry or in kernel mode, or enabling page heap verification, you must be a member of the Administrators group on the computer. However, prior to Windows Vista, users with at least Guest account access can launch a program from the **Global Flags** dialog box.

When features do not work, or work differently, on particular operating system versions, the differences are explained in the description of the feature.

This topic includes:

[GFlags Overview](gflags-overview.md)

[GFlags Details](gflags-details.md)

[**GFlags Commands**](gflags-commands.md)

[GFlags Flag Table](gflags-flag-table.md)

[GFlags and PageHeap](gflags-and-pageheap.md)

[Global Flags Dialog Box](global-flags-dialog-box.md)

[GFlags Examples](gflags-examples.md)

[Global Flag Reference](global-flag-reference.md)

**Note**   Incorrect use of this tool can degrade system performance or prevent Windows from starting, requiring you to reinstall Windows.

 

**Important**  Pool tagging is permanently enabled on Windows Server 2003 and later versions of Windows, including Windows Vista. On these systems, the **Enable pool tagging** check box on the **Global Flags** dialog box is dimmed and commands to enable or disable pool tagging fail.

 

## <span id="related_topics"></span>Related topics


[Tools Included in Debugging Tools for Windows](extra-tools.md)

 

 






