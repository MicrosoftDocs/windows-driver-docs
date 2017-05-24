---
title: Using the Scratch Pad
description: Using the Scratch Pad
ms.assetid: a0f6ce9c-7fad-4df6-bad8-0ea1bc5bfc52
keywords: ["debugging information windows, Scratch Pad", "Scratch Pad"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using the Scratch Pad


## <span id="ddk_scratch_pad_dbg"></span><span id="DDK_SCRATCH_PAD_DBG"></span>


The Scratch Pad window is a clipboard on which you can type and save text.

### <span id="opening_the_scratch_pad_window"></span><span id="OPENING_THE_SCRATCH_PAD_WINDOW"></span>Opening the Scratch Pad Window

To open or switch to the Scratch Pad window, in the WinDbg window, on the **View** menu, click **Scratch Pad**. (You can also press ALT+8 or click the **Scratch Pad (Alt+8)** button (![screen shot of the scratch pad button](images/tbspad.png)) on the toolbar.)

The following screen shot shows an example of a Scratch Pad window.

![screen shot of the scratch pad window](images/window-scratchpad.png)

### <span id="using_the_scratch_pad_window"></span><span id="USING_THE_SCRATCH_PAD_WINDOW"></span>Using the Scratch Pad Window

In the Scratch Pad window, you can do the following:

-   To type in the Scratch Pad window, click in the window where you want to add text and begin typing. You can also use standard copy-and-paste features. The contents of the Scratch Pad window do not affect the operation of the debugger. This window exists solely to help with text editing.

-   If you close the Scratch Pad window, your text is preserved and is available when you reopen the window. You can also save text from the Scratch Pad window by associating it with a file.

The Scratch Pad window has a shortcut menu with additional commands. To access the menu, right-click the title bar or click the icon near the upper-right corner of the window (![screen shot of the button that displays the scratch pad window toolbar shortcut menu](images/tbspad.png)). This menu contains the following commands:

-   (Menu only) **Associate with file** opens a dialog box through which you can select a text file. After the file is selected, the current text in the Scratch Pad is cleared and replaced with the text in the selected file. While Scratch Pad is associated with this file, all new text typed into Scratch Pad is saved to the file. Association with the file can be ended either by selecting the **End file association** short-cut menu option or by closing and reopening Scratch Pad.

-   (Menu only) **End file association** ends Scratch Pad's association with a specified text file. All text in Scratch Pad prior to selecting this option is saved in the file. All text typed in Scratch Pad after the association is ended is no longer saved in the text file.

-   **Dock** or **Undock** causes the window to enter or leave the docked state.

-   (Menu only) **Move to new dock** closes Scratch Pad and opens it in a new dock.

-   (Menu only) **Set as tab-dock target for window type** is unavailable for Scratch Pad. This option is only available for [Source](source-window.md) or [Memory](memory-window.md) windows.

-   **Always floating** causes the window to remain undocked even if it is dragged to a docking location.

-   **Move with frame** causes the window to move when the WinDbg frame is moved, even if the window is undocked. For more information about docked, tabbed, and floating windows, see [Positioning the Windows](positioning-the-windows.md).

-   **Help** opens this topic in the Debugging Tools for Windows documentation.

-   **Close** closes this window.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about docked, tabbed, and floating windows, see [Positioning the Windows](positioning-the-windows.md). For more information about all techniques that you can use to control debugging information windows, see [Using Debugging Information Windows](using-debugging-information-windows.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20the%20Scratch%20Pad%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




