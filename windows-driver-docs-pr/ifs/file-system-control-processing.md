---
title: File System Control Processing
description: File System Control Processing
ms.assetid: 95a610c8-b48c-4fff-bf1f-f9fb6abb0fd9
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , control processing
- FILE_SPECIAL_ACCESS
- FSCTL_MOVE_FILE
- control processing WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Control Processing


## <span id="ddk_file_system_control_processing_if"></span><span id="DDK_FILE_SYSTEM_CONTROL_PROCESSING_IF"></span>


Handling the [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670) operation is different from the data buffer handling required by other operations within the file system. This is because each operation establishes its specific data transfer mechanism for the I/O manager as part of its control code by means of the CTL\_CODE macro. In addition, the control code specifies the file access that is required by the caller. A file system should be particularly cognizant of this issue when defining the control code, because this access is enforced by the I/O manager. Some I/O control codes (FSCTL\_MOVE\_FILE , for example) specify FILE\_SPECIAL\_ACCESS, which is a mechanism for allowing the file system to indicate that the operation's security will be checked by the file system directly. FILE\_SPECIAL\_ACCESS is numerically equivalent to FILE\_ANY\_ACCESS, so the I/O manager does not provide any specific security checks, deferring instead to the file system. FILE\_SPECIAL\_ACCESS mainly provides documentation that additional checks will be made by the file system.

Several file system operations specify FILE\_SPECIAL\_ACCESS. The FSCTL\_MOVE\_FILE operation is used as part of the defragmentation interface for file systems and it specifies FILE\_SPECIAL\_ACCESS. Since you want to be able to defragment open files that are actively being read and written, the handle to be used has only FILE\_READ\_ATTRIBUTES granted access to avoid share access conflicts. However, this operation needs to be a privileged operation as the disk is being modified on a low level. The solution is to verify that the handle used to issue the FSCTL\_MOVE\_FILE is a direct-access storage device (DASD) user volume open, which is a privileged handle. The FASTFAT file system code that ensures this operation is being done against a user volume open is in the **FatMoveFile** function (see the fsctrl.c source file from the fastfat sample that the WDK contains):

```cpp
    //
    //  extract and decode the file object and check for type of open
    //

    if (FatDecodeFileObject( IrpSp->FileObject, &Vcb, &FcbOrDcb, &Ccb ) != UserVolumeOpen) {

        FatCompleteRequest( IrpContext, Irp, STATUS_INVALID_PARAMETER );

        DebugTrace(-1, Dbg, "FatMoveFile -> %08lx\n", STATUS_INVALID_PARAMETER);
        return STATUS_INVALID_PARAMETER;
    }
```

The structure used by the FSCTL\_MOVE\_FILE operation specifies the file being moved:

```cpp
typedef struct {
    HANDLE FileHandle;
    LARGE_INTEGER StartingVcn;
    LARGE_INTEGER StartingLcn;
    ULONG ClusterCount;
} MOVE_FILE_DATA, *PMOVE_FILE_DATA;
```

As previously noted, the handle used to issue the FSCTL\_MOVE\_FILE is an "open" operation of the entire volume, while the operation actually applies to the file handle specified in the MOVE\_FILE\_DATA input buffer. This makes the security checks for this operation somewhat complex. For example, this interface must convert the file handle to a file object that represents the file being moved. This requires careful consideration on the part of any driver. FASTFAT does this using [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) in a guarded fashion in the **FatMoveFile** function in the fsctrl.c source file in the fastfat sample that the WDK contains:

```cpp
    //
    //  Try to get a pointer to the file object from the handle passed in.
    //

    Status = ObReferenceObjectByHandle( InputBuffer->FileHandle,
                                        0,
                                        *IoFileObjectType,
                                        Irp->RequestorMode,
                                        &FileObject,
                                        NULL );

    if (!NT_SUCCESS(Status)) {

        FatCompleteRequest( IrpContext, Irp, Status );

        DebugTrace(-1, Dbg, "FatMoveFile -> %08lx\n", Status);
        return Status;
    }
    //  Complete the following steps to ensure that this is not an invalid attempt
    //
    //    - check that the file object is opened on the same volume as the
    //      DASD handle used to call this routine.
    //
    //    - extract and decode the file object and check for type of open.
    //
    //    - if this is a directory, verify that it&#39;s not the root and that
    //      you are not trying to move the first cluster.  You cannot move the
    //      first cluster because sub-directories have this cluster number
    //      in them and there is no safe way to simultaneously update them
    //      all.
    //
    //  Allow movefile on the root directory if it&#39;s FAT32, since the root dir
    //  is a real chained file.
    //    //
```

Note the use of Irp-&gt;RequestorMode to ensure that if the caller is a user-mode application, the handle cannot be a kernel handle. The required access is 0 so that a file can be moved while it is being actively accessed. And finally note that this call must be made in the correct process context if the call originated in user mode. The source code from the FASTFAT file system enforces this as well in the **FatMoveFile** function in fsctrl.c:

```cpp
    //
    //  Force WAIT to true. There is a handle in the input buffer that can only
    //  be referenced within the originating process.
    //

    SetFlag( IrpContext->Flags, IRP_CONTEXT_FLAG_WAIT );
```

These semantic security checks performed by the FAT file system are typical of those required by a file system for any operation that passes a handle. In addition, the FAT file system must also perform sanity checks specific to the operation. These sanity checks are to ensure that the disparate parameters are compatible (the file being moved is on the volume that was opened, for example) in order to prevent the caller from performing a privileged operation when it should not be allowed.

For any file system, correct security is an essential part of file system control operations, which include:

-   Validating user handles appropriately.

-   Protecting user buffer access.

-   Validating semantics of the specific operation.

In many cases, the code necessary to perform proper validation and security can constitute a substantial portion of the code within the given function.

 

 




