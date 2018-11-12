---
title: Debug Kernel Connection Cycle Initial Break
description: Debug Kernel Connection Cycle Initial Break
ms.assetid: e4dbb810-d9b3-4721-89ec-af4b5e244cc0
keywords: ["Debug Kernel Connection Cycle Initial Break"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug | Kernel Connection | Cycle Initial Break


## <span id="ddk_debug_kernel_connection_cycle_initial_break_dbg"></span><span id="DDK_DEBUG_KERNEL_CONNECTION_CYCLE_INITIAL_BREAK_DBG"></span>


Point to **Kernel Conection** and then click **Cycle Initial Break** on the **Debug** menu to change the conditions on which the debugger automatically breaks into the target computer.

This command is equivalent to pressing CTRL+ALT+K. (You can also press CTRL+K in KD.)

This command causes the kernel debugger to cycle through the following three states:

<span id="No_break"></span><span id="no_break"></span><span id="NO_BREAK"></span>**No break**  
The debugger does not break into the target computer unless you press [CTRL+BREAK](debug---break.md) or Debug | Break.

<span id="Break_on_reboot"></span><span id="break_on_reboot"></span><span id="BREAK_ON_REBOOT"></span>**Break on reboot**  
The debugger breaks into a restarted target computer after the kernel initializes. This command is equivalent to starting WinDbg with the -b [**command-line option**](windbg-command-line-options.md).

<span id="Break_on_first_module_load"></span><span id="break_on_first_module_load"></span><span id="BREAK_ON_FIRST_MODULE_LOAD"></span>**Break on first module load**  
The debugger breaks into a restarted target computer after the first kernel module is loaded. (This action causes the break to occur earlier than in the **Break on reboot** state.) This command is equivalent to starting WinDbg with the -d [**command-line option**](windbg-command-line-options.md).

When you use the **Cycle Initial Break** command, the new break state is displayed.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about related commands and an explanation of how the restart process affects the debugger, see [Crashing and Rebooting the Target Computer](crashing-and-rebooting-the-target-computer.md).

 

 





