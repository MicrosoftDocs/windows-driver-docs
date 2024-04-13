---
title: ".ocommand (Expect Commands from Target)"
description: "The .ocommand command enables the target application to send commands to the debugger."
keywords: ["Expect Commands from Target (.ocommand) command", ".ocommand (Expect Commands from Target) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .ocommand (Expect Commands from Target)
api_type:
- NA
---

# .ocommand (Expect Commands from Target)


The **.ocommand** command enables the target application to send commands to the debugger.

```dbgcmd
.ocommand  String 
.ocommand -d 
.ocommand 
```

## <span id="ddk_meta_expect_commands_from_target_dbg"></span><span id="DDK_META_EXPECT_COMMANDS_FROM_TARGET_DBG"></span>Parameters


<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the command prefix string. *String* can include spaces, but you cannot use C-style control characters such as **\\"** and **\\n**. You can also enclose *String* in quotation marks. However, if *String* includes a semicolon, leading spaces, or trailing spaces, you must enclose *String* in quotation marks.

<span id="_______-d______"></span><span id="_______-D______"></span> **-d**   
Deletes the command prefix string.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes | user mode only |
|Targets | live debugging only |
|Platforms | all  |
 

## Additional Information

For more information about [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringw) and other user-mode functions that communicate with a debugger, see the Microsoft Windows SDK documentation.

## Remarks

If you use the **.ocommand** command without parameters, the debugger displays the current command prefix string. To clear the existing string, use **.ocommand -d**.

When you have set a command prefix string, any target output (such as the contents of an [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringw) command) is scanned. If this output begins with the command prefix string, the text of the output that follows the prefix string is treated as a debugger command string and is run. When this text is executed, the command string is not displayed.

The target can include an [**.echo (Echo Comment)**](-echo--echo-comment-.md) command in the output string if you want additional messages. Target output that does not begin with the prefix string is displayed in the typical manner.

After the commands within the command string have been executed, the target remains broken into the debugger, unless the final command is [**g (Go)**](g--go-.md).

The comparison between the command prefix string and the target output is not case sensitive. (However, subsequent uses of **.ocommand** display the string that you entered with the case preserved).

For this example, assume that you enter the following command in the debugger.

```dbgcmd
0:000> .ocommand magiccommand
```

Then, the target application executes the following line.

```dbgcmd
OutputDebugString("MagicCommand kb;g");
```

The debugger recognizes the command string prefix and executes **kb;g** immediately.

However, the following line does not cause any commands to be executed.

```dbgcmd
OutputDebugString("Command on next line.\nmagiccommand kb;g");
```

There are no commands executed from the preceding example because the command string prefix is not at the beginning of the output, even though it does begin a new line.

**Note**   You should choose a command string prefix that will not likely appear in any target output other than your own commands.

 

 


