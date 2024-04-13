---
title: Risks Entailed When Setting Breakpoints
description: Risks Entailed When Setting Breakpoints
keywords: ["breakpoints, risks"]
ms.date: 06/26/2023
---

# Risks Entailed When Setting Breakpoints

When you are setting a [breakpoints](using-breakpoints.md) by specifying a memory address or a symbol plus an offset, you must not put this breakpoint in the middle of an instruction.

For example, consider the following disassembled code.

```dbgcmd
770000f1 5e               pop     esi
770000f2 5b               pop     ebx
770000f3 c9               leave
770000f4 c21000           ret     0x10
770000f7 837ddc00         cmp     dword ptr [ebp-0x24],0x0
```

The first three instructions are only one byte long. However, the fourth instruction is three bytes long. (It includes bytes 0x770000F4, 0x770000F5, and 0x770000F6.) If you want to put a breakpoint on this instruction by using the **bp**, **bu**, or **ba** command, you must specify the 0x770000F4 address.

If you put a breakpoint in the 0x770000F5 address by using the **ba** command, the processor puts a breakpoint at that location. But this breakpoint would never be triggered, because the processor considers 0x770000F4 to be the actual address of the instruction.

If you put a breakpoint in the 0x770000F5 address by using the **bp** or **bu** commands, the debugger writes a breakpoint at that location. However, this breakpoint might corrupt the target because of how the debugger creates breakpoints:

1. The debugger saves the contents of 0x770000F5 and overwrites this memory with a breakpoint instruction.

2. If you try to display this memory in the debugger, the debugger does not show the breakpoint instruction that it has written. Instead, the debugger shows the memory that "should" be there. That is, the debugger shows the original memory, or any modifications to that memory that you have made since inserting the breakpoint.

3. If you use the **BC** command to remove the breakpoint, the debugger restores the original memory to its proper location.

When you put a breakpoint at 0x770000F5, the debugger saves this byte and a break instruction is written here. However, when the application runs, it reaches the 0x770000F4 address and recognizes this address as the first byte of a multibyte instruction. The processor then tries to combine 0x770000F4, 0x770000F5, and possibly some later bytes into a single instruction. This combination can create a variety of behaviors, none of which are desirable.

Therefore, when you put breakpoints by using a **bp**, **bu**, or **ba** command, make sure that you always put the breakpoints at the proper address. If you are using the WinDbg graphical interface to add breakpoints, you do not have to be concerned about this situation because the correct address is chosen automatically.

## Ambiguous breakpoint resolution

In version 10.0.25310.1001 and later of the debugger engine, ambiguous breakpoint resolution is now supported. Ambiguous breakpoints allow for the debugger to set breakpoints in certain scenarios where a breakpoint expression resolves to multiple locations. For more information, see [Ambiguous breakpoint resolution](ambiguous-breakpoint-resolution.md).

## See also

[Using Breakpoints](using-breakpoints.md)

[Breakpoint Syntax](breakpoint-syntax.md)

[bp, bu, bm (Set Breakpoint)](../debuggercmds/bp--bu--bm--set-breakpoint-.md)

[Ambiguous breakpoint resolution](ambiguous-breakpoint-resolution.md)

[Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md)
