---
title: Edit Find
description: Edit Find
ms.assetid: 9e3a0095-1bce-4262-a22c-584de54113cc
keywords: ["Edit Find"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Find


## <span id="ddk_edit_find_dbg"></span><span id="DDK_EDIT_FIND_DBG"></span>


Click **Find** on the **Edit** menu to find text in the active debugging information window.

**Note**  The active window must be the [Debugger Command window](debugger-command-window.md) or a [Source window](source-window.md).

 

This command is equivalent to pressing CTRL+F.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Find**, the **Find** dialog box appears. In this dialog box, in the **Find what** box, enter the text that you want to find. If there is already text selected, this text automatically appears in the **Find what** box.

In the **Direction** area, click **Up** or **Down** to specify the direction of your search. The search begins wherever the cursor is in the window. You can put the cursor at any location by using the mouse pointer.

Select **Match whole word only** if you want to search for a single whole word. (If you select this option when you search for multiple words, you always receive a failed search.))

Select **Match case** to perform a case-sensitive search.

The **Find** command only changes the WinDbg display. This command does not affect the execution of the target or any other debugger operations.

After you close the **Find** dialog box, you can repeat the search in a forward direction by using the [Edit | Find Next](edit---find-next.md) command or pressing F3. You can repeat the search in a backward direction by pressing SHIFT+F3.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about other ways to find text in debugging information windows, see [Moving Through a Window](moving-through-a-window.md).

 

 





