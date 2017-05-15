---
title: Kill Tool
description: The Kill tool, kill.exe, terminates one or more processes and all of their threads. This tool works only on processes running on the local computer.
ms.assetid: e1733a74-2a31-436f-87b8-e704b27b6f04
keywords: ["Kill Tool", "Kill.exe", "Kill.exe, See "Kill Tool""]
---

# Kill Tool


The Kill tool, kill.exe, terminates one or more processes and all of their threads. This tool works only on processes running on the local computer.

## <span id="Where_to_get_Kill_Tool"></span><span id="where_to_get_kill_tool"></span><span id="WHERE_TO_GET_KILL_TOOL"></span>Where to get Kill Tool


Kill.exe is included in [Debugging Tools for Windows](introduction6.md).

## <span id="Kill_Tool_command-line_options"></span><span id="kill_tool_command-line_options"></span><span id="KILL_TOOL_COMMAND-LINE_OPTIONS"></span>Kill Tool command-line options


``` syntax
kill [/f] { PID | Pattern* }
```

### <span id="ddk_kill_tool_commands_dtools"></span><span id="DDK_KILL_TOOL_COMMANDS_DTOOLS"></span>Parameters

<span id="________f______"></span><span id="________F______"></span> **/f**   
Forces the termination of the process without prompting the user for confirmation. This option is required to terminate a protected process, such as a system service.

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Specifies the process identifier (PID) of the task to be terminated.

To find the PID for a task, use TaskList in Microsoft Windows XP and later or [TList](tlist.md) in Windows 2000.

<span id="_______Pattern_"></span><span id="_______pattern_"></span><span id="_______PATTERN_"></span> *Pattern***\***  
Specifies all or part of the name of a task or window. The Kill tool terminates all processes whose process names or window names match the pattern. The asterisk is required.

Before using a pattern that might match many process or window names unintentionally, use the **tlist** *pattern* command to test the pattern. See [TList](tlist.md) for details.

## <span id="Examples"></span><span id="examples"></span><span id="EXAMPLES"></span>Examples


The following command terminates processes whose names begin with "myapp."

```
kill myapp*
```

The following command terminates the process whose process ID (PID) is 2520:

```
kill 2520
```

The following command terminates processes whose names begin with "my\*." It does not prompt for confirmation. This command succeeds even when this process is a system service:

```
kill /f my*
```

## <span id="related_topics"></span>Related topics


[Tools Included in Debugging Tools for Windows](extra-tools.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Kill%20Tool%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





