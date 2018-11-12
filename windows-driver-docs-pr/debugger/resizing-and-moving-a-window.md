---
title: Resizing and Moving a Window
description: Resizing and Moving a Window
ms.assetid: 135e1ec1-9d58-45de-a0b4-5f962ed9e1f7
keywords: ["debugging information windows, resizing and moving a window", "resizing and moving windows"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Resizing and Moving a Window


## <span id="ddk_resizing_and_moving_windows_dbg"></span><span id="DDK_RESIZING_AND_MOVING_WINDOWS_DBG"></span>


Floating windows are always associated with the WinDbg window. If you minimize WinDbg, all floating windows are minimized. And if you restore WinDbg, all floating windows are restored. You can never put a floating window behind the WinDbg window.

Each floating window moves independently from each other and from the WinDbg window, unless you have selected **Move with frame** on the window's shortcut menu.

A docked window occupies a fixed position within the WinDbg frame. If you resize WinDbg, all of the docked windows are automatically scaled to the new size. The same situation applies to windows that have been docked in a separate dock.

If you move the mouse pointer to the border between two docked windows, the mouse pointer becomes an arrow. By dragging this arrow, you can resize the two adjacent windows and leave them in the docked state.

The WinDbg window is always filled with docked windows. There is never any empty area in the window unless there are no windows docked. The same situation applies to independent docks.

 

 





