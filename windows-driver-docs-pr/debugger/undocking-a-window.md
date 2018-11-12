---
title: Undocking a Window
description: Undocking a Window
ms.assetid: e035b511-949f-4ce1-a948-a8b35fd6562f
keywords: ["debugging information windows, undocking windows", "undocked windows", "undocking windows"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
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

 

 





