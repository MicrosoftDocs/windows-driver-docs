---
title: Using Files In A Driver
author: windows-driver-content
description: Using Files In A Driver
ms.assetid: 721bf336-1d1d-4677-843d-8af04c6f434d
keywords: ["files WDK kernel", "file objects WDK kernel", "objects WDK file objects", "file handles WDK kernel", "handle to file WDK kernel", "reading data from files", "writing data to files", "reading metadata for file", "writing metadata for file", "driver file objects WDK kernel", "multiple file objects WDK kernel", "kernel-mode drivers WDK , files"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Files In A Driver


## <a href="" id="ddk-using-files-in-a-driver-kg"></a>


The Microsoft Windows executive represents files by *file objects*, which are executive objects that are managed by the object manager. (Directories are also represented by file objects.)

Kernel-mode components refer to a file by its object name, which is **\\DosDevices** concatenated to the file's full path. (On Microsoft Windows 2000 and later versions of the operating system, **\\??** is equivalent to **\\DosDevices**.) For example, the object name of the C:\\WINDOWS\\example.txt file is **\\DosDevices\\C:\\WINDOWS\\example.txt**. You use the object name to open a handle to a file. For more information about object names, see [Object Names](object-names.md).

### To use a file

1.  Open a handle to the file.

    For more information, see [Opening a Handle to a File](opening-a-handle-to-a-file.md).

2.  Perform the intended operations by calling the appropriate **Zw*Xxx*File** routines.

    For more information, see [Using a File Handle](using-a-file-handle.md).

3.  Close the handle by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417).

Every time that you open a handle to a file, the Windows executive creates a file object that represents the file, and it returns an open handle to that object. Therefore, multiple file objects can exist for a single file. (Because a user-mode application can copy a handle, multiple handles can also exist for the same file object.) After all the open handles to a file object are closed, the Windows executive deletes the file object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Files%20In%20A%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


