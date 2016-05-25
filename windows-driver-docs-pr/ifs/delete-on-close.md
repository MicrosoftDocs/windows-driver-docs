---
title: Delete on Close
author: windows-driver-content
description: Delete on Close
ms.assetid: 340e470f-7791-4677-9369-75ed8fa9f8ad
keywords: ["security WDK file systems , semantic model checks", "semantic model checks WDK file systems , delete on close", "FILE_DELETE_ON_CLOSE", "delete on close WDK file systems"]
---

# Delete on Close


## <span id="ddk_delete_on_close_if"></span><span id="DDK_DELETE_ON_CLOSE_IF"></span>


When a caller specifies the **FILE\_DELETE\_ON\_CLOSE** option, it is necessary for the file system check to ensure that the caller has delete permission on the file or delete child permission on the parent directory. Either permission is sufficient to allow a file to be deleted. This is an important case for file systems to handle. The semantics of the operation, which delete the file when it is closed, are not enforced by the I/O manager but by the file system.

The file system may also need to check that the volume is not write protected and that this operation does not apply to a directory where this operation is not allowed. For example, the FASTFAT file system code does checks for a write-protected volume and does not allow the root directory to be deleted using FILE\_DELETE\_ON\_CLOSE. An example of these checks can be found in the **FatCommonCreate** function in the Create.c source file from the fastfat sample that the WDK contains.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Delete%20on%20Close%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


