---
title: "Time Travel Debugging Extension !tt Command"
description: "The !tt time travel debugger extension that allows you to navigate forward and backwards in time."
keywords: ["!tt Command", "TTD", "Time Travel", "WinDbg", "Windows Debugging"]
ms.date: 12/16/2024
---

# !tt (time travel)

:::image type="content" source="images/ttd-time-travel-debugging-logo.png" alt-text="Time travel debugging logo featuring a clock.":::

The !tt (time travel) debugger extension that allows you to navigate forward and backwards in time.

## !tt navigation commands

Use the !tt extension to navigate forwards or backwards in time, by traveling to a given position in the trace. 

```dbgcmd
!tt [position]
```

### Parameters

**position**

Provide a time position in any of the following formats to travel to that point in time.
           
- If {position} is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !tt 0                   - Time travel to the beginning of the trace
    - !tt 50                  - Time travel to halfway through the trace
    - !tt 100                 - Time travel to the end of the trace
 
- If {position} is a floating point number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !tt 0.00                 - Time travel to the beginning of the trace
    - !tt 50.1                 - Time travel to just over halfway through the trace
    - !tt 99.9                 - Time travel to almost the end of the trace
 
- If {position} is #:#, where # are a hexadecimal numbers, it travels to that position. If the number after : is omitted, it defaults to zero.
    - !tt 1A0:                - Time travel to position 1A0:0
    - !tt 1A0:0               - Time travel to position 1A0:0
    - !tt 1A0:12F             - Time travel to position 1A0:12F

   > [!NOTE]
   > Traces use a two-part instruction position that references a specific position reference in the trace, for example 12:0. or 15:7. The two elements are hexadecimal numbers defined as described here.
   >
   > xx:yy
   > 
   > xx- the first element is the sequencing number, which corresponds to a sequencing event.
   >
   > yy - the second element is a step count, which corresponds roughly to the instruction count since the sequencing event.

## !tt break commands

### Break on register

`!tt br[-] <register> [<value>]`

This command will navigate to the previous/next position where the specified register changed values (or, if `<value>` is specified, becomes the specified value) on the current thread. 

Examples:

`!tt br rbx 0x12345678` – find next position on current thread that sets rbx to 0x12345678.

`!tt br- ebx` – find previous position on current thread that set rbx to its current value.

```dbgcmd
0:000> !tt br- ebx

Setting position: 2C8:0
(3b24.2d98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 2C8:0
ntdll!LdrInitializeThunk:
00007ff9`999e3dd0 4053            push    rbx
```

- The register watchpoint command supports all supported Windows architectures, such as x64 and ARM64.
- The register watchpoint is limited to general purpose (and XMM) registers.
- The register watchpoint is implemented with an algorithm that is slow compared to normal trace replay speed. The search can be cancelled using Ctrl+C. 

### Break on access

`!tt ba[-] <rwe> <address> <size> [<address> <size> …]`

This command will navigate to the previous/next position where one of the specified memory ranges is accessed in the specified way(s): “R” is for memory read, “W” is for memory write and “E” is for execution. More than one can be specified at same time, i.e. “RW”. This is similar to the [ba (Break on Access)](ba--break-on-access-.md) debugger command. 

Examples:
`!tt ba- rw 0x12345678 0x4000` – find previous position that reads from memory range. (0x12345678 – 0x12345678 + 0x4000).
`!tt ba e 0x7fffe0001234 0x30000` – find next position that executes from specified range. Pretend the address and range represent the range of ntdll.dll. This command would find the next position where ntdll.dll is entered.

- Addresses / sizes must be supplied as numbers. Symbols are not supported.

### Break on module

Use Break on module navigation method move forwards or backwards at the module level.

`!tt bm[-] [<module> ...]`

This command time travels to the previous/next position that executes one of the specified module(s). 

If no module is specified, it will travel to the previous/next execution point outside of currently executing module.

When using this command to move in the trace, searching backwards is considerably slower than searching forwards.

#### Example use cases

Here are two example use cases.

##### Use case 1 - *Move forward or backwards until you are in a different module on the current thread. In this case, TTD moves from the dwmcore to ucrtbase modules going forwards and then travels backwards to ntdll.* 

The trace example starts at an exception in the dwmcore module.

```dbgcmd
Setting position: 1C46AE:0
(a54.c98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 1C46AE:0
dwmcore!wil_atomic_uint32_compare_exchange_relaxed+0xc [inlined in dwmcore!wil_details_FeatureReporting_RecordUsageInCache+0x124]:
00007ffa`441e16a0 f0450fb102      lock cmpxchg dword ptr [r10],r8d ds:00007ffa`444b0450=00000003
```

Execute the !tt bm commmand. As no module is specified, travel to the next execution point outside of currently executing module - ucrtbase.

```dbgcmd
0:001> !tt bm
Replaying - Currently at 1D1BEE:0 (  2.95%)
Setting position: 1C46AF:61
(a54.c98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 1C46AF:61
ucrtbase!_finite:
00007ffa`4ac3c080 48b9ffffffffffffff7f mov rcx,7FFFFFFFFFFFFFFFh
```

Single stepping from that location, TTD correctly found the module boundary.

```dbgcmd
0:001> t-
Time Travel Position: 1C46AF:60
dwmcore!CBaseExpression::IsExpressionValueValid+0x50:
00007ffa`44124b40 48ff15f9db2700  call    qword ptr [dwmcore!_imp__finite (00007ffa`443a2740)] ds:00007ffa`443a2740={ucrtbase!_finite (00007ffa`4ac3c080)}

(a54.c98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 1C46AE:0
dwmcore!wil_atomic_uint32_compare_exchange_relaxed+0xc [inlined in dwmcore!wil_details_FeatureReporting_RecordUsageInCache+0x124]:
00007ffa`441e16a0 f0450fb102      lock cmpxchg dword ptr [r10],r8d ds:00007ffa`444b0450=00000003
```

Search backwards for the next module boundary.

```dbgcmd
0:001> !tt bm-
Setting position: 1C46AD:2B1
(a54.c98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 1C46AD:2B1
ntdll!LdrpDispatchUserCallTarget+0x3b:
00007ffa`4d27f24b 48ffe0          jmp     rax {dwmcore!CKeyframeAnimation::CalculateValueWorker (00007ffa`441264e0)}
```
Then travel forward from the module boundary, to the next module.

```dbgcmd
0:001> t
Time Travel Position: 1C46AD:2B2
dwmcore!CKeyframeAnimation::CalculateValueWorker:
00007ffa`441264e0 48895c2408      mov     qword ptr [rsp+8],rbx ss:0000004e`5151f4d0=0000000000000000
```

##### Use case 2 - *Move forward until a module is entered. In this example, ntdll.*

```dbgcmd
0:001> !tt bm ntdll
Replaying - Currently at 1CBF15:0 (  1.66%)
Setting position: 1C46B0:97
(a54.c98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 1C46B0:97
ntdll!LdrpDispatchUserCallTarget:
00007ffa`4d27f210 4c8b1db1c11000  mov     r11,qword ptr [ntdll!LdrSystemDllInitBlock+0xb8 (00007ffa`4d38b3c8)] ds:00007ffa`4d38b3c8=00007df503990000
```

You can use `!tt bm- <module>` to search backwards.

#### Data Model - NextModuleAccess and PrevModuleAccess

Use the [dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) command and the NextModuleAccess and PrevModuleAccess data model objects, to access the same functionality, that is available in the !tt command. 

Travel forward to the next module access boundary.

```dbgcmd
0:001> dx @$curprocess.TTD.NextModuleAccess()
Replaying - Currently at 1D1BEE:0 (  2.95%)
@$curprocess.TTD.NextModuleAccess() : [UTID 3] Execute [1C46AE:0] -> [1C46AF:61] ucrtbase 0x7ffa4ac3c080
    Position         : 1C46AF:61
    OriginalPosition : 1C46AE:0
    UniqueThreadId   : 0x3
    AccessType       : Execute
    Address          : 0x7ffa4ac3c080
    ModuleName       : ucrtbase
```

Travel backwards to the next previous access boundary.

```dbgcmd
0:001> dx @$curprocess.TTD.PrevModuleAccess()
@$curprocess.TTD.PrevModuleAccess() : [UTID 3] Execute [1C46AE:0] -> [1C46AD:2B1] ntdll 0x7ffa4d27f24b
    Position         : 1C46AD:2B1
    OriginalPosition : 1C46AE:0
    UniqueThreadId   : 0x3
    AccessType       : Execute
    Address          : 0x7ffa4d27f24b
    ModuleName       : ntdll
```

Travel forward to the next *ntdll* module access boundary.


```dbgcmd
0:001> dx @$curprocess.TTD.NextModuleAccess("ntdll")
Replaying - Currently at 1CBF15:0 (  1.66%)
@$curprocess.TTD.NextModuleAccess("ntdll") : [UTID 3] Execute [1C46AE:0] -> [1C46B0:97] ntdll 0x7ffa4d27f210
    Position         : 1C46B0:97
    OriginalPosition : 1C46AE:0
    UniqueThreadId   : 0x3
    AccessType       : Execute
    Address          : 0x7ffa4d27f210
    ModuleName       : ntdll
```

## Use debugger model objects for TTD breakpoints

The break on memory access functionality can be accessed through  the [dx  (Display Debugger Object Model Expression)](dx--display-visualizer-variables-.md) command, the debuggers data model windows, JavaScript and C++. For general information on working with LINQ queries and debugger objects, see [Using LINQ With the debugger objects](../debugger/using-linq-with-the-debugger-objects.md).

### TTD.PrevRegisterWrite

`dx @$curthread.TTD.PrevRegisterWrite("<reg>" [, <value>])`

This method searches for the previous position where the specified register changed values (or, if `<value>` is specified, becomes the specified value) on the current thread. It is analogous to the `!tt br-` command above, except it does not automatically navigate to the position. Instead, it returns information like the following:

```dbgcmd
0:000> dx @$curthread.TTD.PrevRegisterWrite("rbx")

@$curthread.TTD.PrevRegisterWrite("rbx")                 : [UTID 2] rbx [2C8:0] 0x0 -> [2C8:0] 0x0
    Register         : rbx
    Position         : 2C8:0 [Time Travel]
    Value            : 0x0
    OriginalPosition : 2C8:0 [Time Travel]
    OriginalValue    : 0x0
    UniqueThreadId   : 0x2
```
Similarly, you can use @$curthread.TTD.NextRegisterWrite(…) to search for the next register change.

```dbgcmd
0:000> dx @$curthread.TTD.NextRegisterWrite("rbx")

@$curthread.TTD.NextRegisterWrite("rbx")                 : [UTID 2] rbx [2C8:1] 0x0 -> [2C8:2] 0x963127f5a0
    Register         : rbx
    Position         : 2C8:2 [Time Travel]
    Value            : 0x963127f5a0
    OriginalPosition : 2C8:1 [Time Travel]
    OriginalValue    : 0x0
    UniqueThreadId   : 0x2
```

Use the *[Time Travel]* links in the output, to move to that postion in the trace.

```dbgcmd
0:000> dx -s @$create("Debugger.Models.TTD.Position", 712, 0).SeekTo()
(3b24.2d98): Break instruction exception - code 80000003 (first/second chance not available)
Time Travel Position: 2C8:0
```

### TTD.PrevMemoryAccess

`dx @$curprocess.TTD.PrevMemoryAccess("<rwe>", <address>, <size> [, <address>, <size> …])`

This method searches for the previous position where one of the specified memory ranges is accessed in the specified way(s). It is analogous to the !tt ba- command above, except it does not automatically navigate to the position. Instead, it returns information like the following:

```dbgcmd
@$curprocess.TTD.PrevMemoryAccess("w", 0x01a16a939820, 0x10) : [UTID 3] Write 0x1a16a939828 4 bytes [1C46AE:0] -> [1C4575:0]
   Position         : 1C4575:0
   OriginalPosition : 1C46AE:0
   UniqueThreadId   : 0x3
   Address          : 0x1a16a939828
   Size             : 0x4
   AccessType       : Write
```

Similarly, you can use `@$curprocess.TTD.NextMemoryAccess(…)` to search for the next memory access.

0:000> dx @$curprocess.TTD.NextMemoryAccess("r", 0x00007ff9`95420000, 0xFF)

```dbgcmd
@$curprocess.TTD.NextMemoryAccess("r", 0x00007ff9`95420000, 0xFF)                 : [UTID 2] Read 0x7ff995420000 2 bytes [2C8:0] -> [66C:10A2]
    Position         : 66C:10A2 [Time Travel]
    OriginalPosition : 2C8:0 [Time Travel]
    UniqueThreadId   : 0x2
    Address          : 0x7ff995420000
    Size             : 0x2
    AccessType       : Read
```

## !tt DLL

ttdext.dll

## Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)
