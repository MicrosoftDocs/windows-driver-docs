---
title: Edit Breakpoints
description: Edit Breakpoints
ms.assetid: ca55ee25-aef3-42b1-b628-0a0e849103eb
keywords: ["Edit Breakpoints", "breakpoints, Edit Breakpoints"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Breakpoints


## <span id="ddk_edit_breakpoints_dbg"></span><span id="DDK_EDIT_BREAKPOINTS_DBG"></span>


Click **Breakpoints** on the **Edit** menu to display or control breakpoints.

This command is equivalent to pressing ALT+F9. If a [source window](source-window.md) or the [disassembly window](disassembly-window.md) is not active, you can also press f9 or click the **insert or remove breakpoint (f9)** button (![screen shot of the insert or remove breakpoint button](images/tbbp.png)) on the toolbar.

However, if a Source window or the Disassembly window is open, the **Insert or remove breakpoint (F9)** button and the F9 key set a breakpoint on the current line. (If there is already a breakpoint set at the current line, this button or key will remove the breakpoint.)

If a statement or call spans multiple lines, WinDbg sets the breakpoint on the last line of the statement or call. You should insert the caret (^) on or before the statement to set a breakpoint for the whole statement. If the debugger cannot set a breakpoint at the current caret position, it will search in a downward direction for the next allowed position and insert the breakpoint there.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Breakpoints**, the **Breakpoints** dialog box appears. This dialog box displays all current breakpoint information and is presented in the following columns:

-   The breakpoint number. This number is a decimal number that you can use to refer to the breakpoint in future commands.

-   The breakpoint status. This status can be **e** (enabled) or **d** (disabled).

-   (Unresolved breakpoints only) The letter **u**. This letter appears if the breakpoint is unresolved (that is, it does not match any currently-loaded module address). For details, see [Unresolved Breakpoints (bu Breakpoints)](unresolved-breakpoints---bu-breakpoints-.md).

-   The virtual address of the breakpoint. If you have enabled the loading of source line numbers, the display includes file and line number information instead of address offsets. If the breakpoint is unresolved, the address appears at the end of the listing instead of here.

-   (Processor breakpoints only) Type and size information. This information can be **e** (execute), **r** (read/write), **w** (write), or **i** (input/output). These types are followed with the size of the block, in bytes. For details, see [Processor Breakpoints (ba Breakpoints)](processor-breakpoints---ba-breakpoints-.md).

-   The number of passes that are remaining until the breakpoint becomes active, followed by the initial number of passes in parentheses. The number of times that the program counter passes through the breakpoint without breaking is one less than the value of this number. Therefore, this number is never lower than 1. Note also that this number counts only the times the application executes through this point. In other words, stepping over this point does not count. After the full count has been reached, you can reset the count only by clearing and resetting the breakpoint.

-   The associated process and thread. If thread is given with three asterisks (\*\*\*), this breakpoint is not a thread-specific breakpoint.

-   The module and function, with offset, that correspond to the breakpoint address. If the breakpoint is unresolved, the breakpoint address appears here, in parentheses. If the breakpoint is set on a valid address but symbol information is missing, this column will be blank.

-   The command string that is automatically executed when this breakpoint is hit. This command string is displayed in quotation marks. If the breakpoint is hit, the commands in this command string are executed until application execution resumes. Any command that resumes program execution (such as **g** or **t**) will stop the execution of the command list.

If you select any breakpoint, you can then click the **Remove**, **Disable**, or **Enable** button. The **Remove** button permanently removes the breakpoint. The **Disable** button temporarily deactivates the breakpoint. The **Enable** button re-enables a disabled breakpoint.

The **Remove All** button permanently removes all breakpoints.

You can also enter commands in the **Command** box in the following ways:

-   If you enter a [**bp (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md), **bu (Set Unresolved Breakpoint)**, **bm (Set Symbol Breakpoint)**, [**ba (Break on Access)**](ba--break-on-access-.md), [**bc (Breakpoint Clear)**](bc--breakpoint-clear-.md), [**bd (Breakpoint Disable)**](bd--breakpoint-disable-.md), or [**be (Breakpoint Enable)**](be--breakpoint-enable-.md) command, the **Command** box works as if you were entering the command in the [Debugger Command window](debugger-command-window.md). However, the command itself must be in lowercase letters. The command cannot begin with a thread specifier. If you want to use a thread specifier, enter it in the **Thread** box without the initial tilde (~).

-   If you enter any other text, the text will be treated as the argument string for a [**bu (Set Unresolved Breakpoint)**](bp--bu--bm--set-breakpoint-.md) command. That is, the debugger prefixes your entry with **bu** and a space and then executes it as a command.

When you are entering a new breakpoint, you can also do the following:

-   Create a thread-specific breakpoint by entering a thread specifier in the **Thread** box. Do not include the tilde (~) character that is typically prefixed to a thread specifier.

-   Create a conditional breakpoint by entering a condition in the **Condition** box. The condition can be any evaluable expression, and it will be evaluated according to the current expression syntax (see [Evaluating Expressions](evaluating-expressions.md)). For more information about these types of breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about how to use breakpoints, other breakpoint commands and methods of controlling breakpoints, and setting breakpoints in user space from a kernel debugger, see [Using Breakpoints](using-breakpoints.md). For more information about conditional breakpoints, see [Setting a Conditional Breakpoint](setting-a-conditional-breakpoint.md).

 

 





