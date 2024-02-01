---
title: "# (Search for Disassembly Pattern)"
description: "The number sign (#) command searches for the specified pattern in the disassembly code."
keywords: ["(Search for Disassembly Pattern) Windows Debugging"]
ms.date: 08/30/2023
topic_type:
- apiref
ms.topic: reference
api_name:
- (Search for Disassembly Pattern)
api_type:
- NA
---

# \# (Search for Disassembly Pattern)

The number sign (**\#**) command searches for the specified pattern in the disassembly code.

```dbgcmd
# [Pattern] [Address [ L Size ]] 
```

## Parameters

*Pattern*

Specifies the pattern to search for in the disassembly code. *Pattern* can contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md). If you want to include spaces in *Pattern*, you must enclose the pattern in quotation marks. The pattern is not case sensitive. If you have previously used the **\#** command and you omit *Pattern*, the command reuses the most recently used pattern.

*Address*

Specifies the address where the search begins. For more information about the syntax, see [Address and Address Range Syntax](address-and-address-range-syntax.md).

*Size*

Specifies the number of instructions to search. If you omit *Size*, the search continues until the first match occurs.

### Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |


### Additional Information

For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](../debugger/debugging-in-assembly-mode.md).

## Remarks

If you previously used the **\#** command and you omit *Address*, the search begins where the previous search ended.

This command works by searching the disassembled text for the specified pattern. You can use this command to find register names, constants, or any other string that appears in the disassembly output. You can repeat the command without the *Address* parameter to find successive occurrences of the pattern.

You can view disassembly instructions by using the [u (Unassemble)](u--unassemble-.md) command or by using the [Disassembly window](../debugger/disassembly-window.md) in WinDbg. The disassembly display contains up to four parts: Address offset, Binary code, Assembly language mnemonic, and Assembly language details. The following example shows a possible display.

```dbgcmd
0040116b    45          inc         ebp            
0040116c    fc          cld                        
0040116d    8945b0      mov         eax,[ebp-0x1c] 
```

The **\#** command can search for text within any single part of the disassembly display. For example, you could use \# eax 0040116b to find the `mov eax,[ebp-0x1c]` instruction at address 0040116d. The following commands also find this instruction.

```dbgcmd
#  [ebp?0x  0040116b 
#  mov  0040116b 
#  8945*  0040116b 
#  116d  0040116b 
```

However, you cannot search for `mov eax*` as a single unit, because mov and eax appear in different parts of the display. Instead, use `mov*eax`.

As an additional example, you could issue the following command to search for the first reference to the strlen function after the entry point main.

```dbgcmd
# strlen main
```

Similarly, you could issue the following two commands to find the first jnz instruction after address 0x779F9FBA and then find the next jnz instruction after that.

```dbgcmd
# jnz 779f9fba# 
```

When you omit *Pattern* or *Address*, their values are based on the previous use of the **\#** command. If you omit either parameter the first time that you issue the **\#** command, no search is performed. However, the values of *Pattern* and *Address* are initialized even in this situation.

If you include *Pattern* or *Address*, its value is set to the entered value. If you omit *Address*, it is initialized to the current value of the program counter. If you omit *Pattern*, it is initialized to an empty pattern.
