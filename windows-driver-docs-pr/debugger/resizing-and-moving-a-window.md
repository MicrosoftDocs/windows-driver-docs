---
title: Resizing and Moving a Window
description: Resizing and Moving a Window
ms.assetid: 135e1ec1-9d58-45de-a0b4-5f962ed9e1f7
keywords: ["debugging information windows, resizing and moving a window", "resizing and moving windows"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Resizing and Moving a Window


## <span id="ddk_resizing_and_moving_windows_dbg"></span><span id="DDK_RESIZING_AND_MOVING_WINDOWS_DBG"></span>


Floating windows are always associated with the WinDbg window. If you minimize WinDbg, all floating windows are minimized. And if you restore WinDbg, all floating windows are restored. You can never put a floating window behind the WinDbg window.

Each floating window moves independently from each other and from the WinDbg window, unless you have selected **Move with frame** on the window's shortcut menu.

A docked window occupies a fixed position within the WinDbg frame. If you resize WinDbg, all of the docked windows are automatically scaled to the new size. The same situation applies to windows that have been docked in a separate dock.

If you move the mouse pointer to the border between two docked windows, the mouse pointer becomes an arrow. By dragging this arrow, you can resize the two adjacent windows and leave them in the docked state.

The WinDbg window is always filled with docked windows. There is never any empty area in the window unless there are no windows docked. The same situation applies to independent docks.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Resizing%20and%20Moving%20a%20Window%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




