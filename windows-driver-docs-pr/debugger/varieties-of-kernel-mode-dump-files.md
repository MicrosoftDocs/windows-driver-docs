---
title: Varieties of Kernel-Mode Dump Files
description: Varieties of Kernel-Mode Dump Files
ms.assetid: 6db2a755-ed9c-492a-a650-9ae34ae59968
keywords: ["dump file, kernel-mode file types"]
---

# Varieties of Kernel-Mode Dump Files


## <span id="ddk_varieties_of_kernel_mode_dump_files_dbg"></span><span id="DDK_VARIETIES_OF_KERNEL_MODE_DUMP_FILES_DBG"></span>


There are five settings for kernel-mode crash dump files:

[Complete Memory Dump](complete-memory-dump.md)

[Kernel Memory Dump](kernel-memory-dump.md)

[Small Memory Dump](small-memory-dump.md)

[Automatic Memory Dump](automatic-memory-dump.md)

[Active Memory Dump](debugger-active_memory_dump)

The difference between these dump files is one of size. The *Complete Memory Dump* is the largest and contains the most information, the *Kernel Memory Dump* is somewhat smaller, and the *Small Memory Dump* is only 64 KB in size.

If you select *Automatic Memory Dump*, the dump file is the same as a Kernel Memory Dump, but Windows has more flexibility in setting the size of the system paging file.

The advantage to the larger files is that, since they contain more information, they are more likely to help you find the cause of the crash.

The advantage of the smaller files is that they are smaller and written more quickly. Speed is often valuable; if you are running a server, you may want the server to reboot as quickly as possible after a crash, and the reboot will not take place until the dump file has been written.

After a Complete Memory Dump or Kernel Memory Dump has been created, it is possible to create a Small Memory Dump file from the larger dump file. See the [**.dump (Create Dump File)**](https://msdn.microsoft.com/library/windows/hardware/ff562428) command for details.

**Note**   Much information can be obtained by analyzing a kernel-mode dump file. However, no kernel-mode dump file can provide as much information as actually debugging the crash directly with a kernel debugger.

 

## <span id="related_topics"></span>Related topics


[Kernel-Mode Dump Files](kernel-mode-dump-files.md)

[Enabling a Kernel-Mode Dump File](enabling-a-kernel-mode-dump-file.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Varieties%20of%20Kernel-Mode%20Dump%20Files%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





