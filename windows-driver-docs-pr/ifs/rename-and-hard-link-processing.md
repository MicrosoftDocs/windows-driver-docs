---
title: Rename and Hard Link Processing
description: Rename and Hard Link Processing
ms.assetid: 53eb3c9b-cb48-4d5f-8e26-dc93b7607813
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , rename operations
- rename operations WDK file systems
- semantic model checks WDK file systems , hard link operations
- hard link operations WDK file systems
- names WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Rename and Hard Link Processing


## <span id="ddk_rename_and_hard_link_processing_if"></span><span id="DDK_RENAME_AND_HARD_LINK_PROCESSING_IF"></span>


An area of particular concern for file systems is the proper handling of rename operations. A similar area of concern is hard link creation for file systems that support hard links. For rename operations, it is possible for a file system to delete a file (the target of the rename operation), which requires additional security checks by the file system.

When looking at the control structure for a rename operation, one of the structure fields is the **ReplaceIfExists** option:

```cpp
typedef struct _FILE_RENAME_INFORMATION {
    BOOLEAN ReplaceIfExists;
    HANDLE RootDirectory;
    ULONG FileNameLength;
    WCHAR FileName[1];
} FILE_RENAME_INFORMATION, *PFILE_RENAME_INFORMATION;
```

Similarly, in the hard link operation's control structure, one of the structure fields is the **ReplaceIfExists** option:

```cpp
typedef struct _FILE_LINK_INFORMATION {
    BOOLEAN ReplaceIfExists;
    HANDLE RootDirectory;
    ULONG FileNameLength;
    WCHAR FileName[1];
} FILE_LINK_INFORMATION, *PFILE_LINK_INFORMATION;
```

In both cases, the option is to replace the target of the operation, if it exists. While the FASTFAT file system does not support hard links, it does support rename operations. These semantics and behavior can be seen within the FASTFAT file system source code in the **FatSetRenameInfo** function (see the *Fileinfo.c* source file from the fastfat samples that the WDK contains).

The following code example to handle a rename operation mimics the file system checks for deleting the file. For a file system with a more robust security model (NTFS, for example), this check would also require security checking to ensure that the caller was allowed to delete the given file (the caller had the appropriate permissions required for deletion).

```cpp
    //
    //  The name already exists. Check if the user wants
    //  to overwrite the name and has access to do the overwrite.
    //  We cannot overwrite a directory.
    //

    if ((!ReplaceIfExists) ||
        (FlagOn(TargetDirent->Attributes, FAT_DIRENT_ATTR_DIRECTORY)) || 
        (FlagOn(TargetDirent->Attributes, FAT_DIRENT_ATTR_READ_ONLY))) {

        try_return( Status = STATUS_OBJECT_NAME_COLLISION );
    }

    //
    //  Check that the file has no open user handles; otherwise, 
    //  access will be denied. To do the check, search
    //  the list of FCBs opened under the parent Dcb, and make
    //  sure that none of the matching FCBs have a nonzero unclean count or
    //  outstanding image sections.
    //

    for (Links = TargetDcb->Specific.Dcb.ParentDcbQueue.Flink;
            Links != &TargetDcb->Specific.Dcb.ParentDcbQueue; ) {

        TempFcb = CONTAINING_RECORD( Links, FCB, ParentDcbLinks );

        //
        //  Advance now. The image section flush may cause the final
        //  close, which will recursively happen underneath of us here.
        //  It would be unfortunate if we looked through free memory.
        //

        Links = Links->Flink;

        if ((TempFcb->DirentOffsetWithinDirectory == TargetDirentOffset) &&
                ((TempFcb->UncleanCount != 0) ||
                !MmFlushImageSection( &TempFcb->NonPaged->SectionObjectPointers,
                MmFlushForDelete))) {

            //
            //  If there are batch oplocks on this file, then break the
            //  oplocks before failing the rename.
            //

            Status = STATUS_ACCESS_DENIED;

            if ((NodeType(TempFcb) == FAT_NTC_FCB) &&
                    FsRtlCurrentBatchOplock( &TempFcb->Specific.Fcb.Oplock )) {

                //
                //  Do all of the cleanup now since the IrpContext
                //  could go away when this request is posted.
                //

                FatUnpinBcb( IrpContext, TargetDirentBcb );

                Status = FsRtlCheckOplock( &TempFcb->Specific.Fcb.Oplock,
                    Irp,
                    IrpContext,
                    FatOplockComplete,
                    NULL );

                if (Status != STATUS_PENDING) {

                    Status = STATUS_ACCESS_DENIED;
                }
            }

            try_return( NOTHING );
        }
    }

    //
    //  OK, this target is finished. Remember the Lfn offset.
    //

    TargetLfnOffset = TargetDirentOffset -
        FAT_LFN_DIRENTS_NEEDED(&TargetLfn) * sizeof(DIRENT);

    DeleteTarget = TRUE;
}
```

 

 




