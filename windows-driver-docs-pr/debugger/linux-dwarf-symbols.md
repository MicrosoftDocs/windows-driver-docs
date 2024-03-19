---
title: Linux symbols and sources
description: Linux symbols and sources
keywords: ["symbols, linux, process"]
ms.date: 03/18/2024
---

# Linux symbols and sources

This article describes how WinDbg supports standard Linux symbols and sources. Support for debugging on Linux requires WinDbg version 1.2402.24001.0 or above.

## DebugInfoD symbol servers

The Window debugger uses the DebugInfoD standard for automatic download of build artifacts for Linux. Comparably, DebugInfoD is a combination of Microsoft's symbol server and source server technologies. It permits automatically downloading of three artifact types (executables (ELF), debug info (DWARF), and source (code) based on the build-id. Various distributions of Linux now host their own DebugInfoD servers which provide some of the artifact types. The various DebugInfoD servers are listed at ELFUTILS https://debuginfod.elfutils.org.

General information on DebugInfoD is available here:

- [DebugInfoD servers](https://sourceware.org/elfutils/Debuginfod.html)

- [Ubuntu Debuginfod](https://ubuntu.com/server/docs/debuginfod)

The `DebugInfoD*` tag can point to one or more DebugInfoD servers with each server URL formatted as `https://domain.com` and separated by `*`. The servers will be searched in the same order as listed in the source path and the files will be retrieved from the first matching URL.

For example you can set the symbol path like this.

`.sympath+ DebugInfoD*https://debuginfod.elfutils.org`

Use the `!sym noisy` command to display information about symbol loading. For more information, see [!sym](../debuggercmds/-sym.md).

The source path command ([.srcpath, .lsrcpath (Set Source Path)](../debuggercmds/-srcpath---lsrcpath--set-source-path-.md)) supports file retrieval from DebugInfoD servers through the `DebugInfoD*` tag, which allows for the retrieval of source code artifacts. For example, you can set the source path, like this.

`.srcpath+ DebugInfoD*https://debuginfod.elfutils.org`

For more information, see [Source Code Extended Access](source-code-extended-access.md).

## DWARF symbols

DWARF is a widely used, standardized debugging data format. DWARF was originally designed along with Executable and Linkable Format (ELF), although it is independent of object file formats. For more information, see [https://en.wikipedia.org/wiki/DWARF](https://en.wikipedia.org/wiki/DWARF) and for the version 5 standard, see [DWARF Version 5](https://dwarfstd.org/dwarf5std.html).

Use the object dump command to determine the DWARF symbol version. In this example, version 5.

```linux
bob@BOB:/mnt/c/Users/BOB$ objdump -g DisplayGreeting | grep -A 2 'Compilation Unit @'
  Compilation Unit @ offset 0x0:
   Length:        0x285c (32-bit)
   Version:       5
```

### WinDbg DWARF Support

WinDbg supports the following uses of DWARF and ELF.

- *Linux User Mode* - Opening Linux ELF Core Dumps (`-z <core dump>`) and doing post-mortem debugging and analysis with full private DWARF symbols.

- *Linux Kernel Mode* - Opening Linux Kernel (ELF VMCORE) Dumps and doing post-mortem debugging and analysis with full private DWARF symbols.

- *Linux Kernel Mode* - Opening Linux Kernel compressed KDUMPs and doing post-mortem debugging and analysis with full private DWARF symbols (WinDbg only supports ZLIB compressed KDUMP files. LZO and Snappy compressed KDUMPs are unsupported.)

- Opening ELF Images (`-z <ELF image>`) and examining contents, disassembly, etc.

- *Other Scenarios* - Understanding ELF images and DWARF symbols in mixed PE/ELF environments (e.g.: debugging Open Enclave components loaded on Windows. For more information, see [Open Enclave debugging](open-enclave-debugging.md).)

### WinDbg GDBServer Linux support

The GNU Debugger, GDBServer is used on Linux to support the WinDbg connection. For more information about GDBServer, see [https://en.wikipedia.org/wiki/Gdbserver](https://en.wikipedia.org/wiki/Gdbserver). One place to view the documentation for remote gdb debugging is here - https://sourceware.org/gdb/current/onlinedocs/gdb#Remote-Debugging

For more information, on using GDBServer with WinDbg and a code walkthrough, see [Linux live remote process debugging](linux-live-remote-process-debugging.md). The examples here use Ubuntu running under the Windows Subsystem for Linux (WSL), but other Linux implementations can also be used.

### DWARF Implementation

DWARF symbols are supported embedded in the original image (a debug binary) or stripped into a separate ELF image (a debug package).

In order for the Linux DWARF stack walk to succeed, the original binary image for any module loaded into the Linux process must be able to be found.

DWARF symbols/ELF images (stripped or not) can be found via the debugger's sympath or the symbol server (indexed as per .NET Core via the GNU Build ID hash).

DWARF symbols can be found via a Linux style debug package install. Such is given by a directory named `.build-id` in the symbol path. Under this are directories named according to the first byte of the GNU Build ID hash. Under each such directory is a file named `<remaining 18 bytes of GNU Build ID hash>`.debug.

When the debugger opens DWARF symbols, it performs an initial indexing step as the format itself does not include necessary lookup tables. For large sets of DWARF symbols (e.g.: private DWARF information for the Linux kernel), this may take 10 - 30 seconds.

## !addsourcemap for automatic source retrieval from known repo / commit

If you are debugging components built from a known repo and commit, there is an extension, `!addsourcemap`, debugger command allows you to tell the debugger that for a given module and path, you would like to automatically retrieve sources from a known URL. The usage of the extension is:

`!addsourcemap <module> <local spec> <remote spec>`

Where:

`<module>` is the name of the module of interest.

`<local spec>` is the path of sources within that module which will be looked up via a URL. This path should end in a wildcard.

`<remote spec>` is the URL at which files that match `<local spec>` will be looked up. This path should end in a wildcard which will be replaced with how the wildcard in `<local spec>` matches a particular source path.

To set the sourcemap, confirm that the module is present using [lm (List Loaded Modules)](../debuggercmds/lm--list-loaded-modules-.md). Then determine the remote location of the source.

This example sets the vmlinux module to a specific build available on GitHub.

```dbgcmd
0:000> !addsourcemap vmlinux /build/linux/* https://raw.githubusercontent.com/torvalds/linux/6e61dde82e8bfe65e8ebbe43da45e615bc529236/
Source map /build/linux/* -> https://raw.githubusercontent.com/torvalds/linux/6e61dde82e8bfe65e8ebbe43da45e615bc529236/ successfully added
```

After the sourcemap command has been issued, a number of things will trigger a source load, for example switching frames back and forth or reloading, using the .reload command. After that, and an automatic source pull from GitHub will happen.

### !sourcemaps

Use the `!sourcemaps` command to list existing source maps.

```dbgcmd
0:000> !sourcemaps
Source maps for vmlinux.6:
    /build/linux/* -> https://raw.githubusercontent.com/torvalds/linux/6e61dde82e8bfe65e8ebbe43da45e615bc529236/
```

### !removesourcemaps

Use the `!removesourcemaps` command to remove an existing source map.

```dbgcmd
0:000> !removesourcemaps vmlinux /build/linux/* https://raw.githubusercontent.com/torvalds/linux/6e61dde82e8bfe65e8ebbe43da45e615bc529236/
1 source maps successfully removed
```

## Troubleshooting DWARF symbols

If you are debugging Linux/Android dumps (or other targets that use DWARF symbols), you may want to look at the raw contents of symbols to understand why local variables, type definitions, or function definitions are incorrect. To do this, the debugger has some built-in extension commands to dump the raw contents of DWARF symbols. In addition use Linux utilities such as readelf and dumpdwarf to display symbol internals information.

### readelf command

Use the readelf command at the Linux command prompt to display the debug build ID that was created for the sample DisplayGreeting program that was created in [Linux live remote process debugging](linux-live-remote-process-debugging.md). In this example, a build ID of *aba822dd158b997b09903d4165f3dbfd37f5e5c1* is returned.

```linux
Bob@BOB6:/mnt/c/Users/Bob$ readelf -n DisplayGreeting

Displaying notes found in: .note.gnu.property
  Owner                Data size        Description
  GNU                  0x00000020       NT_GNU_PROPERTY_TYPE_0
      Properties: x86 feature: IBT, SHSTK
        x86 ISA needed: x86-64-baseline

Displaying notes found in: .note.gnu.build-id
  Owner                Data size        Description
  GNU                  0x00000014       NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: aba822dd158b997b09903d4165f3dbfd37f5e5c1

Displaying notes found in: .note.ABI-tag
  Owner                Data size        Description
  GNU                  0x00000010       NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0
```

Readelf can be used with grep to return the symbol version.

```linux
 readelf --debug-dump=info DisplayGreeting | grep -A 2 'Compilation Unit @'
  Compilation Unit @ offset 0x0:
   Length:        0x285c (32-bit)
   Version:       5
```

### dwarfdump

The dwarfdump linux command prints or checks DWARF sections as requested by specific options. Use dwarfdump -h to view the many options.

```linux
bob@BOB6:/mnt/c/Users/BOB$ dwarfdump -h
```

For more information about using dwarfdump on Ubuntu, see [dwarfdump ](https://manpages.ubuntu.com/manpages/mantic/en/man1/dwarfdump.1.html).

## !diesym

This debugger command will display the DIE (or DIE subtree) for whatever symbol is at the given expression (can be an address, a function name, etc.) with an optionally specified recursion level. It locates the DIE for the symbol (typically function but could be data, etc...) contained at a given address and performs a diagnostic dump of the DIE similar to running dwarfdump or llvm-dwarfdump on the symbols and finding the DIE.

`!diesym [options] <expression>`

`-r#` : dump N levels recursively.  Normally, this is one and only the DIE itself is dumped.

`<expression>` - The address to locate the DIE is given by an expression.  It may be a flat hex address (`0x<blah>`) or it may be an otherwise unique function name.  

It needs to be evaluatable by the data model's standard evaluation. Use the dx command to validate that the model expression. For more information about using the dx command, see [dx (Display Debugger Object Model Expression)](../debuggercmds/dx--display-visualizer-variables-.md).

```dbgcmd
0:000> dx DisplayGreeting!GetCppConGreeting
DisplayGreeting!GetCppConGreeting                 : DisplayGreeting!GetCppConGreeting+0x0 [Type: GetCppConGreeting]
```

Display DIE symbol information for the sample DisplayGreeting program, GetCppConGreeting function.

```dbgcmd
0:000> !diesym DisplayGreeting!GetCppConGreeting
0x2816: DW_TAG_subprogram [^^^]
    DW_AT_external          (true)
    DW_AT_name              'GetCppConGreeting'
    DW_AT_decl_file         1 ('/mnt/c/Users/BOB/DisplayGreeting.cpp')
    DW_AT_decl_line         0x7
    DW_AT_decl_column       0x6
    DW_AT_linkage_name      '_Z17GetCppConGreetingPwm'
    DW_AT_low_pc            0x11E9
    DW_AT_high_pc           +0x3c (== 0x1225)
    DW_AT_frame_base        DW_OP_call_frame_cfa 
    DW_AT_call_all_tail_calls   (true)
```

Use the -r2 option to display an additional level of DIE symbol information.

```dbgcmd
0:000> !diesym -r2 DisplayGreeting!GetCppConGreeting
0x2816: DW_TAG_subprogram [^^^]
    DW_AT_external          (true)
    DW_AT_name              'GetCppConGreeting'
    DW_AT_decl_file         1 ('/mnt/c/Users/BOB/DisplayGreeting.cpp')
    DW_AT_decl_line         0x7
    DW_AT_decl_column       0x6
    DW_AT_linkage_name      '_Z17GetCppConGreetingPwm'
    DW_AT_low_pc            0x11E9
    DW_AT_high_pc           +0x3c (== 0x1225)
    DW_AT_frame_base        DW_OP_call_frame_cfa 
    DW_AT_call_all_tail_calls   (true)

    0x2834: DW_TAG_formal_parameter [^^^]
        DW_AT_name              'buffer'
        DW_AT_decl_file         1 ('/mnt/c/Users/BOB/DisplayGreeting.cpp')
        DW_AT_decl_line         0x7
        DW_AT_decl_column       0x21
        DW_AT_type              (CU + 0x12f7 == 0x12f7)
        DW_AT_location          DW_OP_fbreg(-40) 
```

## !die

`!die` will display the DIE (or DIE subtree) for whatever DIE is at the given offset expression within the DWARF debug section with an optionally specified recursion level.

`!die [-r#] [-t] -m <module base expression> <offset expression>`

`-r#` : dump N levels recursively.

`-t`  : If the DIE is within a type unit in .debug_types instead of a compilation unit within .debug_info, you must specify the -t switch.

Supply an `-m <module base expression>` that gives the base address of whatever module you are querying about.

The `<offset expression>` is the size of the DIE offset.

At the Linux prompt use dwarfdump with the -r to print the *.debug_aranges* section of the DWARF file to locate the DIE offset.

```linux
bob@BOB6:/mnt/c/Users/BOB$ dwarfdump -r DisplayGreeting

.debug_aranges

COMPILE_UNIT<header overall offset = 0x00000000>:
< 0><0x0000000c>  DW_TAG_compile_unit
                    DW_AT_producer              GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection
                    DW_AT_language              DW_LANG_C_plus_plus_14
                    DW_AT_name                  DisplayGreeting.cpp
                    DW_AT_comp_dir              /mnt/c/Users/BOB
                    DW_AT_ranges                0x0000000c

      Offset of rnglists entries: 0x0000000c
      [ 0] start,end             0x000011e9 0x0000134a
      [ 1] start,end             0x0000134a 0x00001368
      [ 2] start,end             0x00001368 0x0000137b
      [ 3] start,end             0x0000137b 0x0000138d
      [ 4] end of list
                    DW_AT_low_pc                0x00000000
                    DW_AT_stmt_list             0x00000000


arange starts at 0x000011e9, length of 0x00000161, cu_die_offset = 0x0000000c
arange starts at 0x0000134a, length of 0x0000001e, cu_die_offset = 0x0000000c
arange starts at 0x00001368, length of 0x00000013, cu_die_offset = 0x0000000c
arange starts at 0x0000137b, length of 0x00000012, cu_die_offset = 0x0000000c
```

Note the  DW_AT_ranges value of `0x0000000c`. In the debugger use that offset value and the module name of DisplayGreeting to display DIE symbol information.

```dbgcmd
0:000> !die -m DisplayGreeting 0x0000000c
0xc: DW_TAG_compile_unit [^^^]
    DW_AT_producer          'GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection'
    DW_AT_language          0x21
    DW_AT_name              
    DW_AT_comp_dir          
    DW_AT_ranges            
        [0x11e9 - 0x134a)
        [0x134a - 0x1368)
        [0x1368 - 0x137b)
        [0x137b - 0x138d)
    DW_AT_low_pc            0x0
    DW_AT_stmt_list        
```

## !dieancestry

The `!dieancestry` command behaves similar to `!die` except that it walks up the DIE tree towards the containing compilation or type unit, instead of down the tree.

`!dieancestry [-r#] [-t] -m <module base expression> <offset expression>`

`-r#` : dump N levels recursively.

Supply an `-m <module base expression>` that gives the base address of whatever module you are querying about.

The `<offset expression>` is the size of the DIE offset.

Example:

```dbgcmd
0:000> !dieancestry -m DisplayGreeting 0x0000000c
0xc: DW_TAG_compile_unit [^^^]
    DW_AT_producer          'GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection'
    DW_AT_language          0x21
    DW_AT_name              
    DW_AT_comp_dir          
    DW_AT_ranges            
        [0x11e9 - 0x134a)
        [0x134a - 0x1368)
        [0x1368 - 0x137b)
        [0x137b - 0x138d)
    DW_AT_low_pc            0x0
    DW_AT_stmt_list       
```

Note that links, for example to parents or siblings, are clickable to allow for further traversal of the DWARF symbol tree.

```dbgcmd
0:000> !die -r2 -m 0x555555554000 0xc
0xc: DW_TAG_compile_unit [^^^]
    DW_AT_producer          'GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection'
    DW_AT_language          0x21
    DW_AT_name              
    DW_AT_comp_dir          
    DW_AT_ranges            
        [0x11e9 - 0x134a)
        [0x134a - 0x1368)
        [0x1368 - 0x137b)
        [0x137b - 0x138d)
    DW_AT_low_pc            0x0
    DW_AT_stmt_list         

    0x2a: DW_TAG_namespace [^^^]
        DW_AT_name              'std'
        DW_AT_decl_file         9 ('/usr/include/c++/11/bits/exception_ptr.h')
        DW_AT_decl_line         0x116
        DW_AT_decl_column       0xb
        DW_AT_sibling           (CU + 0xf01 == 0xf01)

    0xf01: DW_TAG_base_type [^^^]
        DW_AT_byte_size         0x1
        DW_AT_encoding          DW_ATE_boolean (2)
        DW_AT_name              'bool'

    0xf08: DW_TAG_base_type [^^^]
        DW_AT_byte_size         0x8
        DW_AT_encoding          DW_ATE_unsigned (7)
        DW_AT_name              'long unsigned int'

...
   
```

Not all output is shown.

## !dwunwind

`!dwunwind` is somewhat similar to [.fnent (Display function data)](../debuggercmds/-fnent--display-function-data-.md) for PE images. It displays the DWARF unwind rules for an address given by the expression. It is also similar to the readelf --unwind command, that displays unwind information, when it is available.

`!dwunwind <expression>`

This example displays the unwind rules for the GetCppConGreeting function in the DisplayGreeting program.

```dbgcmd
0:000> !dwunwind DisplayGreeting!GetCppConGreeting
DW_FRAME_SAME_VAL: 0('rax'), 1('rdx'), 2('rcx'), 3('rbx'), 4('rsi'), 5('rdi'), 6('rbp'), 7('rsp'), 8('r8'), 9('r9'), 10('r10'), 11('r11'), 12('r12'), 13('r13'), 14('r14'), 15('r15')
0('CFA'): DW_EXPR_OFFSET 7('rsp') + 8
16('<Return Address>'): DW_EXPR_OFFSET 12290('CFA') + -8
```

This displays the unwind stack for the instruction pointer register.

```dbgcmd
0:000> !dwunwind @rip
DW_FRAME_SAME_VAL: 0('rax'), 1('rdx'), 2('rcx'), 4('rsi'), 5('rdi'), 7('rsp'), 8('r8'), 9('r9'), 10('r10'), 11('r11'), 14('r14'), 15('r15')
0('CFA'): DW_EXPR_OFFSET 7('rsp') + 208
3('rbx'): DW_EXPR_OFFSET 12290('CFA') + -40
6('rbp'): DW_EXPR_OFFSET 12290('CFA') + -32
12('r12'): DW_EXPR_OFFSET 12290('CFA') + -24
13('r13'): DW_EXPR_OFFSET 12290('CFA') + -16
16('<Return Address>'): DW_EXPR_OFFSET 12290('CFA') + -8
```

Here is a program counter example.

```dbgcmd
   0:000> !dwunwind @pc
   DW_FRAME_SAME_VAL: 0('x0'), 1('x1'), 2('x2'), 3('x3'), 4('x4'), 5('x5'), 6('x6'), 7('x7'), 8('x8'), 9('x9'), 10('x10'), 11('x11'), 12('x12'), 13('x13'), 14('x14'), 15('x15'), 16('x16'), 17('x17'), 18('x18'), 31('sp'), 32('pc')
   0('CFA'): DW_EXPR_OFFSET 31('sp') + 208
   19('x19'): DW_EXPR_OFFSET 1436('CFA') + -192
   20('x20'): DW_EXPR_OFFSET 1436('CFA') + -184
   21('x21'): DW_EXPR_OFFSET 1436('CFA') + -176
   22('x22'): DW_EXPR_OFFSET 1436('CFA') + -168
   23('x23'): DW_EXPR_OFFSET 1436('CFA') + -160
   24('x24'): DW_EXPR_OFFSET 1436('CFA') + -152
   25('x25'): DW_EXPR_OFFSET 1436('CFA') + -144
   26('x26'): DW_EXPR_OFFSET 1436('CFA') + -136
   27('x27'): DW_EXPR_OFFSET 1436('CFA') + -128
   28('x28'): DW_EXPR_OFFSET 1436('CFA') + -120
   29('fp'): DW_EXPR_OFFSET 1436('CFA') + -208
   30('lr'): DW_EXPR_OFFSET 1436('CFA') + -200
```

## !dietree

Dumps the DIE tree for a given module at a given recursion level similar to running dwarfdump or llvm-dwarfdump on the symbols and finding the DIE.

`!dietree [OPTIONS] -m <module base> <offset expression>`

`-r#` : Specify recursion level

`-t` : Dump .debug_types and not .debug_info

The module base for the module containing the DIE must be given by the `-m <expression>` option.

The `<offset expression>` is the size of the DIE offset.

Example:

```dbgcmd
0:000> !dietree -m DisplayGreeting 0x0000000c
0xc: DW_TAG_compile_unit [^^^]
    DW_AT_producer          'GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection'
    DW_AT_language          0x21
    DW_AT_name              
    DW_AT_comp_dir          
    DW_AT_ranges            
        [0x11e9 - 0x134a)
        [0x134a - 0x1368)
        [0x1368 - 0x137b)
        [0x137b - 0x138d)
    DW_AT_low_pc            0x0
    DW_AT_stmt_list  
```

Use the -r2 option to display additional values in the dietree.

```dbgcmd
0:000> !dietree -r2 -m DisplayGreeting 0x0000000c
0xc: DW_TAG_compile_unit [^^^]
    DW_AT_producer          'GNU C++17 11.4.0 -mtune=generic -march=x86-64 -g -fasynchronous-unwind-tables -fstack-protector-strong -fstack-clash-protection -fcf-protection'
    DW_AT_language          0x21
    DW_AT_name              
    DW_AT_comp_dir          
    DW_AT_ranges            
        [0x11e9 - 0x134a)
        [0x134a - 0x1368)
        [0x1368 - 0x137b)
        [0x137b - 0x138d)
    DW_AT_low_pc            0x0
    DW_AT_stmt_list         

    0x2a: DW_TAG_namespace [^^^]
        DW_AT_name              'std'
        DW_AT_decl_file         9 ('/usr/include/c++/11/bits/exception_ptr.h')
        DW_AT_decl_line         0x116
        DW_AT_decl_column       0xb
        DW_AT_sibling           (CU + 0xf01 == 0xf01)

    0xf01: DW_TAG_base_type [^^^]
        DW_AT_byte_size         0x1
        DW_AT_encoding          DW_ATE_boolean (2)
        DW_AT_name              'bool'

    0xf08: DW_TAG_base_type [^^^]
        DW_AT_byte_size         0x8
        DW_AT_encoding          DW_ATE_unsigned (7)
        DW_AT_name              'long unsigned int'

    0xf0f: DW_TAG_base_type [^^^]
        DW_AT_byte_size         0x1
        DW_AT_encoding          DW_ATE_unsigned_char (8)
        DW_AT_name              'unsigned char'

...

```

Not all output is shown. Note that links, for example to siblings, are clickable to allow for further traversal of the DWARF symbol tree.

## !dielocal

Locates the DIE for the local variable named "name" and performs a diagnostic dump of the DIE similar to running dwarfdump or llvm-dwarfdump on the symbols and finding the DIE.

`!dielocal [options] <name>`

`-r#` : dump N levels recursively.  Normally, this is one and only the DIE itself is dumped.

`<name>` : local variable named "name".

Example:

```dbgcmd
0:000> !dielocal greeting
0x2806: DW_TAG_variable [^^^]
    DW_AT_name              'greeting'
    DW_AT_decl_file         1 ('/mnt/c/Users/BOB/DisplayGreeting.cpp')
    DW_AT_decl_line         0xf
    DW_AT_decl_column       0x1d
    DW_AT_type              (CU + 0xb18 == 0xb18)
    DW_AT_location          DW_OP_fbreg(-240) 
```

## See also

[Source Code Extended Access](source-code-extended-access.md)

[ELFUTILS debuginfod](https://sourceware.org/elfutils/Debuginfod.html)

[DWARF Version 5](https://dwarfstd.org/dwarf5std.html)

[Using Symbols](using-symbols.md)

[!sym](../debuggercmds/-sym.md)
