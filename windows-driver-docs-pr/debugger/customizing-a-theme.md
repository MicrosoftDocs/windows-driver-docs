---
title: Customizing a Theme
description: Customizing a Theme
ms.assetid: 3dddbf19-34ec-4cb0-b427-854ae7622fa1
keywords: ["themes, customizing"]
---

# Customizing a Theme


## <span id="ddk_creating_and_opening_a_workspace_dbg"></span><span id="DDK_CREATING_AND_OPENING_A_WORKSPACE_DBG"></span>


Before customizing a theme, it must first be loaded. See [Loading a Theme](loading-a-theme.md) for details.

After the theme is loaded, start WinDbg with no command-line parameters. This opens the base workspace. There are two common areas of focus for customizing a theme: setting paths and adjusting window position.

After you have completed any wanted adjustments, exit WinDbg and save your workspace by selecting **Save Workspace** from the **File** menu. If you want to save your new settings to a .reg file, open Regedit and export the registry key under **HKCU\\Software\\Microsoft\\Windbg\\Workspaces** to a .reg file.

### <span id="setting_paths"></span><span id="SETTING_PATHS"></span>Setting Paths

By setting the appropriate paths, you can ensure that WinDbg can locate all of the files that it needs to debug effectively. There are three main paths to set: the symbol path, the source path, and the executable image path.

Here are examples of how to set the symbol and source path. The executable image path is typically the same as your symbol path.

To set your symbol path:

```
SRV*c:\MySymCache*\\CompanySymbolServer\Symbols;SRV*c:\WinSymCache*https://msdl.microsoft.com/download/symbols
```

To set your source path:

```
SRV*;d:\MySourceRoot
```

### <span id="adjusting_window_position"></span><span id="ADJUSTING_WINDOW_POSITION"></span>Adjusting Window Position

Before using your theme, you should adjust the window positioning so that WinDbg handles your source files correctly. This ensures that Source windows knows where to dock.

Begin by opening a Source window in WinDbg. Tab-dock this window with the placeholder set aside for your Source windows. In order for the proper relationship to be made, the placeholder window must be the uppermost window in the dock before you perform this tab-docking operation. Now close the source window but not the placeholder window.

Because debugging information windows "remember" their last docking operation, each source window's last docking operation is associated with one of the placeholder windows after you have performed this procedure. Because of this memory attribute, you should not close any of your placeholder windows. Further, if you choose to change the theme's configuration, any window you reposition in a dock should always be tab-docked with a placeholder file.

The sample themes included with the Debugging Tools for Windows were created using the following actions:

Place and position the placeholder\*.c files into the dock.

Tab-dock every window type above the wanted placeholder window.

For further information about adjusting window position in WinDbg, see [Positioning the Windows](positioning-the-windows.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Customizing%20a%20Theme%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




