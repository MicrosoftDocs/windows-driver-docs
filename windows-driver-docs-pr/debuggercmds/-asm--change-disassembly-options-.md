---
title: .asm (Change Disassembly Options)
description: The .asm command controls how disassembly code will be displayed.
keywords: ["Change Disassembly Options (.asm) command", "assembly debugging, Change Disassembly Options (.asm) command", ".asm (Change Disassembly Options) Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- .asm (Change Disassembly Options)
api_type:
- NA
---

# .asm (Change Disassembly Options)


The **.asm** command controls how disassembly code will be displayed.

```dbgcmd
    .asm 
    .asm[-] Options
```

## <span id="ddk_meta_change_disassembly_options_dbg"></span><span id="DDK_META_CHANGE_DISASSEMBLY_OPTIONS_DBG"></span>Parameters


<span id="_______-______"></span> **-**   
Causes the specified options to be disabled. If no minus sign is used, the specified options will be enabled.

*Options*
Can be any number of the following options:

<span id="ignore_output_width"></span><span id="IGNORE_OUTPUT_WIDTH"></span>**ignore\_output\_width**  
Prevents the debugger from checking the width of lines in the disassembly display.

<span id="no_code_bytes"></span><span id="NO_CODE_BYTES"></span>**no\_code\_bytes**  
(x86 and x64 targets only) Suppresses the display of raw bytes.

<span id="source_line"></span><span id="SOURCE_LINE"></span>**source\_line**  
Prefixes each line of disassembly with the line number of the source code.

<span id="verbose"></span><span id="VERBOSE"></span>**verbose**  
(Itanium target only) Causes bundle-type information to be displayed along with the standard disassembly information.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For a description of assembly debugging and related commands, see [Debugging in Assembly Mode](../debugger/debugging-in-assembly-mode.md).

## Remarks

Using **.asm** by itself displays the current state of the options.

This command affects the display of any disassembly instructions in the Debugger Command window. In WinDbg it also changes the contents of the Disassembly window.

 

 





