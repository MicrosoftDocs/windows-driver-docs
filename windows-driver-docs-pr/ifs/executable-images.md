---
title: Executable Images
author: windows-driver-content
description: Executable Images
ms.assetid: ca279a74-5f30-4413-bf1c-4d5af12d294d
keywords: ["security WDK file systems , semantic model checks", "semantic model checks WDK file systems , executable images", "executable images WDK file systems", "memory mapped files WDK file systems"]
---

# Executable Images


## <span id="ddk_executable_images_if"></span><span id="DDK_EXECUTABLE_IMAGES_IF"></span>


Executable files are loaded into the address space of a process using a memory mapped image file. The file itself is not required to be opened nor does a handle need to be created because the mapping is done by means of a section. File systems must check to enforce these special semantics, assuming that they support memory mapped files. For example, the FASTFAT file system code to check for this case can be found in the **FatOpenExistingFCB** function in the Create.c source file from the fastfat samples that the WDK contains:

```
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

        if (!MmFlushImageSection( &amp;Fcb->NonPaged->SectionObjectPointers,
                                  MmFlushForWrite )) {

            Iosb.Status = DeleteOnClose ? STATUS_CANNOT_DELETE :STATUS_SHARING_VIOLATION;
            try_return( Iosb );
        }
    }
```

Thus, the file system ensures that a memory mapped file, including an executable image, cannot be deleted even though the file is not open.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Executable%20Images%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


