---
title: Interacting with the Engine
description: Interacting with the Engine
ms.assetid: 80f5320f-ed34-4839-a16e-b3ff5d8edbfe
keywords: ["Debugger Engine API, use"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Interacting with the Engine


### <span id="commands_and_expressions"></span><span id="COMMANDS_AND_EXPRESSIONS"></span>Commands and Expressions

The debugger engine API provides methods to execute commands and evaluate expressions, like those typed into WinDbg's [Debugger Command Window](the-debugger-command-window.md). To execute a debugger command, use [**Execute**](https://msdn.microsoft.com/library/windows/hardware/ff543208). Or, to execute all of the commands in a file, use [**ExecuteCommandFile**](https://msdn.microsoft.com/library/windows/hardware/ff543215).

The method [**Evaluate**](https://msdn.microsoft.com/library/windows/hardware/ff543046) will evaluate expressions using the C++ or MASM syntax. The syntax used by the debugger engine to evaluate expressions--such as in the **Evaluate** method--is given by [**GetExpressionSyntax**](https://msdn.microsoft.com/library/windows/hardware/ff546701) and can be changed using [**SetExpressionSyntaxByName**](https://msdn.microsoft.com/library/windows/hardware/ff556697) and [**SetExpressionSyntax**](https://msdn.microsoft.com/library/windows/hardware/ff556696). The number of different syntaxes that are recognized by the debugger is returned by [**GetNumberExpressionSyntaxes**](https://msdn.microsoft.com/library/windows/hardware/ff547913), and their names are returned by [**GetExpressionSyntaxNames**](https://msdn.microsoft.com/library/windows/hardware/ff546708).

The type of value that is returned by **Evaluate** is determined by the symbols and constants used in the string that was evaluated. The value is contained in a [**DEBUG\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/ff541719) structure and can be cast to different types using [**CoerceValue**](https://msdn.microsoft.com/library/windows/hardware/ff539158) and [**CoerceValues**](https://msdn.microsoft.com/library/windows/hardware/ff539162).

### <span id="aliases"></span><span id="ALIASES"></span>Aliases

*Aliases* are character strings that are automatically replaced with other character strings when used in debugger commands and expressions. For an overview of aliases, see [Using Aliases](using-aliases.md). The debugger engine has several classes of aliases.

The *fixed-name aliases* are indexed by number and have the names **$u0**, **$u1**, ..., **$u9**. The values of these aliases can be set using the [**SetTextMacro**](https://msdn.microsoft.com/library/windows/hardware/ff556809) method and can be retrieved using [**GetTextMacro**](https://msdn.microsoft.com/library/windows/hardware/ff549270) method.

The *automatic aliases* and *user-named aliases* can have any name. The automatic aliases are defined by the debugger engine and the user-named aliases are defined by the user through debugger commands or the debugger engine API. To define or remove a user-named alias, use the [**SetTextReplacement**](https://msdn.microsoft.com/library/windows/hardware/ff556818) method. The [**GetTextReplacement**](https://msdn.microsoft.com/library/windows/hardware/ff549280) method returns the name and value of an automatic alias or a user-named alias. All the user-named aliases can be removed using the [**RemoveTextReplacements**](https://msdn.microsoft.com/library/windows/hardware/ff554548) method. The [**GetNumberTextReplacements**](https://msdn.microsoft.com/library/windows/hardware/ff547988) method will return the number of user-name and automatic aliases; this can be used with **GetTextReplacement** to iterate over all these aliases. The [**OutputTextReplacements**](https://msdn.microsoft.com/library/windows/hardware/ff553268) method will print a list of all the user-named aliases, including their names and values.

**Note**   if a user-named alias is given the same name as an automatic alias, the user-named alias will hide the automatic alias so that when retrieving the value of the alias by name, the user-named alias will be used.

 

### <span id="engine_options"></span><span id="ENGINE_OPTIONS"></span>Engine Options

The engine has a number of options that control its behavior. These options are listed in [**DEBUG\_ENGOPT\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541475). They are returned by [**GetEngineOptions**](https://msdn.microsoft.com/library/windows/hardware/ff546598) and can be set using [**SetEngineOptions**](https://msdn.microsoft.com/library/windows/hardware/ff556670). Individual options can be set using [**AddEngineOptions**](https://msdn.microsoft.com/library/windows/hardware/ff537884) and unset using [**RemoveEngineOptions**](https://msdn.microsoft.com/library/windows/hardware/ff554491).

### <span id="interrupts"></span><span id="INTERRUPTS"></span>Interrupts

An interrupt is a way to force a break into the debugger or to tell the engine to stop processing the current command, for example, by pressing Ctrl+Break in WinDbg.

To request a break into the debugger, or to interrupt the debugger's current task, use [**SetInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff556722). To check if there has been an interrupt, use [**GetInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff546944).

**Note**   When undertaking a long task from a debugger extension, it is recommended that the extension check **GetInterrupt** regularly and stop processing if an interrupt has been requested.

 

When requesting a break into the debugger, the engine might time out if it takes too long for the target to carry out the break-in. This can occur if the target is in a non-responsive state or if the break-in request is blocked or delayed by resource contention. The length of time the engine will wait is returned by [**GetInterruptTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff546955) and can be set using [**SetInterruptTimeout**](https://msdn.microsoft.com/library/windows/hardware/ff556725).

 

 





