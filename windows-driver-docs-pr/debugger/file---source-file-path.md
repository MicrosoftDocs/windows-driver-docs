---
title: File Source File Path
description: File Source File Path
ms.assetid: 2fa7cbc1-a1e6-411b-95d2-18fd183ee117
keywords: ["File Source File Path", "source files and paths, File Source File Path"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File | Source File Path


## <span id="ddk_file_source_file_path_dbg"></span><span id="DDK_FILE_SOURCE_FILE_PATH_DBG"></span>


Click **Source File Path** on the **File** menu to display, set, or append to the source path.

This command is equivalent to pressing CTRL+P.

### <span id="source_search_path_dialog_box"></span><span id="SOURCE_SEARCH_PATH_DIALOG_BOX"></span>Source Search Path Dialog Box

When you click **Source File Path**, the **Source Search Path** dialog box appears. This dialog box displays the current source path. If the **Source path** box is blank, there is no current source path.

You can enter a new path or edit the old path. If you want to search more than one directory, separate the directory names with semicolons.

If you are performing remote debugging, the **Local** check box will be available. Select this box to edit your debugging client's local source path; clear it to edit the debugging server's source path.

Click **OK** to save changes, or click **Cancel** to discard changes.

You can also click **Browse** to open the **Browse For Folder** dialog box.

### <span id="browse_for_folder_dialog_box"></span><span id="BROWSE_FOR_FOLDER_DIALOG_BOX"></span>Browse For Folder Dialog Box

In the **Browse For Folder** dialog box, you can browse through the folders on your computer or your network. You can also click the **Make New Folder** button to create a new folder. If you right-click a file or folder in this dialog box, a standard Windows shortcut menu appears.

Click **OK** to append the selected folder to the source path and return to the **Source Search Path** dialog box.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information and for other ways to change this path, see [Source Path](source-path.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Source%20File%20Path%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




