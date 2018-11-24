---
title: Using Files In A Driver
description: Using Files In A Driver
ms.assetid: 721bf336-1d1d-4677-843d-8af04c6f434d
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "reading data from files", "writing data to files", "reading metadata for file", "writing metadata for file", "driver file objects WDK kernel", "multiple file objects WDK kernel", "kernel-mode drivers WDK , files"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Files In A Driver





The Microsoft Windows executive represents files by *file objects*, which are executive objects that are managed by the object manager. (Directories are also represented by file objects.)

Kernel-mode components refer to a file by its object name, which is **\\DosDevices** concatenated to the file's full path. (On Microsoft Windows 2000 and later versions of the operating system, **\\??** is equivalent to **\\DosDevices**.) For example, the object name of the C:\\WINDOWS\\example.txt file is **\\DosDevices\\C:\\WINDOWS\\example.txt**. You use the object name to open a handle to a file. For more information about object names, see [Object Names](object-names.md).

### To use a file

1.  Open a handle to the file.

    For more information, see [Opening a Handle to a File](opening-a-handle-to-a-file.md).

2.  Perform the intended operations by calling the appropriate **Zw*Xxx*File** routines.

    For more information, see [Using a File Handle](using-a-file-handle.md).

3.  Close the handle by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

Every time that you open a handle to a file, the Windows executive creates a file object that represents the file, and it returns an open handle to that object. Therefore, multiple file objects can exist for a single file. (Because a user-mode application can copy a handle, multiple handles can also exist for the same file object.) After all the open handles to a file object are closed, the Windows executive deletes the file object.

 

 




