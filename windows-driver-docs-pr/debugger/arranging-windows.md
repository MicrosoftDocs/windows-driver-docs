---
title: Arranging Windows
description: Arranging Windows
ms.assetid: f6c0b778-42a8-4073-8cdb-c4b801e59274
keywords: ["debugging information windows, suggestions for docking"]
---

# Arranging Windows


## <span id="ddk_suggested_configurations_dbg"></span><span id="DDK_SUGGESTED_CONFIGURATIONS_DBG"></span>


One useful window arrangement is to combine all of your [Source windows](source-window.md) into a single tabbed collection. The easiest way to do this is by marking your first source window as the tab-dock target for all Source windows by selecting the **Set as tab-dock target for window type** option in the Source window's short-cut menu. Once this is done, all future Source windows that are opened will automatically be included in a tabbed collection with this first Source window. The Source window marked as the tab-dock target will not be closed when the **Window | Close All Source Windows** menu command is selected. Thus you can set up a placeholder window for the Source windows that will only be closed when you want it to be.

This collection can occupy half of the WinDbg window or you can put it in a separate dock.

If you want each debugging information window to be completely separate, you can create one dock for each window. This arrangement enables you to minimize or maximize each window separately.

If you want all of your windows to be floating, you should select **Always floating** on each window's shortcut menu so that you can drag each window independently to any location.

Alternatively, you can use the [MDI Emulation](https://msdn.microsoft.com/library/windows/hardware/ff561351) command on the **Window** menu. This command makes all of the windows floating windows and constrains them within the frame window. This behavior emulates the behavior of WinDbg before the introduction of docking mode.

If you are using dual monitors, you can put the WinDbg window in one monitor and an extra dock in the other.

Some standard window arrangements for various debugging scenarios are included in the Debugging Tools for Windows package. For details on these arrangements, see [Using and Customizing WinDbg Themes](using-and-customizing-windbg-themes.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Arranging%20Windows%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




