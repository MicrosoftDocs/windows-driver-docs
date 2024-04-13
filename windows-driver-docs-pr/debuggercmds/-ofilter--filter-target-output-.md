---
title: ".ofilter (Filter Target Output)"
description: "The .ofilter command filters the output from the target application or target computer."
keywords: ["Filter Target Output (.ofilter) command", ".ofilter (Filter Target Output) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .ofilter (Filter Target Output)
api_type:
- NA
---

# .ofilter (Filter Target Output)


The **.ofilter** command filters the output from the target application or target computer.

```dbgcmd
.ofilter [/!] String 
.ofilter "" 
.ofilter 
```

## <span id="ddk_meta_filter_target_output_dbg"></span><span id="DDK_META_FILTER_TARGET_OUTPUT_DBG"></span>Parameters


<span id="_______________"></span> **/!**   
Reverses the filter so that the debugger displays only output that does not contain *String*. If you do not use this parameter, the debugger displays only output that contains *String*.

<span id="_______String______"></span><span id="_______string______"></span><span id="_______STRING______"></span> *String*   
Specifies the string to match in the target's output. *String* can include spaces, but you cannot use C-style control characters such as **\\"** and **\\n**. *String* might contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

You can enclose *String* in quotation marks. However, if *String* includes a semicolon, leading spaces, or trailing spaces, you must use quotation marks. Alphanumeric characters in *String* are converted to uppercase letters, but the actual pattern matching is case insensitive.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringw) and other user-mode routines, see the Microsoft Windows SDK documentation. For more information about **DbgPrint**, **DbgPrintEx**, and other kernel-mode routines, see the Windows Driver Kit (WDK).

## Remarks

If you use the **.ofilter** command without parameters, the debugger displays the current pattern-matching criteria.

To clear the existing filter, use **.ofilter ""**. This command filters any data that is sent by user-mode routines (such as [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringw)) and kernel-mode routines (such as **DbgPrint**). However, the debugger always displays prompts that **DbgPrompt** sends.

The **DbgPrintEx** and **KdPrintEx** routines supply another method of filtering debugging messages that you do not want.

 


