---
title: Debugging in Assembly Mode
description: Debugging in Assembly Mode
ms.assetid: 048c43ff-7f9e-4a20-a524-44f66d92eefe
keywords: ["assembly debugging", "assembly mode", "assembly debugging, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging in Assembly Mode


## <span id="ddk_debugging_in_assembly_mode_dbg"></span><span id="DDK_DEBUGGING_IN_ASSEMBLY_MODE_DBG"></span>


If you have C or C++ source files for your application, you can use the debugger much more powerfully if you [debug in source mode](debugging-in-source-mode.md).

However, there are many times you cannot perform source debugging. You might not have the source files for your application. You might be debugging someone else's code. You might not have built your executable files with full .pdb symbols. And even if you can do source debugging on your application, you might have to trace Microsoft Windows routines that your application calls or that are used to load your application.

In these situations, you have to debug in assembly mode. Moreover, assembly mode has many useful features that are not present in source debugging. The debugger automatically displays the contents of memory locations and registers as they are accessed and displays the address of the program counter. This display makes assembly debugging a valuable tool that you can use together with source debugging.

### <span id="disassembly_code"></span><span id="DISASSEMBLY_CODE"></span>Disassembly Code

The debugger primarily analyzes binary executable code. Instead of displaying this code in raw format, the debugger *disassembles* this code. That is, the debugger converts the code from machine language to assembly language.

You can display the resulting code (known as *disassembly code*) in several different ways:

-   The [**u (Unassemble)**](u--unassemble-.md) command disassembles and displays a specified section of machine language.

-   The [**uf (Unassemble Function)**](uf--unassemble-function-.md) command disassembles and displays a function.

-   The [**up (Unassemble from Physical Memory)**](up--unassemble-from-physical-memory-.md) command disassembles and displays a specified section of machine language that has been stored in physical memory.

-   The [**ur (Unassemble Real Mode BIOS)**](ur--unassemble-real-mode-bios-.md) command disassembles and displays a specified 16-bit real-mode code.

-   The [**ux (Unassemble x86 BIOS)**](ux--unassemble-x86-bios-.md) command disassembles and displays the x86-based BIOS code instruction set at a specified address.

-   (WinDbg only) The [disassembly window](view---disassembly.md) disassembles and displays a specified section of machine language. this window is automatically active if you select the **automatically open disassembly** command on the **window** menu. you can also open this window by clicking **disassembly** on the **view** menu, pressing alt+7, or pressing the **disassembly (alt+7)** button (![screen shot of the disassembly button](images/tbdisasm2.png)) on the WinDbg toolbar.

The disassembly display appears in four columns: address offset, binary code, assembly language mnemonic, and assembly language details. The following example shows this display.

```dbgcmd
0040116b    45          inc         ebp            
0040116c    fc          cld                        
0040116d    8945b0      mov         eax,[ebp-0x1c] 
```

To the right of the line that represents the current program counter, the display shows the values of any memory locations or registers that are being accessed. If this line contains a branch instruction, the notation **\[br=1\]** or **\[br=0\]** appears. This notation indicates a branch that is or is not taken, respectively.

You can use the [**.asm (Change Disassembly Options)**](-asm--change-disassembly-options-.md) command to change how the disassembled instructions are displayed.

In WinDbg's Disassembly window, the line that represents the current program counter is highlighted. Lines where breakpoints are set are also highlighted.

You can also use the following commands to manipulate assembly code:

-   The [**\# (Search for Disassembly Pattern)**](---search-for-disassembly-pattern-.md) command searches a region of memory for a specific pattern. This command is equivalent to searching the four columns of the disassembly display.

-   The [**a (Assemble)**](a--assemble-.md) command can take assembly instructions and translate them into binary machine code.

### <span id="assembly_mode_and_source_mode"></span><span id="ASSEMBLY_MODE_AND_SOURCE_MODE"></span>Assembly Mode and Source Mode

The debugger has two different operating modes: *assembly mode* and *source mode*.

When you are single-stepping through an application, the size of a single step is one line of assembly code or one line of source code, depending on the mode.

Several commands create different data displays depending on the mode.

In WinDbg, the [Disassembly window](disassembly-window.md) automatically moves to the foreground when you run or step through an application in assembly mode. In source mode, the [Source window](source-window.md) moves to the foreground.

To set the mode, you can do one of the following:

-   Use the [**l+, l- (Set Source Options)**](l---l---set-source-options-.md) command to control the mode. The **l-t** command activates assembly mode.

-   (WinDbg only) Clear the **Source Mode** command on the **Debug** menu to cause the debugger to enter assembly mode.You can also click the **Source mode off** button (![screen shot of the source mode off button](images/tbasm.png)) on the toolbar.

In WinDbg, when you are in assembly mode, **ASM** appears visible on the status bar.

The shortcut menu in WinDbg's Disassembly window includes the **Highlight instructions from the current source line** command. This command highlights all of the instructions that correspond to the current source line. Frequently, a single source line corresponds to multiple assembly instructions. If code has been optimized, these assembly instructions might not be consecutive. The **Highlight instructions from the current source line** command enables you to find all of the instructions that were assembled from the current source line.

### <span id="assembly_language_source_files"></span><span id="ASSEMBLY_LANGUAGE_SOURCE_FILES"></span>Assembly Language Source Files

If your application was written in assembly language, the disassembly that the debugger produces might not exactly match your original code. In particular, NO-OPs and comments will not be present.

If you want to debug your code by referencing the original .asm files, you must use source mode debugging. You can load the assembly file like a C or C++ source file. For more information about this kind of debugging, see [Debugging in Source Mode](debugging-in-source-mode.md).

 

 





