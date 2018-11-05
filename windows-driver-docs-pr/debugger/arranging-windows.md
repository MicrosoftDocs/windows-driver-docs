---
title: Arranging Windows
description: Arranging Windows
ms.assetid: f6c0b778-42a8-4073-8cdb-c4b801e59274
keywords: ["debugging information windows, suggestions for docking"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Arranging Windows


## <span id="ddk_suggested_configurations_dbg"></span><span id="DDK_SUGGESTED_CONFIGURATIONS_DBG"></span>


One useful window arrangement is to combine all of your [Source windows](source-window.md) into a single tabbed collection. The easiest way to do this is by marking your first source window as the tab-dock target for all Source windows by selecting the **Set as tab-dock target for window type** option in the Source window's short-cut menu. Once this is done, all future Source windows that are opened will automatically be included in a tabbed collection with this first Source window. The Source window marked as the tab-dock target will not be closed when the **Window | Close All Source Windows** menu command is selected. Thus you can set up a placeholder window for the Source windows that will only be closed when you want it to be.

This collection can occupy half of the WinDbg window or you can put it in a separate dock.

If you want each debugging information window to be completely separate, you can create one dock for each window. This arrangement enables you to minimize or maximize each window separately.

If you want all of your windows to be floating, you should select **Always floating** on each window's shortcut menu so that you can drag each window independently to any location.

Alternatively, you can use the [MDI Emulation](window---mdi-emulation.md) command on the **Window** menu. This command makes all of the windows floating windows and constrains them within the frame window. This behavior emulates the behavior of WinDbg before the introduction of docking mode.

If you are using dual monitors, you can put the WinDbg window in one monitor and an extra dock in the other.

Some standard window arrangements for various debugging scenarios are included in the Debugging Tools for Windows package. For details on these arrangements, see [Using and Customizing WinDbg Themes](using-and-customizing-windbg-themes.md).

 

 





