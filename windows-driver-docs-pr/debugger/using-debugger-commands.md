---
title: Using Debugger Commands
description: This section describes using Debugger Commands. You enter commands at the prompt at the bottom of the window.
ms.assetid: 64dcc364-53b5-41d3-9266-abcfe4b328f4
keywords: commands, debugger commands, meta-commands
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using Debugger Commands


## <span id="ddk_using_debugger_commands_dbg"></span><span id="DDK_USING_DEBUGGER_COMMANDS_DBG"></span>


For KD or CDB, "Debugger Command window" refers to the whole window. You enter commands at the prompt at the bottom of the window. If the commands have any output, the window displays the output and then displays the prompt again.

For Visual Studio, "Debugger Command window" refers to a window that is labeled "Debugger Immediate Window" in the title bar. This window has two panes:

-   In the small, bottom pane, you enter commands.

-   In the large, upper pane, you view command output.

For WinDbg, "Debugger Command window" refers to the window that is labeled "Command" in the title bar. This window contains two panes:

-   In the small, bottom pane, you enter commands.

-   In the large, upper pane, you view command output.

This window is always open at the beginning of a debugging session. You can reopen or switch to this window by clicking **Command** on the **View** menu, pressing ALT+1, or clicking the **Command (Alt+1)** button (![screen shot of the debugger command window button](images/tbcmd.png)) on the toolbar.

You can use the UP ARROW and DOWN ARROW keys to scroll through the command history. When a previous command appears, you can edit it and then press ENTER to execute the previous command (or the edited version of the previous command). The cursor does not have to be at the end of the line for this procedure to work correctly.

### <span id="debugger_command_window_prompt"></span><span id="DEBUGGER_COMMAND_WINDOW_PROMPT"></span>Debugger Command Window Prompt

When you are performing user-mode debugging, the prompt in the Debugger Command window looks like the following example.

`2:005>`

In the preceding example, 2 is the current process number, and 005 is the current thread number.

If you attach the debugger to more than one computer, the system number is included before the process and thread number, as in the following example.

`3:2:005>`

In this example, 3 is the current system number, 2 is the current process number, and 005 is the current thread number.

When you are performing kernel-mode debugging on a target computer that has only one processor, the prompt looks like the following example.

`kd>`

However, if the target computer has multiple processors, the number of the current processor appears before the prompt, as in the following example.

`0: kd> `

If the debugger is busy processing a previously issued command, new commands will temporarily not be processed, although they can be added to the command buffer. In addition, you can still use [control keys](control-keys.md) in KD and CDB, and you can still use menu commands and [shortcut keys](keyboard-shortcuts.md) in WinDbg. When KD or CDB is in this busy state, no prompt is displayed. When WinDbg is in this busy state, the following indicator will appear in place of the prompt:

`*BUSY* `

You can use the [**.pcmd (Set Prompt Command)**](-pcmd--set-prompt-command-.md) command to add text to this prompt.

### <span id="kinds_of_commands"></span><span id="KINDS_OF_COMMANDS"></span>Kinds of Commands

WinDbg, KD, and CDB support a variety of commands. Some commands are shared between the debuggers, and some are available only on one or two of the debuggers.

Some commands are available only in live debugging, and other commands are available only when you debug a dump file.

Some commands are available only during user-mode debugging, and other commands are available only during kernel-mode debugging.

Some commands are available only when the target is running on certain processors. For more information about all of the commands and their restrictions, see [Debugger Commands](debugger-commands.md).

### <span id="editing__repeating__and_canceling_commands"></span><span id="EDITING__REPEATING__AND_CANCELING_COMMANDS"></span>Editing, Repeating, and Canceling Commands

You can use standard editing keys when you enter a command:

-   Use the UP ARROW and DOWN ARROW keys to find previous commands.

-   Edit the current command with the BACKSPACE, DELETE, INSERT, and LEFT ARROW and RIGHT ARROW keys.

-   Press the ESC key to clear the current line.

You can press the TAB key to automatically complete your text entry. In any of the debuggers, press the TAB key after you enter at least one character to automatically complete a command. Press the TAB key repeatedly to cycle through text completion options, and hold down the SHIFT key and press TAB to cycle backward. You can also use wildcard characters in the text and press TAB to expand to the full set of text completion options. For example, if you type **fo\*!ba** and then press TAB, the debugger expands to the set of all symbols that start with "ba", in all modules with module names that start with "fo". As another example, you can complete all extension commands that have "prcb" in them by typing **!\*prcb** and then pressing TAB.

When you use the TAB key to perform text completion, if your text fragment begins with a period (.), the text is matched to a dot command. If your text fragment begins with an exclamation point (!), the text is matched to an extension command. Otherwise, the text is matched with a symbol. When you usee the TAB key to enter symbols, pressing the TAB key completes code and type symbols and module names. If no module name is apparent, local symbols and module names are completed. If a module or module pattern is given, symbol completion completes code and type symbols from all matches.

You can right-click in the Debugger Command window to automatically paste the contents of the clipboard into the command that you are typing.

The maximum command length is 4096 characters. However, if you are [controlling the user-mode debugger from the kernel debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md), the maximum line length is 512 characters.

In CDB and KD, press the ENTER key by itself to repeat the previous command. In WinDbg, you can enable or disable this behavior. For more information about this behavior, see [**ENTER (Repeat Last Command)**](enter--repeat-last-command-.md).

If the last command that you issued presents a long display and you want to cut it off, use the [**CTRL+C**](ctrl-c--break-.md) key in CDB or KD. In WinDbg, use [Debug | Break](debug---break.md) or press CTRL+BREAK.

In kernel-mode debugging, you can cancel commands from the keyboard of the target computer by pressing [**CTRL+C**](ctrl-c--break-.md).

You can use the [**.cls (Clear Screen)**](-cls--clear-screen-.md) command to clear all of the text from the [Debugger Command window](debugger-command-window.md). This command clears the whole command history. In WinDbg, you can clear the command history by using the [Edit | Clear Command Output](edit---clear-command-output.md) command or by clicking **Clear command output** on the shortcut menu of the Debugger Command window.

### <span id="expression_syntax"></span><span id="EXPRESSION_SYNTAX"></span>Expression Syntax

Many commands and extension commands accept *expressions* as their arguments. The debugger evaluates these expressions before executing the command. For more information about expressions, see [Evaluating Expressions](evaluating-expressions.md).

### <span id="aliases"></span><span id="ALIASES"></span>Aliases

*Aliases* are text macros that you can use to avoid having to retype complex phrases. There are two kinds of aliases. For more information about aliases, see [Using Aliases](using-aliases.md).

### <span id="self_repeating_commands"></span><span id="SELF_REPEATING_COMMANDS"></span>Self-Repeating Commands

You can use the following commands to repeat an action or conditionally execute other commands:

-   The [**j (Execute If-Else)**](j--execute-if---else-.md) conditional command

-   The [**z (Execute While)**](z--execute-while-.md) conditional command

-   The [**~e (Thread-Specific Command)**](-e--thread-specific-command-.md) command qualifier

-   The [**!list**](-list.md) extension command

For more information about each command, see the individual command topics.

### <span id="controlling_scrolling"></span><span id="CONTROLLING_SCROLLING"></span>Controlling Scrolling

You can use the scrollbar to view your previous commands and their output.

When you are using CDB or KD, any keyboard entry automatically scrolls down the Debugger Command window back to the bottom.

In WinDbg, the display automatically scrolls down to the bottom whenever a command produces output or you press the ENTER key. If you want to disable this automatic scrolling, click the [Options](view---options.md) on the **View** menu and then clear the **Automatically scroll** check box.

### <span id="windbg_text_features"></span><span id="WINDBG_TEXT_FEATURES"></span>WinDbg Text Features

In WinDbg, you can use several additional features to change how text is displayed in the [Debugger Command window](debugger-command-window.md). You can access some of these features in the WinDbg window, some in the shortcut menu in the Debugger Command window, and some by clicking on the appropriate menu icon.

-   The **Word wrap** command on the shortcut menu turns on and off the word wrap status. This command affects the whole window, not only commands that you use after this state is changed. Because many commands and extensions produce formatted displays, we typically do not recommend word wrap.

-   The [Edit | Add to Command Output](edit---add-to-command-output.md) menu command adds a comment in the Debugger Command window. The **Add to command output** command on the shortcut menu has the same effect.

-   You can customize the colors that are used for the text and the background of the Debugger Command window. You can specify different colors for different kinds of text. For example, you can display the automatic register output in one color, error messages in another color, and **DbgPrint** messages in a third color. For more information about this customization, see [View | Options](view---options.md).

-   You can use all of the features common to WinDbg's debugging information windows, such as customizing the fonts and using special editing commands. For more information about these features, see [Using Debugging Information Windows](using-debugging-information-windows.md).

### <span id="remote_debugging"></span><span id="REMOTE_DEBUGGING"></span>Remote Debugging

When you are performing remote debugging through the debugger, the debugging client can access a limited number of commands. To change the number of commands that the client can access, use the **-clines** [command-line option](command-line-options.md) or the \_NT\_DEBUG\_HISTORY\_SIZE [environment variable](environment-variables.md).

 

 





