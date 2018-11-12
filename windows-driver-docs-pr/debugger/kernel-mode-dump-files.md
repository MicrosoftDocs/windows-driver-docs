---
title: Kernel-Mode Dump Files
description: Kernel-Mode Dump Files
ms.assetid: f04dc580-0e14-41aa-88a2-e04f4406add8
keywords: ["dump file, kernel mode"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Kernel-Mode Dump Files


## <span id="ddk_kernel_mode_dump_files_dbg"></span><span id="DDK_KERNEL_MODE_DUMP_FILES_DBG"></span>


When a kernel-mode error occurs, the default behavior of Microsoft Windows is to display the blue screen with bug check data.

However, there are several alternative behaviors that can be selected:

-   A kernel debugger (such as WinDbg or KD) can be contacted.

-   A memory dump file can be written.

-   The system can automatically reboot.

-   A memory dump file can be written, and the system can automatically reboot afterwards.

This section covers how to create and analyze a kernel-mode memory dump file. There are three different varieties of crash dump files. However, it should be remembered that no dump file can ever be as useful and versatile as a live kernel debugger attached to the system that has failed.

This section includes:

[Varieties of Kernel-Mode Dump Files](varieties-of-kernel-mode-dump-files.md)

[Creating a Kernel-Mode Dump File](creating-a-kernel-mode-dump-file.md)

[Analyzing a Kernel-Mode Dump File](analyzing-a-kernel-mode-dump-file.md)

 

 





