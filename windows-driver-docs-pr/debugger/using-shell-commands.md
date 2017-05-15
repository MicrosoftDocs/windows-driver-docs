---
title: Using Shell Commands
description: Using Shell Commands
ms.assetid: 16df2592-0e7d-4cd3-bc35-5323578cf555
keywords: ["shell commands", "shell commands, overview"]
---

# Using Shell Commands


## <span id="ddk_using_shell_commands_dbg"></span><span id="DDK_USING_SHELL_COMMANDS_DBG"></span>


The debugger can transmit certain commands to the Microsoft Windows environment in which the debugger is running.

You can use the [**.shell (Command Shell)**](-shell--command-shell-.md) command in any Windows debugger. With this command, you can execute an application or a Microsoft MS-DOS command directly from the debugger. If you are performing [remote debugging](remote-debugging.md), these shell commands are executed on the server.

The [**.noshell (Prohibit Shell Commands)**](-noshell--prohibit-shell-commands-.md) command or the **-noshell** [command-line option](command-line-options.md) disables all shell commands. The commands are disabled while the debugger is running, even if you begin a new debugging session. The commands remain disabled even if you issue a [**.restart (Restart Kernel Connection)**](-restart--restart-kernel-connection-.md) command in KD.

If you are running a debugging server,you might want to disable shell commands. If the shell is available, a remote connection can use the **.shell** command to change your computer.

### <span id="network_drive_control"></span><span id="NETWORK_DRIVE_CONTROL"></span>Network Drive Control

In WinDbg, you can use the [File | Map Network Drive](file---map-network-drive.md) and [File | Disconnect Network Drive](file---disconnect-network-drive.md) commands to control the network drive mappings. These changes always occur on the computer that WinDbg is running on, never on any computer that is remotely connected to WinDbg.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20Shell%20Commands%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




