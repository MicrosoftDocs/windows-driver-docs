---
title: Debug Modules
description: Debug Modules
ms.assetid: 4107ff36-31c4-45a6-95f6-b647543f01be
keywords: ["Debug Modules", "executable files and paths, Debug Modules"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debug | Modules


## <span id="ddk_debug_modules_dbg"></span><span id="DDK_DEBUG_MODULES_DBG"></span>


Click **Modules** on the **Debug** menu to display the current list of loaded modules.

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Modules**, the **Module List** dialog box appears. This dialog box lists all modules that are currently loaded into memory.

**Module List** is divided into the following columns:

-   The **Name** column specifies the module name.

-   The **Start** and **End** columns specify the first and last address of the module's memory image.

-   The **Timestamp** column specifies the build date and time for the module.

-   The **Checksum** column specifies the checksum value.

-   The **Symbols** column displays information about the symbols that this module uses. For more information about the values that appear in this column, see [Symbol Status Abbreviations](symbol-status-abbreviations.md).

-   The **Symbol file** column specifies the path and file name of the associated symbol file. If the debugger is unaware of any symbol file, the name of the executable file is given instead.

If you click the title bar of a column, the display is sorted by the data in that column. If you click the title bar again, the sort order reverses.

If you select a line and then click **Reload**, that module's symbol information is reloaded.

If you select a line and press CTRL+C, the whole line is copied to the clipboard.

Click **Close** to close this dialog box.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20|%20Modules%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




