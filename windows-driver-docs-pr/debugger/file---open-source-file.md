---
title: File Open Source File
description: File Open Source File
ms.assetid: 27007865-7517-40df-a30a-26ecf3cec9f5
keywords: ["File Open Source File", "source debugging, File Open Source File"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# File | Open Source File


## <span id="ddk_file_open_source_file_dbg"></span><span id="DDK_FILE_OPEN_SOURCE_FILE_DBG"></span>


Click **Open Source File** on the **File** menu to load a specific source file.

This command is equivalent to pressing CTRL+O or clicking the **Open source file (Ctrl+O)** button (![screen shot of the open source file button](images/tbopen.png)).

### <span id="dialog_box"></span><span id="DIALOG_BOX"></span>Dialog Box

When you click **Open Source File**, the **Open Source File** dialog box appears. To open a file, do the following:

1.  In the **Look in** list, select the directory where the file is located. The directory last opened is selected by default.

2.  In the **Files of type** list, select the type of file that you want to open. Only files with the chosen extensions are displayed in the **Open Source File** dialog box.
    **Note**  You can also use wildcard patterns in the **File name** box to display only files with a certain extension. The new wildcard pattern is retained in a session until you change it. You can use any combination of wildcard patterns, separated by semicolons. For example, entering **\*.INC; \*.H; \*.CPP** displays all files with these extensions. The maximum number of characters in a line is 251.

     

3.  If you find the file you want, double-click the file name, or click the file name and click **Open**.

    -OR-

    To discard changes and close the dialog box, click **Cancel**.

The names of the four files that you opened most recently in WinDbg are displayed when you point to **Recent files** on the **File** menu. To open one of these files, click its name.

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about source files and source paths and for other ways to load source files, see [Source Path](source-path.md).

 

 





