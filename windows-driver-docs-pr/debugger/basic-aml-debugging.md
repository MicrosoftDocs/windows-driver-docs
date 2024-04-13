---
title: Basic AML Debugging
description: Basic AML Debugging
keywords: ["AMLI Debugger, basic use"]
ms.date: 11/07/2018
---

# Basic AML Debugging


## <span id="ddk_basic_aml_debugging_dbg"></span><span id="DDK_BASIC_AML_DEBUGGING_DBG"></span>


The AMLI Debugger supports two types of specialized commands: *AMLI Debugger extensions* and *AMLI Debugger commands*.

When you are performing AML debugging, you should carefully distinguish between two different kinds of prompts that will appear in the Debugger Command window:

-   When you see the **kd&gt;** prompt, you are controlling the kernel debugger. All the standard kernel debugger commands and extensions are available. In addition, the AMLI Debugger extensions are also available. These extensions have a syntax of **!amli** *command*. The AMLI Debugger commands are not available in this mode.

-   When you see the **AMLI(? for help)-&gt;** prompt, you are controlling the AMLI Debugger. (When you are using WinDbg, this prompt will appear in the top pane of the Debugger Command window, and an **Input&gt;** prompt will appear in the bottom pane.) From this prompt, you can enter any AMLI Debugger command. You can also enter any AMLI Debugger extension; these extensions should not be prefixed with **!amli**. The standard kernel debugging commands are not available in this mode.

-   When you see no prompt at all, the target computer is running.

At the beginning of any debugging session, you should set your AMLI Debugger options with the [**!amli set**](../debuggercmds/-amli-set.md) extension. The **verboseon**, **traceon**, and **errbrkon** options are also very useful. You should consider activating the **spewon** option. See the extension reference page for details.

There are several ways for the AMLI Debugger to become active:

-   If a breakpoint in AML code is encountered, ACPI will break into the AMLI Debugger.

-   If a serious error or exception occurs within AML code (such as an **int 3**), ACPI will break into the AMLI Debugger.

-   If the **errbrkon** option has been set, any AML error will cause ACPI to break into the AMLI Debugger.

-   If you want to deliberately break into the AMLI Debugger, use the [**!amli debugger**](../debuggercmds/-amli-debugger.md) extension and then the [**g (Go)**](../debuggercmds/g--go-.md) command. The next time any AML code is executed by the interpreter, the AMLI Debugger will take over.

When you are at the AMLI Debugger prompt, you can type **q** to return to the kernel debugger, or type **g** to resume normal execution.

The following extensions are especially useful for AML debugging:

-   The [**!amli dns**](../debuggercmds/-amli-dns.md) extension displays the ACPI namespace for a particular object, the namespace tree subordinate to that object, or even the entire namespace tree. This command is especially useful in determining what a particular namespace object is -- whether it is a method, a fieldunit, a device, or another type of object.

-   The [**!amli find**](../debuggercmds/-amli-find.md) extension takes the name of any namespace object and returns its full path.

-   The [**!amli u**](../debuggercmds/-amli-u.md) extension unassembles AML code.

-   The [**!amli lc**](../debuggercmds/-amli-lc.md) extension displays brief information about all active ACPI contexts.

-   The [**!amli r**](../debuggercmds/-amli-r.md) extension displays detailed information about the current context of the interpreter. This is useful when the AMLI Debugger prompt appears after an error is detected.

-   Breakpoints can be set and controlled within AML code. Use [**!amli bp**](../debuggercmds/-amli-bp.md) to set a breakpoint, [**!amli bc**](../debuggercmds/-amli-bc.md) to clear a breakpoint, [**!amli bd**](../debuggercmds/-amli-bd.md) to disable a breakpoint, [**!amli be**](../debuggercmds/-amli-be.md) to re-enable a breakpoint, and [**!amli bl**](../debuggercmds/-amli-bl.md) to list all breakpoints.

-   The AMLI Debugger is able to run, step, and trace through AML code. Use the **run**, **p**, and **t** commands to perform these actions.

For a full list of extensions and commands, see [Using AMLI Debugger Extensions](using-amli-debugger-extensions.md) and [Using AMLI Debugger Commands](using-amli-debugger-commands.md).

## See Also

[The AMLI Debugger](the-amli-debugger.md)
