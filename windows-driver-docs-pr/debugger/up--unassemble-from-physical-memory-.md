---
title: up (Unassemble from Physical Memory)
description: The up command displays an assembly translation of the specified program code in physical memory.
keywords: ["up (Unassemble from Physical Memory) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- up (Unassemble from Physical Memory)
api_type:
- NA
---

# up (Unassemble from Physical Memory)


The **up** command displays an assembly translation of the specified program code in physical memory.

```dbgcmd
up Range 
up Address 
up 
```

## <span id="ddk_cmd_unassemble_dbg"></span><span id="DDK_CMD_UNASSEMBLE_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range in physical memory that contains the instructions to disassemble. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the beginning of the memory range in physical memory to disassemble. Eight instructions on an x86-based processor are unassembled. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

## Remarks

If you do not specify a parameter for the **up** command, the disassembly begins at the current address and extends eight instructions on an x86-based processor.

Do not confuse this command with the [**u (Unassemble)**](u--unassemble-.md). The **up** command disassembles only physical memory, while the **u** command disassembles only virtual memory.

 

 





