---
title: File Image File Path
description: File Image File Path
ms.assetid: d2a827b5-bba0-4840-8e74-5b24c9eb6a22
keywords: ["File Image File Path", "executable files and paths, File Image File Path"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Image File Path


## <span id="ddk_file_image_file_path_dbg"></span><span id="DDK_FILE_IMAGE_FILE_PATH_DBG"></span>


Click **Image File Path** on the **File** menu to display, set, or append to the executable image path.

This command is equivalent to pressing CTRL+I.

### <span id="executable_image_search_path_dialog_box"></span><span id="EXECUTABLE_IMAGE_SEARCH_PATH_DIALOG_BOX"></span>Executable Image Search Path Dialog Box

When you click **Image File Path**, the **Executable Image Search Path** dialog box appears. This dialog box displays the current executable image path. If the **Image path** box is blank, there is no current executable image path.

You can enter a new path or edit the old path. If you want to search more than one directory, separate the directory names with semicolons.

Click **OK** to save changes, or click **Cancel** to discard changes.

If you select the **Reload** check box, the debugger will reload all loaded image and symbol files after you click **OK**. This command is equivalent to using the [**.reload (Reload Module)**](-reload--reload-module-.md) command.

You can also click **Browse** to open the **Browse For Folder** dialog box.

### <span id="browse_for_folder_dialog_box"></span><span id="BROWSE_FOR_FOLDER_DIALOG_BOX"></span>Browse For Folder Dialog Box

In the **Browse For Folder** dialog box, you can browse through the folders on your computer or your network. You can also use the **Make New Folder** button to create a new folder. If you right-click a file or folder in this dialog box, a standard Windows shortcut menu appears.

Click **OK** to append the selected folder to the executable image path and return to the **Executable Image Search Path** dialog box.

 

 





