---
title: Neither I/O Operations
description: Neither I/O Operations
ms.assetid: c8fc4742-e220-45c4-9113-ec5658bc09cc
keywords:
- security WDK file systems , semantic model checks
- semantic model checks WDK file systems , neither I/O operations
- I/O WDK file systems
- neither I/O operations WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Neither I/O Operations


## <span id="ddk_neither_i_o_operations_if"></span><span id="DDK_NEITHER_I_O_OPERATIONS_IF"></span>


A file system must handle operations that typically involve directly manipulating user buffers. Such operations are inherently risky because the user address might not be valid. File systems must be particularly conscious of such operations and ensure that they protect them appropriately. The following operations rely upon the **Flags** member of the file system's device object to specify how the I/O manager is to transfer data between user and kernel address space:

-   [**IRP\_MJ\_DIRECTORY\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548658)

-   [**IRP\_MJ\_QUERY\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549279)

-   [**IRP\_MJ\_QUERY\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549293)

-   [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff549327)

-   [**IRP\_MJ\_SET\_EA**](https://msdn.microsoft.com/library/windows/hardware/ff549346)

-   [**IRP\_MJ\_SET\_QUOTA**](https://msdn.microsoft.com/library/windows/hardware/ff549401)

-   [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff549427)

Typically, a file system chooses neither I/O implicitly by setting neither DO\_DIRECT\_IO nor DO\_BUFFERED\_IO in the **Flags** member of the volume device object that it creates.

The following operation ignores the **Flags** member of the file system's device object and uses neither I/O to transfer data between user and kernel address space:

-   [**IRP\_MJ\_QUERY\_SECURITY**](https://msdn.microsoft.com/library/windows/hardware/ff549298)

Using neither I/O, the file system is responsible for handling its own data transfer operations. This allows a file system to satisfy an operation by directly placing the data into the user-space buffer of an application. The file system must thus ensure that the user's buffer is valid when the operation begins and gracefully handle the buffer becoming invalid while the operation is ongoing. Fast I/O also passes raw pointers. Developers should be aware that checking the validity of the buffer at the beginning of the operation is not sufficient to ensure that it remains valid throughout the operation. For example, a malicious application could map a block of memory (through a section, for example), issue an I/O operation, and unmap the block of memory while the I/O operation is ongoing.

There are several ways for a file system to handle this situation. One mechanism is to lock down the physical memory that corresponds to the user's address and create a second mapping in the operating system's address space. This ensures that the file system uses a virtual address that it controls. So even if the user address becomes invalid, the address created by the file system will remain valid. The FASTFAT file system code uses two different functions to achieve this. The first function locks down the user's buffer:

```cpp
VOID
FatLockUserBuffer (
    IN PIRP_CONTEXT IrpContext,
    IN OUT PIRP Irp,
    IN LOCK_OPERATION Operation,
    IN ULONG BufferLength
    )

/*++
Routine Description:

    This routine locks the specified buffer for the specified type of
    access. The file system requires this routine because it does not
    ask the I/O system to lock its buffers for direct I/O. This routine
    can only be called from the file system driver (FSD) while still in the user context.

    Note that this is the *input/output* buffer.

Arguments:
    Irp - Pointer to the Irp for which the buffer will be locked.
    Operation - IoWriteAccess for read operations, or IoReadAccess for
                write operations.
    BufferLength - Length of user buffer.

Return Value:
    None
--*/

{
    PMDL Mdl = NULL;

    if (Irp->MdlAddress == NULL) {
        //
        // Allocate the Mdl and Raise if the allocation fails.
        //
        Mdl = IoAllocateMdl( Irp->UserBuffer, BufferLength, FALSE, FALSE, Irp );
        if (Mdl == NULL) {
            FatRaiseStatus( IrpContext, STATUS_INSUFFICIENT_RESOURCES );
        }

        //
        // now probe the buffer described by the Irp. If there is an exception,
        // deallocate the Mdl and return the appropriate "expected" status.
        //
        try {
            MmProbeAndLockPages( Mdl,
                                 Irp->RequestorMode,
                                 Operation );
        } except(EXCEPTION_EXECUTE_HANDLER) {
            NTSTATUS Status;
            Status = GetExceptionCode();
            IoFreeMdl( Mdl );
            Irp->MdlAddress = NULL;
            FatRaiseStatus( IrpContext,
                            FsRtlIsNtstatusExpected(Status) ? Status : STATUS_INVALID_USER_BUFFER );
        }
    }

    UNREFERENCED_PARAMETER( IrpContext );
}
```

This routine ensures that the physical memory that backs a user's address will not be reused for any other purpose while the operation is ongoing. A file system might do this in order to send the I/O operation to the underlying volume management or disk class layer to satisfy a non-cached user I/O. In such a case, the file system does not need its own virtual address to the buffer. A second function creates the file system's mapping into the kernel address space:

```cpp
PVOID
FatMapUserBuffer (
    IN PIRP_CONTEXT IrpContext,
    IN OUT PIRP Irp
    )
/*++
Routine Description:
    This routine conditionally maps the user buffer for the current I/O
    request in the specified mode. If the buffer is already mapped, it
    just returns its address.
 
    Note that this is the *input/output* buffer.

Arguments:
    Irp - Pointer to the Irp for the request.

Return Value:
    Mapped address
--*/
{
    UNREFERENCED_PARAMETER( IrpContext );

    //
    // If there is no Mdl, then we must be in  the FSD, and can simply
    // return the UserBuffer field from the Irp.
    //
    if (Irp->MdlAddress == NULL) {
        return Irp->UserBuffer;
    } else {
        PVOID Address = MmGetSystemAddressForMdlSafe( Irp->MdlAddress, NormalPagePriority );
        if (Address == NULL) {
            ExRaiseStatus( STATUS_INSUFFICIENT_RESOURCES );
        }
        return Address;
    }
}
```

The FASTFAT implementation allows the second routine to return the user-level address as well, which requires that the FAT file system ensure that the address returned (user or kernel) must be valid. It does this by using the \_\_try and \_\_except keywords to create a protected block.

These routines are in the deviosup.c source file from the fastfat samples that the WDK contains.

Another critical issue occurs when the request is not satisfied in the context of the caller. If a file system posts the request to a worker thread, the driver must lock down the buffer with an MDL to not lose track of it. The **FatPrePostIrp** function in the workque.c source file from the fastfat samples provides an example of how this issue is handled by the FASTFAT file system.

The FASTFAT file system protects against a broad range of failures, not simply invalid user buffers, by using these routines. While this is a very powerful technique, it also involves ensuring that all protected code blocks properly release any resources they might be holding. The resources to release include memory, synchronization objects, or some other resource of the file system itself. A failure to do so would give a would-be attacker the ability to cause resource starvation by making many repetitive calls into the operating system to exhaust the resource.

 

 




