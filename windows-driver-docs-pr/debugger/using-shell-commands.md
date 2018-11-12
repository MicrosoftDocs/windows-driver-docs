---
title: Using Shell Commands
description: Using Shell Commands
ms.assetid: 16df2592-0e7d-4cd3-bc35-5323578cf555
keywords: ["shell commands", "shell commands, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Shell Commands


## <span id="ddk_using_shell_commands_dbg"></span><span id="DDK_USING_SHELL_COMMANDS_DBG"></span>


The debugger can transmit certain commands to the Microsoft Windows environment in which the debugger is running.

You can use the [**.shell (Command Shell)**](-shell--command-shell-.md) command in any Windows debugger. With this command, you can execute an application or a Microsoft MS-DOS command directly from the debugger. If you are performing [remote debugging](remote-debugging.md), these shell commands are executed on the server.

The [**.noshell (Prohibit Shell Commands)**](-noshell--prohibit-shell-commands-.md) command or the **-noshell** [command-line option](command-line-options.md) disables all shell commands. The commands are disabled while the debugger is running, even if you begin a new debugging session. The commands remain disabled even if you issue a [**.restart (Restart Kernel Connection)**](-restart--restart-kernel-connection-.md) command in KD.

If you are running a debugging server,you might want to disable shell commands. If the shell is available, a remote connection can use the **.shell** command to change your computer.

### <span id="network_drive_control"></span><span id="NETWORK_DRIVE_CONTROL"></span>Network Drive Control

In WinDbg, you can use the [File | Map Network Drive](file---map-network-drive.md) and [File | Disconnect Network Drive](file---disconnect-network-drive.md) commands to control the network drive mappings. These changes always occur on the computer that WinDbg is running on, never on any computer that is remotely connected to WinDbg.

 

 





