---
title: Opening a Dump File Using CDB
description: Opening a Dump File Using CDB
ms.assetid: 204DFA6F-2BA2-4B76-AFE0-28207710322B
ms.author: domars
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Opening a Dump File Using CDB


## <span id="Command_Prompt"></span><span id="command_prompt"></span><span id="COMMAND_PROMPT"></span>Command Prompt


In a Command Prompt window, you can open a user-mode dump file when you launch CDB. Enter the following command.

**cdb -y** *SymbolPath* **-i** *ImagePath* **-z** *DumpFileName*

The **-v** option (verbose mode) is also useful. For more information about the command-line syntax, see [**CDB Command-Line Options**](cdb-command-line-options.md)

## <span id="CDB_Command_Line"></span><span id="cdb_command_line"></span><span id="CDB_COMMAND_LINE"></span>CDB Command Line


You can also open a dump file after the debugger is running by entering the [**.opendump (Open Dump File)**](-opendump--open-dump-file-.md) command, followed by [**g (Go)**](g--go-.md). This allows you to debug multiple dump files at the same time.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Opening%20a%20Dump%20File%20Using%20CDB%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




