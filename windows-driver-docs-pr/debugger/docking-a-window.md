---
title: Docking a Window
description: Docking a Window
ms.assetid: e8963a3b-0e86-4f4f-a59e-27cbde6a6ff8
keywords: ["debugging information windows, docking windows", "docking windows", "window docking"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Docking a Window


## <span id="ddk_docking_a_window_dbg"></span><span id="DDK_DOCKING_A_WINDOW_DBG"></span>


To dock a floating window, do one of the following:

-   Double-click the window's title bar.

-   Open the shortcut menu by right-clicking the window's title bar or clicking the window's icon in the upper-right corner, and then click **Dock**.

-   In the WinDbg window, on the **Window** menu, click **Dock All**. This command docks all of the windows except those that have the **Always floating** option selected on their individual shortcut menus.

-   Drag the window to a docking location. This action causes the window to dock unless **Always floating** is selected on the shortcut menu for that window, or unless you press and hold the ALT key as you begin dragging the window.

When you dock a window by any method other than dragging it, WinDbg automatically positions the docked window. If the window has never been docked before, WinDbg moves the window to a new untabbed location within the WinDbg window. If the window has been docked before, WinDbg returns the window to its most recent docking location, which might be tabbed or untabbed.

When you dock a window by dragging it, you can control its destination position. As you drag the window, you will see a semi-transparent outline of the window appear. This outline shows where the window will be docked if you release the mouse button at that point. The following rules determine where a dragged window is docked:

-   If you drag the mouse pointer over the WinDbg window when the window is empty or over an empty dock, and then you release the mouse button, the dragged window is docked in that location and completely fills the frame or dock.

-   If you drag the mouse pointer over the left, right, top, or bottom portion of an already-docked window and then you release the mouse button, the dragged window is docked to the left, right, top, or bottom of the already-docked window, respectively.

-   When you drag the mouse pointer over a floating window (including the original position of the window that you are dragging), no docking occurs. This exception means that you might have to drag other windows out of the way (or drag the current window two times) before you can move the window to where you want it.

-   If you drag the mouse pointer to a position that is not inside the WinDbg frame or any other dock and then you release the mouse button, the dragged window remains floating.

All of the preceding rules apply to the mouse pointer location itself. They do not depend on where you originally clicked within the title bar of the window that you are dragging.

### <span id="re_docking"></span><span id="RE_DOCKING"></span>Re-docking

If you let WinDbg automatically dock a floating window that was previously docked, WinDbg tries to put the window in the same docking position that it previously occupied. Also, if you load a workspace, WinDbg tries to restore all of the debugging information windows to their previous positions, whether docked or floating.

However, multiple instances of [Memory windows](memory-window.md) and [Source windows](source-window.md) are not distinguished when the docking position is saved. For example, if you combine the [Locals window](locals-window.md) together with a Memory window in a tabbed collection, and this state is saved and later restored, the Locals window joins a Memory window in a tabbed collection, but it might not be the same Memory window as before.

If you load a workspace that includes one or more Source windows when the source files are inaccessible, those Source windows are not reopened. When this situation occurs, other windows that were tabbed together with those windows might return to the floating state. If you want to keep all of your Source windows tabbed together, you should include at least one source file that is always present, or include an additional window in the tabbed collection.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Docking%20a%20Window%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




