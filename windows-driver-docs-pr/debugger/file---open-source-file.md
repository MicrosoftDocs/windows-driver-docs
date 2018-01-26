---
title: File Open Source File
description: File Open Source File
ms.assetid: 27007865-7517-40df-a30a-26ecf3cec9f5
keywords: ["File Open Source File", "source debugging, File Open Source File"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20File%20|%20Open%20Source%20File%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




