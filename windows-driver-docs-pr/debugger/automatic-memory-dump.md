---
title: Automatic Memory Dump
description: Automatic Memory Dump
ms.assetid: A2C71497-7865-4DC8-B760-6121B224737A
---

# Automatic Memory Dump


## <span id="ddk_kernel_memory_dump_dbg"></span><span id="DDK_KERNEL_MEMORY_DUMP_DBG"></span>


An *Automatic Memory Dump* contains the same information as a [Kernel Memory Dump](kernel-memory-dump.md). The difference between the two is not in the dump file itself, but in the way that Windows sets the size of the system paging file.

If the system paging file size is set to **System managed size**, and the kernel-mode crash dump is set to **Automatic Memory Dump**, then Windows can set the size of the paging file to less than the size of RAM. In this case, Windows sets the size of the paging file large enough to ensure that a kernel memory dump can be captured most of the time.

If the computer crashes and the paging file is not large enough to capture a kernel memory dump, Windows increases the size of the paging file to at least the size of RAM. The time of this event is recorded here in the Registry:

**HKLM**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**CrashControl**\\**LastCrashTime**

The increased paging file size stays in place for 4 weeks and then returns to the smaller size. If you want to return to the smaller paging file before 4 weeks, you can delete the Registry entry.

To see the paging file settings, go to **Control Panel &gt; System and Security &gt; System &gt; Advanced system settings**. Under **Performance**, click **Settings**. On the **Advanced** tab, under **Virtual memory**, click **Change**. In the Virtual Memory dialog box, you can see the paging file settings.

![screen shot of the virtual memory dialog box.](images/virtualmemorydialog.png)

The Automatic Memory Dump file is written to %SystemRoot%\\Memory.dmp by default.

The Automatic Memory Dump is available in Windows 8 and later.

**Note**  To suppress missing page error messages when debugging an Automatic Memory Dump, use the [**.ignore\_missing\_pages**](https://msdn.microsoft.com/library/windows/hardware/ff563226) command.

 

## <span id="related_topics"></span>Related topics


[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Automatic%20Memory%20Dump%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





