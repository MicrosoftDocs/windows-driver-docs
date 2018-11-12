---
title: Edit Go to Address
description: Edit Go to Address
ms.assetid: 152bdbb1-87e5-4a73-a1b7-1c4997f4a41c
keywords: ["Edit Go to Address"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Edit | Go to Address


## <span id="ddk_edit_go_to_address_dbg"></span><span id="DDK_EDIT_GO_TO_ADDRESS_DBG"></span>


Click **Go to Address** on the **Edit** menu to go to an address in the target's virtual address space.

This command is equivalent to pressing CTRL+G.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Go to Address**, the **View Code Offset** dialog box appears. In this dialog box, enter the address that you want to move to. This address can be an expression (such as a function, symbol, or integer memory address) or any valid address expression. If the address is ambiguous, the dialog box displays a list that contains all of the ambiguous items.

**Note**   If you put the cursor on a line within the [Disassembly window](disassembly-window.md) or a [Source window](source-window.md) and then use the**Go to Address** command, the address of the line that you have selected will appear in the **View Code Offset** dialog box. You can use this address or replace it with any address of your choice.

 

After you click **OK**, the debugger moves the caret (^) to the beginning of the function or address in the Disassembly window or a Source window.

You can use the **Go to Address** command in any window that is currently active. If the debugger is in disassembly mode, WinDbg finds the address in the Disassembly window. If the debugger is in source mode, WinDbg finds the address in a Source window. If the address cannot be found in a Source window, WinDbg finds it in the Disassembly window. If the appropriate window is not open, WinDbg opens it.

The **Go to Address** command only changes the WinDbg display. This command does not affect the execution of the target or any other debugger operations.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about other ways of finding text in debugging information windows, see [Moving Through a Window](moving-through-a-window.md).

 

 





