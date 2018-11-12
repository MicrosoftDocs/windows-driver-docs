---
title: Avoiding debugger searches for unneeded symbols
description: Why does symbol loading sometimes take so long? That depends on whether the symbol name is qualified or unqualified.
ms.assetid: 710BAEAF-BC45-416E-8359-69E9DFCA2570
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Avoiding debugger searches for un-needed symbols


**Last updated:**

-   May 27, 2007

You arrive at an interesting breakpoint while debugging your driver, only to have the debugger pause for a very long time while it attempts to load symbols for drivers that you don't own and that don't even matter for the debugging task at hand. What's going on?

By default, symbols are loaded by the debugger as they are needed. (This is called deferred symbol loading or lazy symbol loading.) The debugger looks for symbols whenever it executes a command that calls for the display of symbols. This can happen at a breakpoint if you have set a watch variable that is not valid in the current context, such as a function parameter or local variable that doesn't exist in the current stack frame, because they become invalid when the context changes. It can also happen if you simply mistype a symbol name or execute an invalid debugger command-the debugger starts looking for a matching symbol.

Why does this sometimes take so long? That depends on whether the symbol name is qualified or unqualified. A qualified symbol name is preceded with the name of the module that contains the symbol-for example, myModule!myVar. An unqualified symbol name does not specify a module name-for example, myOtherVar.

In the case of the qualified name, the debugger looks for the symbol in the specified module and, if the module is not already loaded, loads the module (assuming the module exists and contains the symbol). This happens fairly quickly.

In the case of an unqualified name, the debugger doesn't "know" which module contains the symbol, so it must look in all of them. The debugger first checks all loaded modules for the symbol and then, if it cannot match the symbol in any loaded module, the debugger continues its search by loading all unloaded modules, starting with the downstream store and ending with the symbol server, if you're using one. Obviously, this can take a lot of time.

## <span id="How_to_prevent_automatic_loading_for_unqualified_symbols_"></span><span id="how_to_prevent_automatic_loading_for_unqualified_symbols_"></span><span id="HOW_TO_PREVENT_AUTOMATIC_LOADING_FOR_UNQUALIFIED_SYMBOLS_"></span>How to prevent automatic loading for unqualified symbols


The **SYMOPT\_NO\_UNQUALIFIED\_LOADS** option disables or enables the debugger's automatic loading of modules when it searches for an unqualified symbol. When **SYMOPT\_NO\_UNQUALIFIED\_LOADS** is set and the debugger attempts to match an unqualified symbol, it searches only modules that have already been loaded, and stops searching when it cannot match the symbol, instead of loading unloaded modules to continue its search. This option does not affect searching for qualified names.

**SYMOPT\_NO\_UNQUALIFIED\_LOADS** is off by default. To activate this option, use the **-snul** command-line option or, while the debugger is running, use **.symopt+0x100** or **.symopt-0x100** to turn the option on or off, respectively.

To see the effect of **SYMOPT\_NO\_UNQUALIFIED\_LOADS**, try this experiment:

1.  Activate noisy symbol loading (**SYMOPT\_DEBUG**) by using the **-n** command-line option or, if the debugger is already running, use **.symopt+0x80000000** or the **!sym noisy** debugger extension command. **SYMOPT\_DEBUG** instructs the debugger to display information about its search for symbols, such as the name of each module as it is loaded or an error message if the debugger cannot find a file.
2.  Instruct the debugger to evaluate a nonexistent symbol (for example, type **?asdasdasd**). The debugger should report numerous errors while it searches for the nonexistent symbol.
3.  Activate **SYMOPT\_NO\_UNQUALIFIED\_LOADS** by using **.symopt+0x100**.
4.  Repeat step 2. The debugger should search only loaded modules for the nonexistent symbol, and it should finish the task much faster.
5.  To disable **SYMOPT\_DEBUG**, use **.symopt-0x80000000** or the **!sym quiet** debugger extension command.

A number of options are available to control how the debugger loads and uses symbols. For a complete list of symbol options and how to use them, see "Setting Symbol Options" in the online documentation provided with Debugging Tools for Windows. The latest release of the Debugging Tools for Windows package is available as a free download from the web, or you can install the package from the Windows DDK, Platform SDK, or Customer Support Diagnostics CD.

## <span id="What_should_you_do__"></span><span id="what_should_you_do__"></span><span id="WHAT_SHOULD_YOU_DO__"></span>What should you do?


-   To speed up symbol searching, use qualified names in breakpoints and debugger commands whenever possible. If you want to see a symbol from a known module, qualify it with the module name; if you don't know where the symbol is, use an unqualified name. For local variables and function arguments, use **$** as the module name (for example, *$!MyVar*).
-   To diagnose the causes of slow symbol loading, activate noisy symbol loading (**SYMOPT\_DEBUG**) by using the **-n** command-line option or, if the debugger is already running, by using **.symopt+0x80000000** or the **!sym noisy** debugger extension command.
-   To prevent the debugger from searching for symbols in unloaded modules, activate **SYMOPT\_NO\_UNQUALIFIED\_LOADS** by using the **-snul** command-line option or, if the debugger is already running, by using **.symopt+0x100**.
-   To explicitly load the modules you need for your debugging session, use debugger commands such as **.reload** or **ld**.

## <span id="related_topics"></span>Related topics


[WDK and WinDbg downloads](https://go.microsoft.com/fwlink/p/?LinkId=733614)

[Windows Debugging](https://msdn.microsoft.com/library/windows/hardware/ff551063.aspx)

 

 






