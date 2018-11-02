---
title: Crashing and Rebooting the Target Computer
description: This topic covers crashing and rebooting the Target Computer
ms.assetid: 7480e572-05ca-40c6-aa91-b1ab35e4496b
keywords: debugging, debug, controlling the target, crashing the target computer, rebooting the target computer, reboot, boot process, system crash, bug check
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Crashing and Rebooting the Target Computer


## <span id="ddk_crashing_and_rebooting_the_target_computer_dbg"></span><span id="DDK_CRASHING_AND_REBOOTING_THE_TARGET_COMPUTER_DBG"></span>


When you perform kernel debugging, you can cause the target computer to stop responding (that is, *crash* or *bug check*) by issuing the [**.crash (Force System Crash)**](-crash--force-system-crash-.md) command. This command immediately causes the target computer to stop responding. The debugger writes a kernel-mode dump file if you have enabled crash dumps. (For more information about these files, see [Creating a Kernel-Mode Dump File](creating-a-kernel-mode-dump-file.md).)

To restart the target computer, use the [**.reboot (Reboot Target Computer)**](-reboot--reboot-target-computer-.md) command.

If you want the target computer to create a crash dump file and then restart, you should issue the **.crash** command, followed by the **.reboot** command. If you want only to restart, the **.crash** command is not required.

In the early stages of the boot process, the connection between the host computer and the target computer is lost. No information about the target computer is available to the debugger.

After the connection is broken, the debugger closes all symbol files and unloads all debugger extensions. At this point, all breakpoints are lost if you are running KD or CDB. In WinDbg, you can save the current workspace. This action saves all breakpoints.

If you want to end the debugging session at this point, use the [**CTRL+B**](ctrl-b--quit-local-debugger-.md) command (in KD) or click **Exit** on the **File** menu (in WinDbg).

If you do not exit the debugger, the connection is reestablished after enough of the boot process has completed. Symbols and extensions are reloaded at this point. If you are running WinDbg, the kernel-mode workspace is reloaded.

You can tell the debugger to automatically break into the target computer during the restart process at two possible times:

-   When the first kernel module is loaded into memory

-   When the kernel initializes

To set an automatic breakpoint when the first kernel module loads, use the **-d** [command-line option](command-line-options.md).

You can also change the break state after the debugger is running:

-   Control the initial module load and kernel initialization breakpoints like all exceptions and events. You can break into the debugger when these events occur, or ignore them. You can also have a specified command automatically execute when these breakpoints are hit. For more information, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

-   Use the [**CTRL+K**](ctrl-k--change-post-reboot-break-state-.md) shortcut keys in KD, the [CTRL+ALT+K](debug---kernel-connection---cycle-initial-break.md) shortcut keys in WinDbg, and the Debug | Kernel Connection | Cycle Initial Break command in WinDbg to change the break state. Every time that you use these commands, the debugger switches between three states: no automatic break, break upon kernel initialization, and break on first kernel module load. This method cannot activate both automatic breakpoints at the same time.

 

 





