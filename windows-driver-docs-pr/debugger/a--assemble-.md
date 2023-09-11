---
title: a (Assemble)
description: The a command assembles 32-bit x86 instruction mnemonics and puts the resulting instruction codes into memory.
keywords: ["Assemble (a) command", "assembly debugging, Assemble (a) command", "a (Assemble) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- a (Assemble)
api_type:
- NA
---

# a (Assemble)


The **a** command assembles 32-bit x86 instruction mnemonics and puts the resulting instruction codes into memory.

```dbgcmd
a [Address]
```

## <span id="DDK_CMD_ASSEMBLE_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the beginning of the block in memory where the resulting codes are put. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

### Additional Information

For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

## Remarks

The **a** command does not support 64-bit instruction mnemonics. However, the **a** command is enabled regardless of whether you are debugging a 32-bit target or a 64-bit target. Because of the similarities between x86 and x64 instructions, you can sometimes use the **a** command successfully when debugging a 64-bit target.

If you do not specify an address, the assembly starts at the address that the current value of the instruction pointer specifies. To assemble a new instruction, type the desired mnemonic and press ENTER. To end assembly, press only ENTER.

Because the assembler searches for all of the symbols that are referred to in the code, this command might take time to complete. During this time, you cannot press [**CTRL+C**](ctrl-c--break-.md)to end the **a** command.

 

 





