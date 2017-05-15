---
title: Executing a Debugger Command Program
description: Executing a Debugger Command Program
ms.assetid: ad28a5d6-0d6a-42c0-82f3-6760a8c773ab
keywords: ["debugger command program, execution"]
---

# Executing a Debugger Command Program


## <span id="ddk_debugger_command_program_execution_dbg"></span><span id="DDK_DEBUGGER_COMMAND_PROGRAM_EXECUTION_DBG"></span>


You can execute a debugger command program in one of the following ways:

-   Enter all of the statements in the [Debugger Command window](debugger-command-window.md) as a single string, with individual statements and commands separated by semicolons.

-   Add all of the statements in a script file on a single line, with individual statements and commands separated by semicolons. Then, run this script file by using one of the methods described in [Using Script Files](using-script-files.md).

-   Add all of the statements in a script file, with each statement on a separate line. (Alternatively, separate statements by any combination of carriage returns and semicolons.) Then, run this script file by using the [**$&gt;&lt; (Run Script File)**](-----------------------a---run-script-file-.md) or **$$&gt;&lt; (Run Script File)** command. These commands open the specified script file, replace all carriage returns with semicolons, and execute the resulting text as a single command block.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Executing%20a%20Debugger%20Command%20Program%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




