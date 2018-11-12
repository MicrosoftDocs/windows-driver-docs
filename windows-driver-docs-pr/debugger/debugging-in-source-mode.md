---
title: Debugging in Source Mode
description: Debugging in Source Mode
ms.assetid: b236f53b-2429-4085-b008-6648d1474ec2
keywords: ["source debugging", "source mode", "source debugging, overview", "Build utility (build.exe), avoiding optimization"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging in Source Mode


## <span id="ddk_debugging_in_source_mode_dbg"></span><span id="DDK_DEBUGGING_IN_SOURCE_MODE_DBG"></span>


Debugging an application is easier if you can analyze the source of the code, instead of the disassembled binaries.

WinDbg, CDB, and KD can use source code in debugging, if the source language is C, C++, or assembly.

### <span id="compilation_requirements"></span><span id="COMPILATION_REQUIREMENTS"></span>Compilation Requirements

To use source debugging, you must have your compiler or linker create symbol files (.pdb files) when the binaries are built. These symbol files show the debugger how the binary instructions correspond to the source lines.

Also, the debugger must be able to access the actual source files , because symbol files do not contain the actual source text.

If it is possible, the compiler and linker should not optimize your code. Source debugging and access to local variables are more difficult, and sometimes almost impossible, if the code has been optimized. If you are using the Build utility as your compiler and linker, set the MSC\_OPTIMIZATION macro to **/Od /Oi** to avoid optimization.

### <span id="locating_the_symbol_files_and_source_files"></span><span id="LOCATING_THE_SYMBOL_FILES_AND_SOURCE_FILES"></span>Locating the Symbol Files and Source Files

To debug in source mode, the debugger must be able to find the source files and the symbol files. For more information, see [Source Code](source-code.md).

### <span id="beginning_source_debugging"></span><span id="BEGINNING_SOURCE_DEBUGGING"></span>Beginning Source Debugging

The debugger can display source information whenever it has proper symbols and source files for the thread that is currently being debugged.

If you start a new user-mode application by using the debugger, the initial break occurs when Ntdll.dll loads the application. Because the debugger does not have access to the Ntdll.dll source files, you cannot access source information for your application at this point.

To move the program counter to the beginning of the application, add a breakpoint at the entry point to your binary. In the [Debugger Command window](debugger-command-window.md), type the following command.

```dbgcmd
bp main
g
```

The application is then loaded and stops when the **main** function is entered. (Of course, you can use any entry point, not only **main**.)

If the application throws an exception, it breaks into the debugger. Source information is available at this point. However, if you issue a break by using the [**CTRL+C**](ctrl-c--break-.md), [CTRL+BREAK](debug---break.md), or Debug | Break command, the debugger creates a new thread, so you cannot see your source code.

After you have reached a thread that you have source files for, you can use the Debugger Command window to execute source debugging commands. If you are using WinDbg, the [Source window](source-window.md) appears. If you have already opened a Source window by clicking **Open Source File** on the **File** menu, WinDbg typically create a new window for the source. You can close the previous window without affecting the debugging process.

### <span id="source_debugging_in_the_windbg_gui"></span><span id="SOURCE_DEBUGGING_IN_THE_WINDBG_GUI"></span>Source Debugging in the WinDbg GUI

If you are using WinDbg, a Source window appears as soon as the program counter is in code that the debugger has source information for.

WinDbg displays one Source window for each source file that you or WinDbg opened. For more information about the text properties of this window, see [Source Windows](source-window.md).

You can then step through your application or execute to a breakpoint or to the cursor. For more information about stepping and tracing commands, see [Controlling the Target](controlling-the-target.md).

If you are in source mode, the appropriate Source window moves to the foreground as you step through your application. Because there are also Microsoft Windows routines that are called during the application's execution, the debugger might move a [Disassembly window](disassembly-window.md) to the foreground when this kind of call occurs (because the debugger does not have access to the source for these functions). When the program counter returns to known source files, the appropriate Source window becomes active.

As you move through the application, WinDbg highlights your location in the Source window and the Disassembly window. Lines at which breakpoints are set are also highlighted. The source code is colored according to the parsing of the language. If the Source window has been selected, you can hover over a symbol with the mouse to evaluate it. For more information about these features and how to control them, see [Source Windows](source-window.md).

To activate source mode in WinDbg, use the [**l+t**](l---l---set-source-options-.md) command, click **source mode** on the **debug** menu, or click the **source mode on** button (![screen shot of the source mode on button](images/tbsrc.png)) on the toolbar.

When source mode is active, the **ASM** indicator appears unavailable on the status bar.

You can view or alter the values of any local variables as you step through a function in source mode. For more information, see [Reading and Writing Memory](reading-and-writing-memory.md).

### <span id="source_debugging_in_the_debugger_command_window"></span><span id="SOURCE_DEBUGGING_IN_THE_DEBUGGER_COMMAND_WINDOW"></span>Source Debugging in the Debugger Command Window

If you are using CDB, you do not have a separate Source window. However, you can still view your progress as you step through the source.

Before you can do source debugging in CDB, you have to load source line symbols by issuing the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command or by starting the debugger with the [**-lines command-line option**](cdb-command-line-options.md).

If you execute an [**l+t**](l---l---set-source-options-.md) command, all program stepping is performed one source line at a time. Use **l-t** to step one assembly instruction at a time. If you are using WinDbg, this command has the same effect as selecting or clearing **Source Mode** on the **Debug** menu or using the toolbar buttons.

The [**l+s**](l---l---set-source-options-.md) command displays the current source line and line number at the prompt. If you want to see only the line number, use **l+l** instead.

If you use [**l+o**](l---l---set-source-options-.md) and **l+s**, only the source line is displayed while you step through the program. The program counter, disassembly code, and register information are hidden. This kind of display enables you to quickly step through the code and view nothing but the source.

You can use the [**lsp (Set Number of Source Lines)**](lsp--set-number-of-source-lines-.md) command to specify exactly how many source lines are displayed when you step through or execute the application.

The following sequence of commands is an effective way to step through a source file.

```text
.lines        enable source line information
bp main       set initial breakpoint
l+t           stepping will be done by source line
l+s           source lines will be displayed at prompt
g             run program until "main" is entered
pr            execute one source line, and toggle register display off
p             execute one source line 
```

Because [**ENTER**](enter--repeat-last-command-.md) repeats the last command, you can now step through the application by using the ENTER key. Each step causes the source line, memory offset, and assembly code to appear.

For more information about how to interpret the disassembly display, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

When the assembly code is displayed, any memory location that is being accessed is displayed at the right end of the line. You can use the [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) and [**e\* (Enter Values)**](e--ea--eb--ed--ed--ef--ep--eq--eu--ew--eza--ezu--enter-values-.md) commands to view or change the values in these locations.

If you have to view each assembly instruction to determine offsets or memory information, use [**l-t**](l---l---set-source-options-.md) to step by assembly instructions instead of source lines. The source line information can still be displayed. Each source line corresponds to one or more assembly instructions.

All of these commands are available in WinDbg and in CDB. You can use the commands to view source line information from WinDbg's [Debugger Command window](debugger-command-window.md) instead of from the Source window.

### <span id="source_lines_and_offsets"></span><span id="SOURCE_LINES_AND_OFFSETS"></span>Source Lines and Offsets

You can also perform source debugging by using the expression evaluator to determine the offset that corresponds to a specific source line.

The following command displays a memory offset.

```dbgcmd
? `[[module!]filename][:linenumber]` 
```

If you omit *filename*, the debugger searches for the source file that corresponds to the current program counter.

The debugger reads *linenumber* as a decimal number unless you add **0x** before it, regardless of the current default radix. If you omit *linenumber*, the expression evaluates to the initial address of the executable file that corresponds to the source file.

This syntax is understood in CDB only if the **.lines** command or the **-lines** command-line option has loaded source line symbols.

This technique is very versatile, because you can use it regardless of where the program counter is pointing. For example, this technique enables you to set breakpoints in advance, by using commands such as the following.

```dbgcmd
bp `source.c:31` 
```

For more information, see [Source Line Syntax](source-line-syntax.md) and [Using Breakpoints](using-breakpoints.md).

### <span id="stepping_and_tracing_in_source_mode"></span><span id="STEPPING_AND_TRACING_IN_SOURCE_MODE"></span>Stepping and Tracing in Source Mode

When you are debugging in source mode, there can be multiple function calls on a single source line. You cannot use the **p** and **t** commands to separate these function calls.

For example, in the following command, the **t** command steps into both **GetTickCount** and **printf**, while the **p** command steps over both function calls.

```cpp
printf( "%x\n", GetTickCount() );
```

If you want to step over certain calls while tracing into other calls, use [**.step\_filter (Set Step Filter)**](-step-filter--set-step-filter-.md) to indicate which calls to step over.

You can use **\_step\_filter** to filter out framework functions (for example, Microsoft Foundation Classes (MFC) or Active Template Library (ATL) calls).

 

 





