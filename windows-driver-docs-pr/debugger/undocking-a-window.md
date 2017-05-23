---
title: Undocking a Window
description: Undocking a Window
ms.assetid: e035b511-949f-4ce1-a948-a8b35fd6562f
keywords: ["debugging information windows, undocking windows", "undocked windows", "undocking windows"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Undocking a Window


## <span id="ddk_undocking_a_window_dbg"></span><span id="DDK_UNDOCKING_A_WINDOW_DBG"></span>


To undock a window and make it a floating window, do one of the following:

-   Double-click the window's title bar.

-   Open the shortcut menu by right-clicking the window's title bar, right-clicking the window's tab if it is part of a tabbed collection, or clicking the window's icon in the upper-right corner, and then click **Undock**.

-   In the WinDbg window, on the **Window** menu, click **Undock All**. This command changes all of the docked windows into floating windows.

When you undock a window by one of the preceding methods, the window returns to its previous undocked position.

You can also drag a docked window by clicking its title bar. This action enables you to move the window to a different docked position or undock it. (Dragging a docked window to a new position works exactly like dragging a floating window to a new position. For more information about dragging a floating window to a new position, see [Docking a Window](docking-a-window.md).)

When you try to undock or drag a tabbed window by any of these methods, only the active window in the tabbed collection is moved.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Undocking%20a%20Window%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




