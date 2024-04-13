---
title: "l+, l- (Set Source Options)"
description: "The l+and l- commands set the source line options that control source display and program stepping options."
keywords: ["l+, l- (Set Source Options) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- l+, l- (Set Source Options)
api_type:
- NA
---

# l+, l- (Set Source Options)

The <strong>l+</strong>and **l-** commands set the source line options that control source display and program stepping options.

```dbgcmd
l+Option
l-Option
l{+|-}
```

## Parameters

**+** or **-**  
Specifies whether a given option is to be turned on (plus sign \[+\])or turned off (minus sign \[-\]).

*Option*

One of the following options. The options must be in lowercase letters.

**l**

Displays source line numbers at the command prompt. You can disable source line display through l-ls or .prompt\_allow -src. To make the source line numbers visible, you must enable source line display through both mechanisms.

**o**

Hides all messages (other than the source line and line number) when you are stepping through code. (The **s** option must also be active for the **o** option to have any effect.)

**s**  
Displays source lines and source line numbers at the command prompt.

**t**  

Starts [source mode](../debugger/debugging-in-source-mode.md). If this mode is not set, the debugger is in [assembly mode](../debugger/debugging-in-assembly-mode.md).

**\***  
Turns on or turns off all options.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

## Additional Information

For more information about source debugging and related commands, see [Debugging in Source Mode](../debugger/debugging-in-source-mode.md). For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](../debugger/debugging-in-assembly-mode.md).

## Remarks

If you omit *Option*, the previously set options are displayed. In this case, the **l+** and **l-** commands have identical effects. However, you must include a plus sign (**+**) or minus sign (-) for the **l** command to work.

You can include only one *Option* every time that you issue this command. If you list more than one option, only the first option is detected. However, by repeatedly issuing this command, you can turn on or off as many options as you want. (In other words, **l+lst** does not work, but **l+l; l+s; l+t** does achieve the effect that you want.)

When you specify the **s** option, source lines and line numbers are displayed when you step through code, regardless of whether you specified the **l** option. The **o** option has no effect unless you specify the **s** option.

Source line options do not take effect unless you enable line number loading by using the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command or the [-lines command-line option](../debugger/command-line-options.md). By default, if you have not used these commands, WinDbg turns on source line support and CDB turns it off.

