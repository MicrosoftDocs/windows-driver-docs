---
title: Small Memory Dump
description: Small Memory Dump
ms.assetid: bc502411-5366-49d3-b650-9dddda286934
keywords: ["dump file, Small Memory Dump", "Small Memory Dump"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Small Memory Dump


## <span id="ddk_small_memory_dump_dbg"></span><span id="DDK_SMALL_MEMORY_DUMP_DBG"></span>


A *Small Memory Dump* is much smaller than the other two kinds of kernel-mode crash dump files. It is exactly 64 KB in size, and requires only 64 KB of pagefile space on the boot drive.

This dump file includes the following:

-   The bug check message and parameters, as well as other blue-screen data.

-   The processor context (PRCB) for the processor that crashed.

-   The process information and kernel context (EPROCESS) for the process that crashed.

-   The thread information and kernel context (ETHREAD) for the thread that crashed.

-   The kernel-mode call stack for the thread that crashed. If this is longer than 16 KB, only the topmost 16 KB will be included.

-   A list of loaded drivers.

In Windows XP and later versions of Windows, the following items are also included:

-   A list of loaded modules and unloaded modules.

-   The debugger data block. This contains basic debugging information about the system.

-   Any additional memory pages that Windows identifies as being useful in debugging failures. This includes the data pages that the registers were pointing to when the crash occurred, and other pages specifically requested by the faulting component.

-   (Windows Server 2003 and later) The Windows SKU -- for example, "Professional" or "Server".

This kind of dump file can be useful when space is greatly limited. However, due to the limited amount of information included, errors that were not directly caused by the thread executing at time of crash may not be discovered by an analysis of this file.

Since this kind of dump file does not contain images of any executables residing in memory at the time of the crash, you may also need to set the executable image path if these executables turn out to be important.

If a second bug check occurs and a second Small Memory Dump file is created, the previous file will be preserved. Each additional file will be given a distinct name, which contains the date of the crash encoded in the filename. For example, mini022900-01.dmp is the first memory dump file generated on February 29, 2000. A list of all Small Memory Dump files is kept in the directory %SystemRoot%\\Minidump.

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Small%20Memory%20Dump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





