---
title: Kernel Memory Dump
description: Kernel Memory Dump
ms.assetid: 466f5b92-c9bd-4050-9ef8-469979ba0cbe
keywords: ["dump file, Kernel Memory Dump", "Kernel Memory Dump"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Kernel Memory Dump


## <span id="ddk_kernel_memory_dump_dbg"></span><span id="DDK_KERNEL_MEMORY_DUMP_DBG"></span>


A *Kernel Memory Dump* contains all the memory in use by the kernel at the time of the crash.

This kind of dump file is significantly smaller than the Complete Memory Dump. Typically, the dump file will be around one-third the size of the physical memory on the system. This quantity will vary considerably, depending on your circumstances.

This dump file will not include unallocated memory, or any memory allocated to user-mode applications. It only includes memory allocated to the Windows kernel and hardware abstraction level (HAL), as well as memory allocated to kernel-mode drivers and other kernel-mode programs.

For most purposes, this crash dump is the most useful. It is significantly smaller than the Complete Memory Dump, but it only omits those portions of memory that are unlikely to have been involved in the crash.

Since this kind of dump file does not contain images of any user-mode executables residing in memory at the time of the crash, you may also need to set the executable image path if these executables turn out to be important.

The Kernel Memory Dump file is written to %SystemRoot%\\Memory.dmp by default.

If a second bug check occurs and another Kernel Memory Dump (or Complete Memory Dump) is created, the previous file will be overwritten.

To suppress missing page error messages when debugging a Kernel Memory Dump, use the [**.ignore\_missing\_pages**](-ignore-missing-pages--suppress-missing-page-errors-.md) command.

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Kernel%20Memory%20Dump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





