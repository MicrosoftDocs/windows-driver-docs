---
title: Edit Find
description: Edit Find
ms.assetid: 9e3a0095-1bce-4262-a22c-584de54113cc
keywords: ["Edit Find"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Edit%20|%20Find%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




