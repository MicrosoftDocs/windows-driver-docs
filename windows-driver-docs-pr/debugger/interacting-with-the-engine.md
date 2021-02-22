---
title: Interacting with the Engine
description: Interacting with the Engine
keywords: ["Debugger Engine API, use"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Interacting with the Engine


### <span id="commands_and_expressions"></span><span id="COMMANDS_AND_EXPRESSIONS"></span>Commands and Expressions

The debugger engine API provides methods to execute commands and evaluate expressions, like those typed into WinDbg's [Debugger Command Window](the-debugger-command-window.md). To execute a debugger command, use [**Execute**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-execute). Or, to execute all of the commands in a file, use [**ExecuteCommandFile**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-executecommandfile).

The method [**Evaluate**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-evaluate) will evaluate expressions using the C++ or MASM syntax. The syntax used by the debugger engine to evaluate expressions--such as in the **Evaluate** method--is given by [**GetExpressionSyntax**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getexpressionsyntax) and can be changed using [**SetExpressionSyntaxByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setexpressionsyntaxbyname) and [**SetExpressionSyntax**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setexpressionsyntax). The number of different syntaxes that are recognized by the debugger is returned by [**GetNumberExpressionSyntaxes**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumberexpressionsyntaxes), and their names are returned by [**GetExpressionSyntaxNames**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getexpressionsyntaxnames).

The type of value that is returned by **Evaluate** is determined by the symbols and constants used in the string that was evaluated. The value is contained in a [**DEBUG\_VALUE**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_value) structure and can be cast to different types using [**CoerceValue**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-coercevalue) and [**CoerceValues**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-coercevalues).

### <span id="aliases"></span><span id="ALIASES"></span>Aliases

*Aliases* are character strings that are automatically replaced with other character strings when used in debugger commands and expressions. For an overview of aliases, see [Using Aliases](using-aliases.md). The debugger engine has several classes of aliases.

The *fixed-name aliases* are indexed by number and have the names **$u0**, **$u1**, ..., **$u9**. The values of these aliases can be set using the [**SetTextMacro**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-settextmacro) method and can be retrieved using [**GetTextMacro**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-gettextmacro) method.

The *automatic aliases* and *user-named aliases* can have any name. The automatic aliases are defined by the debugger engine and the user-named aliases are defined by the user through debugger commands or the debugger engine API. To define or remove a user-named alias, use the [**SetTextReplacement**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-settextreplacement) method. The [**GetTextReplacement**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-gettextreplacement) method returns the name and value of an automatic alias or a user-named alias. All the user-named aliases can be removed using the [**RemoveTextReplacements**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-removetextreplacements) method. The [**GetNumberTextReplacements**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getnumbertextreplacements) method will return the number of user-name and automatic aliases; this can be used with **GetTextReplacement** to iterate over all these aliases. The [**OutputTextReplacements**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-outputtextreplacements) method will print a list of all the user-named aliases, including their names and values.

**Note**   if a user-named alias is given the same name as an automatic alias, the user-named alias will hide the automatic alias so that when retrieving the value of the alias by name, the user-named alias will be used.

 

### <span id="engine_options"></span><span id="ENGINE_OPTIONS"></span>Engine Options

The engine has a number of options that control its behavior. These options are listed in [**DEBUG\_ENGOPT\_XXX**](/previous-versions/ff541475(v=vs.85)). They are returned by [**GetEngineOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getengineoptions) and can be set using [**SetEngineOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setengineoptions). Individual options can be set using [**AddEngineOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-addengineoptions) and unset using [**RemoveEngineOptions**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-removeengineoptions).

### <span id="interrupts"></span><span id="INTERRUPTS"></span>Interrupts

An interrupt is a way to force a break into the debugger or to tell the engine to stop processing the current command, for example, by pressing Ctrl+Break in WinDbg.

To request a break into the debugger, or to interrupt the debugger's current task, use [**SetInterrupt**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setinterrupt). To check if there has been an interrupt, use [**GetInterrupt**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getinterrupt).

**Note**   When undertaking a long task from a debugger extension, it is recommended that the extension check **GetInterrupt** regularly and stop processing if an interrupt has been requested.

 

When requesting a break into the debugger, the engine might time out if it takes too long for the target to carry out the break-in. This can occur if the target is in a non-responsive state or if the break-in request is blocked or delayed by resource contention. The length of time the engine will wait is returned by [**GetInterruptTimeout**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-getinterrupttimeout) and can be set using [**SetInterruptTimeout**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugcontrol3-setinterrupttimeout).

 

