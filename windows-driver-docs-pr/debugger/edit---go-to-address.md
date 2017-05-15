---
title: Edit Go to Address
description: Edit Go to Address
ms.assetid: 152bdbb1-87e5-4a73-a1b7-1c4997f4a41c
keywords: ["Edit Go to Address"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Edit%20|%20Go%20to%20Address%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




