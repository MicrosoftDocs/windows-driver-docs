---
title: File Symbol File Path
description: File Symbol File Path
ms.assetid: 22d32b1b-d1b9-4627-99ed-08656da9b849
keywords: ["File Symbol File Path", "symbol files and paths, File Symbol File Path"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Symbol File Path


## <span id="ddk_file_symbol_file_path_dbg"></span><span id="DDK_FILE_SYMBOL_FILE_PATH_DBG"></span>


Click **Symbol File Path** on the **File** menu to display, set, or append to the symbol path.

This command is equivalent to pressing CTRL+S.

### <span id="symbol_search_path_dialog_box"></span><span id="SYMBOL_SEARCH_PATH_DIALOG_BOX"></span>Symbol Search Path Dialog Box

When you click **Symbol File Path**, the **Symbol Search Path** dialog box appears. This dialog box displays the current symbol path. If the **Symbol path** box is blank, there is no current symbol path.

You can enter a new path or edit the old path. If you want to search more than one directory, separate the directory names with semicolons.

Click **OK** to save changes, or click **Cancel** to discard changes.

If you select the **Reload** check box, the debugger will reload all loaded symbols and images after you click **OK**. The **Reload** command is equivalent to using the [**.reload (Reload Module)**](-reload--reload-module-.md) command.

You can also click **Browse** to open the **Browse For Folder** dialog box.

### <span id="browse_for_folder_dialog_box"></span><span id="BROWSE_FOR_FOLDER_DIALOG_BOX"></span>Browse For Folder Dialog Box

In the **Browse For Folder** dialog box, you can browse through the folders on your computer or your network. You can also click the **Make New Folder** button to create a new folder. If you right-click a file or folder in this dialog box, a standard Windows shortcut menu appears.

Click **OK** to append the selected folder to the symbol path and return to the **Symbol Search Path** dialog box.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information and for other ways to change the symbol path, see [Symbol Path](symbol-path.md).

 

 





