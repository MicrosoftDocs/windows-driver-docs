---
title: View Options
description: View Options
ms.assetid: 2579c586-f1f3-4b03-a47f-22be98fe6c51
keywords: ["View Options"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# View | Options


## <span id="ddk_view_options_dbg"></span><span id="DDK_VIEW_OPTIONS_DBG"></span>


Click **Options** on the **View** menu to open the **Options** dialog box. This command is equivalent to clicking the button (![screen shot of the options button](images/tbopt.png)) on the toolbar.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

In the **Options** dialog box, you can select or deselect the following options:

<span id="Tab_width"></span><span id="tab_width"></span><span id="TAB_WIDTH"></span>**Tab width**  
The **Tab width** box controls how tab characters are displayed in any Source window. In the **Tab width** box, enter the number of spaces that you want to have between each tab setting. (The default setting is 8. For more information about text properties, see [Changing Text Properties](changing-text-properties.md).)

<span id="Reuse_after_opening_this_many"></span><span id="reuse_after_opening_this_many"></span><span id="REUSE_AFTER_OPENING_THIS_MANY"></span>**Reuse after opening this many**  
The **Reuse after opening this many** box controls the number of document, or source, windows that can be open at the same time. If the specified number of source windows has been reached, opening a new window causes an existing window to close. Windows that are marked as tab-dock targets do not close. The last windows to close are the ones you used most recently.

<span id="Parse_source_languages"></span><span id="parse_source_languages"></span><span id="PARSE_SOURCE_LANGUAGES"></span>**Parse source languages**  
If the **Parse source languages** check box is selected, the text of source code in all Source windows is colored according to a simple parse of the source syntax. To change the colors, in the **Colors** area of the dialog box, select a syntax element and then click **Change**. (To turn the syntax colors off in a single Source window, open that window's shortcut menu, click **Select source language**, and then click **&lt;None&gt;**.)

<span id="Evaluate_on_hover"></span><span id="evaluate_on_hover"></span><span id="EVALUATE_ON_HOVER"></span>**Evaluate on hover**  
If the **Evaluate on hover** check box is selected (and the **Parse source languages** check box is selected as well), symbols in a Source window will be evaluated when you select that window and then hover over a symbol with the mouse. The evaluation is the same as that produced by the [**dt (Display Type)**](dt--display-type-.md) command.

<span id="Enter_repeats_last_command"></span><span id="enter_repeats_last_command"></span><span id="ENTER_REPEATS_LAST_COMMAND"></span>**Enter repeats last command**  
If the **Enter repeats last command** check box is selected, you can press the ENTER key at an empty prompt in the [Debugger Command window](debugger-command-window.md) to repeat the previous command. If you clear this check box, the ENTER key generates a new prompt.

<span id="Automatically_scroll"></span><span id="automatically_scroll"></span><span id="AUTOMATICALLY_SCROLL"></span>**Automatically scroll**  
The **Automatically scroll** check box controls the automatic scrolling that occurs when new text is sent to the Debugger Command window. If you want to turn off this feature, clear the **Automatically scroll** check box. For more information about this scrolling, see [Using Debugger Commands](using-debugger-commands.md).

<span id="Workspace_Prompts"></span><span id="workspace_prompts"></span><span id="WORKSPACE_PROMPTS"></span>**Workspace Prompts**  
In the **Workspace Prompts** area, you can click one of three options to determine when and how frequently the workspace is saved in WinDbg.

-   If you click **Always ask**, when a workspace changes (such as when a debugging session ends), the debugger displays the **Workspace save** dialog box where you can save the workspace.

    In the **Workspace save** dialog box, if you click **Don't ask again**, WinDbg resets the **Workspace Prompts** option to **Never save** or **Always save**.

-   If you click **Always save**, the workspace is saved automatically whenever it changes.

-   If you click **Never save**, the workspace is not saved when it changes, and you are not prompted to save it.

<span id="QuickEdit_Mode"></span><span id="quickedit_mode"></span><span id="QUICKEDIT_MODE"></span>**QuickEdit Mode**  
If the **QuickEdit Mode** check box is selected, you can right-click an item to copy or paste, depending on the window selection state. When you clear this check, QuickEdit is disabled and you can right-click an item to open a shortcut menu for the window. You cannot give individual windows different settings; the QuickEdit setting applies globally to all windows. By default, this box is selected. The QuickEdit setting is saved in the current workspace.

<span id="Colors"></span><span id="colors"></span><span id="COLORS"></span>**Colors**  
To change the color of the source text that is displayed, select an item from the **Colors** area and then click **Change**. Select a color, or select a custom color, and then click **OK**.

In the **Colors** menu, you can change the colors of the following items:

-   The first ten items represent text in the [Disassembly window](disassembly-window.md) and the [Source window](source-window.md).

-   The **Changed data text** item represents data entries that have been changed (for example, in the [Registers window](registers-window.md)).

-   The ten **Source** *Xxx* items control the colors that are used for syntax elements in the Source window.

-   The remaining items refer to different kinds of text in the Debugger Command window.

These color changes take effect when you click **OK**. To discard these changes, click **Cancel**.

 

 





