---
title: Edit Go to Line
description: Edit Go to Line
ms.assetid: af7f2afc-95cb-4dcd-9b74-1bd46713239f
keywords: ["Edit Go to Line"]
---

# Edit | Go to Line


## <span id="ddk_edit_go_to_line_dbg"></span><span id="DDK_EDIT_GO_TO_LINE_DBG"></span>


Click **Go to Line** on the **Edit** menu to search for a specific line in the currently-active [Source window](source-window.md). If the active window is not a Source window, this command has no effect.

This command is equivalent to pressing CTRL+L.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Go to Line**, the **Go to Line** dialog box appears. In this dialog box, enter the line number that you want to find and then click **OK**. The debugger will move the caret (^) to that line. If the line number is bigger than the last line in the file, the cursor will move to the end of the file.

The **Go to Line** command only changes the WinDbg display. This command does not affect the execution of the target or any other debugger operations.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about other ways of finding text in debugging information windows, see [Moving Through a Window](moving-through-a-window.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Edit%20|%20Go%20to%20Line%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




