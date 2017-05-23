---
title: Crashing and Rebooting the Target Computer
description: This topic covers crashing and rebooting the Target Computer
ms.assetid: 7480e572-05ca-40c6-aa91-b1ab35e4496b
keywords: ["controlling the target, crashing the target computer", "controlling the target, rebooting the target computer", "reboot", "reboot, See "boot process"", "boot process", "boot process, debugging during", "system crash, deliberately causing", "bug check, deliberately causing"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Crashing%20and%20Rebooting%20the%20Target%20Computer%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




