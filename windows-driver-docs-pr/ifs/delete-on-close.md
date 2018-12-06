---
title: Delete on Close
description: Delete on Close
ms.assetid: 340e470f-7791-4677-9369-75ed8fa9f8ad
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , delete on close
- FILE_DELETE_ON_CLOSE
- delete on close WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Delete on Close


## <span id="ddk_delete_on_close_if"></span><span id="DDK_DELETE_ON_CLOSE_IF"></span>


When a caller specifies the **FILE\_DELETE\_ON\_CLOSE** option, it is necessary for the file system check to ensure that the caller has delete permission on the file or delete child permission on the parent directory. Either permission is sufficient to allow a file to be deleted. This is an important case for file systems to handle. The semantics of the operation, which delete the file when it is closed, are not enforced by the I/O manager but by the file system.

The file system may also need to check that the volume is not write protected and that this operation does not apply to a directory where this operation is not allowed. For example, the FASTFAT file system code does checks for a write-protected volume and does not allow the root directory to be deleted using FILE\_DELETE\_ON\_CLOSE. An example of these checks can be found in the **FatCommonCreate** function in the Create.c source file from the fastfat sample that the WDK contains.

 

 




