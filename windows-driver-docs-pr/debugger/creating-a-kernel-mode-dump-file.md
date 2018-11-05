---
title: Creating a Kernel-Mode Dump File
description: Creating a Kernel-Mode Dump File
ms.assetid: d3eb86b2-eba7-4ddb-90e9-0e26414436fb
keywords: ["dump file, creating kernel-mode dump file", "dump file, NMI switch", "NMI switch"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





