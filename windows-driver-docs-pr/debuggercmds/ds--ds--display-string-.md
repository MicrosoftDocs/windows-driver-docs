---
title: "ds, dS (Display String)"
description: "The ds and dS commands display a STRING, ANSI_STRING, or UNICODE_STRING structure."
keywords: ["ds, dS (Display String) Windows Debugging"]
ms.date: 05/03/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- ds, dS (Display String)
api_type:
- NA
---

# ds, dS (Display String)


The **ds** and **dS** commands display a STRING, ANSI\_STRING, or UNICODE\_STRING *structures*. 

These commands do not display null-delimited character strings, but rather string structures.

If you have the address of the characters of a Unicode string then use the du command instead. Use the da command to display ASCII characters. For more information, see [d, da, db, dc, dd, dD, df, dp, dq, du, dw (Display Memory)](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md).

```dbgcmd
d{s|S} [/c Width] [Address]
```

## <span id="ddk_cmd_display_string_dbg"></span><span id="DDK_CMD_DISPLAY_STRING_DBG"></span>Parameters


<span id="_______s______"></span><span id="_______S______"></span> **s**   
Specifies that a STRING or ANSI\_STRING structure is to be displayed. (This **s** is case-sensitive.)

<span id="_______S______"></span><span id="_______s______"></span> **S**   
Specifies that a UNICODE\_STRING structure is to be displayed. (This **S** is case-sensitive.)

<span id="________c_______Width______"></span><span id="________c_______width______"></span><span id="________C_______WIDTH______"></span> **/c** *Width*   
Specifies the number of characters to display on each line. This number includes null characters, which will not be visible.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
The memory address where the where the UNICODE_STRING structure is stored. 

For more syntax details, see [Address and Address Range Syntax](address-and-address-range-syntax.md). If omitted, the last address used in a display command is assumed.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For an overview of memory manipulation and a description of other memory-related commands, see [Reading and Writing Memory](../debugger/reading-and-writing-memory.md).

## Remarks

If you want to display Unicode strings in the Locals window or Watch window of WinDbg, you need to use the [**.enable\_unicode (Enable Unicode Display)**](-enable-unicode--enable-unicode-display-.md) command first.

 


