---
title: "ur (Unassemble Real Mode BIOS)"
description: "The ur command displays an assembly translation of the specified 16-bit real-mode code."
keywords: ["ur (Unassemble Real Mode BIOS) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- ur (Unassemble Real Mode BIOS)
api_type:
- NA
---

# ur (Unassemble Real Mode BIOS)


The **ur** command displays an assembly translation of the specified 16-bit real-mode code.

```dbgcmd
ur Range 
ur Address
ur 
```

## <span id="ddk_cmd_unassemble_real_mode_bios_dbg"></span><span id="DDK_CMD_UNASSEMBLE_REAL_MODE_BIOS_DBG"></span>Parameters


<span id="_______Range______"></span><span id="_______range______"></span><span id="_______RANGE______"></span> *Range*   
Specifies the memory range that contains the instructions to disassemble. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the beginning of the memory range to disassemble. Eight instructions on an x86-based processor are unassembled. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Additional Information

For more information about how to debug BIOS code, see [Debugging BIOS Code](../debugger/debugging-bios-code.md).

## Remarks

If you do not specify *Range* or *Address*, the disassembly begins at the current address and extends eight instructions on an x86-based processor.

If you are examining 16-bit real-mode code on an x86-based processor, both the **ur** command and the [**u (Unassemble)**](u--unassemble-.md) command give correct results.

However, if real-mode code exists in a location where the debugger is not expecting it (for example, a non-x86 computer that is running or emulating x86-based BIOS code from a plug-in card), you must use **ur** to correctly disassemble this code.

If you use **ur** on 32-bit or 64-bit code, the command tries to disassemble the code as if it were 16-bit code. This situation produces meaningless results.

