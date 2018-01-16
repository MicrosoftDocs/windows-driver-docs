---
title: Creating a Kernel-Mode Dump File
description: Creating a Kernel-Mode Dump File
ms.assetid: d3eb86b2-eba7-4ddb-90e9-0e26414436fb
keywords: ["dump file, creating kernel-mode dump file", "dump file, NMI switch", "NMI switch"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Creating a Kernel-Mode Dump File


## <span id="ddk_creating_a_kernel_mode_dump_file_dbg"></span><span id="DDK_CREATING_A_KERNEL_MODE_DUMP_FILE_DBG"></span>


There are three ways in which a kernel-mode dump file can be created:

1.  You can enable the dump file from the Control Panel, and then the system can crash on its own.

2.  You can enable the dump file from the Control Panel, and then force the system to crash.

3.  You can use the debugger to create a dump file without crashing the system.

This section includes:

[Enabling a Kernel-Mode Dump File](enabling-a-kernel-mode-dump-file.md)

[Forcing a System Crash](forcing-a-system-crash.md)

[Creating a Dump File Without a System Crash](creating-a-dump-file-without-a-system-crash.md)

[Verifying the Creation of a Kernel-Mode Dump File](verifying-the-creation-of-a-kernel-mode-dump-file.md)

### <span id="using_an_nmi_switch"></span><span id="USING_AN_NMI_SWITCH"></span>Using an NMI Switch

It is also possible to use an NMI switch to create a crash dump file. Contact your hardware vendor to determine whether your machine has this switch.

The usage of NMI switches is not covered in this documentation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Creating%20a%20Kernel-Mode%20Dump%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




