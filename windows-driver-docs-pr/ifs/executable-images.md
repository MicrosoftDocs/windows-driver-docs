---
title: Executable Images
description: Executable Images
ms.assetid: ca279a74-5f30-4413-bf1c-4d5af12d294d
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , executable images
- executable images WDK file systems
- memory mapped files WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Executable Images


## <span id="ddk_executable_images_if"></span><span id="DDK_EXECUTABLE_IMAGES_IF"></span>


Executable files are loaded into the address space of a process using a memory mapped image file. The file itself is not required to be opened nor does a handle need to be created because the mapping is done by means of a section. File systems must check to enforce these special semantics, assuming that they support memory mapped files. For example, the FASTFAT file system code to check for this case can be found in the **FatOpenExistingFCB** function in the Create.c source file from the fastfat samples that the WDK contains:

```cpp
    //
    //  If the user wants write access to the file, make sure there
    //  is not a process mapping this file as an image. Any attempt to
    //  delete the file will be stopped in fileinfo.c
    //
    //  If the user wants to delete on close, check at this
    //  point though.
    //

    if (FlagOn(*DesiredAccess, FILE_WRITE_DATA) || DeleteOnClose) {

        Fcb->OpenCount += 1;
        DecrementFcbOpenCount = TRUE;

        if (!MmFlushImageSection( &Fcb->NonPaged->SectionObjectPointers,
                                  MmFlushForWrite )) {

            Iosb.Status = DeleteOnClose ? STATUS_CANNOT_DELETE :STATUS_SHARING_VIOLATION;
            try_return( Iosb );
        }
    }
```

Thus, the file system ensures that a memory mapped file, including an executable image, cannot be deleted even though the file is not open.

 

 




