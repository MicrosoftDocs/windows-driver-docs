---
title: Breaking Oplocks
description: Breaking Oplocks
ms.date: 07/07/2023
---

# Breaking Oplocks

After an [oplock](oplock-overview.md) is [requested and granted](granting-oplocks.md), the owner of that oplock has access to the stream based on the type of oplock that was requested. If the operation received isn't compatible with the current oplock, the system breaks the oplock.

When an oplock is granted, the system pends the requesting IRP. When an oplock is broken, the pended oplock's request IRP is completed with STATUS_SUCCESS. For Level 1, Batch, and Filter oplocks the **IoStatus.Information** member of the IRP is set to indicate the level to which the oplock is breaking. These levels are:

* FILE_OPLOCK_BROKEN_TO_NONE - The oplock was broken and there's no current oplock on the stream. The oplock is said to have been "broken to None."

* FILE_OPLOCK_BROKEN_TO_LEVEL_2 - The current oplock (Level 1 or Batch) was converted to a Level 2 oplock. Filter oplocks never break to Level 2, they always break to None.

For Read-Handle, Read-Write, and Read-Write-Handle oplocks, the level to which the oplock is breaking is described as a combination of zero or more of the flags OPLOCK_LEVEL_CACHE_READ, OPLOCK_LEVEL_CACHE_HANDLE, or OPLOCK_LEVEL_CACHE_WRITE in the **NewOplockLevel** member of the REQUEST_OPLOCK_OUTPUT_BUFFER structure passed as the *lpOutBuffer* parameter of [DeviceIoControl](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol). In a similar manner, [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) and [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) can be used to request Windows 7 oplocks from kernel mode. For more information, see [**FSCTL_REQUEST_OPLOCK**](./fsctl-request-oplock.md).

When the system's oplock package breaks a Level 1, Batch, Filter, Read-Write, Read-Write-Handle, or, under certain circumstances a Read-Handle oplock:

* The oplock package completes the pended oplock request IRP.
* The operation that caused the oplock break is itself pended.

If the operation is issued on a synchronous handle or it's an IRP_MJ_CREATE, which is always synchronous, the I/O manager causes the operation to block, rather than return STATUS_PENDING, waiting for an acknowledgment from the owner of the oplock to tell the oplock package that they have finished their processing and it's safe for the pended operation to proceed. The purpose of this delay is to allow the owner of the oplock to put the stream back into a consistent state before the current operation proceeds. The system waits forever to receive the acknowledgment as there's no timeout. It's therefore incumbent on the owner of the oplock to acknowledge the break in a timely manner. The pended operation's IRP is set into a cancelable state. If the application or driver performing the wait terminates, the oplock package immediately completes the IRP with STATUS_CANCELLED.

An IRP_MJ_CREATE IRP may specify the FILE_COMPLETE_IF_OPLOCKED create option to avoid being blocked as part of oplock break acknowledgment. This option tells the oplock package not to block the create IRP until the oplock break acknowledgment is received. Instead, the create is allowed to proceed. If a successful create results in an oplock break, the return code is STATUS_OPLOCK_BREAK_IN_PROGRESS, rather than STATUS_SUCCESS. The FILE_COMPLETE_IF_OPLOCKED flag is typically used to avoid deadlocks. For example, if a client owns an oplock on a stream and the same client later opens the same stream, the client would block waiting for itself to acknowledge the oplock break. In this scenario, use of the FILE_COMPLETE_IF_OPLOCKED flag avoids the deadlock.

Because the NTFS file system initiates oplock breaks for Batch and Filter oplocks before checking for sharing violations, it's possible for a create that specified FILE_COMPLETE_IF_OPLOCKED to fail with STATUS_SHARING_VIOLATION but still cause a Batch or Filter oplock to break. In this case, the information member of the [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure is set to FILE_OPBATCH_BREAK_UNDERWAY to allow the caller to detect this case.

For Read-Handle and Read-Write-Handle oplocks, the oplock break is initiated after NTFS checks for and detects a sharing violation. This gives holders of these oplocks the opportunity to close their handles and get out of the way, thus allowing for the possibility of not returning the sharing violation to the user. It also avoids unconditionally breaking the oplock in cases where the handle that the oplock caches doesn't conflict with the new create.

When Level 2, Read, and, under certain circumstances Read-Handle oplocks break, the system doesn't wait for an acknowledgment. This is because there should be no cached state on the stream that needs to be restored to the file before allowing other clients access to it.

There are certain file system operations that check the current oplock state to determine if the oplock needs to be broken. The following articles list each operation and describe what triggers an oplock break, what determines the level to which the oplock breaks, and whether an acknowledgment of the break is required:

- [IRP_MJ_CREATE](irp-mj-create2.md)

- [IRP_MJ_READ](irp-mj-read2.md)

- [IRP_MJ_WRITE](irp-mj-write2.md)

- [IRP_MJ_CLEANUP](irp-mj-cleanup2.md)

- [IRP_MJ_LOCK_CONTROL](irp-mj-lock-control2.md)

- [IRP_MJ_SET_INFORMATION](irp-mj-set-information2.md)

- [IRP_MJ_FILE_SYSTEM_CONTROL](irp-mj-file-system-control2.md)

A break of a Windows 7 oplock requires an acknowledgment if the REQUEST_OPLOCK_OUTPUT_FLAG_ACK_REQUIRED flag is set in the **Flags** member of the REQUEST_OPLOCK_OUTPUT_BUFFER structure passed as the output parameter of [DeviceIoControl](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol)(*lpOutBuffer*), [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile)(*OutBuffer*) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85))(*OutBuffer*). For more information, see [**FSCTL_REQUEST_OPLOCK**](./fsctl-request-oplock.md).

The listed per-operation articles describe the details of when a break of a Read-Handle oplock results in the pending of the operation that broke the oplock. For example, the [IRP_MJ_CREATE](irp-mj-create2.md) article contains the associated Read-Handle details.
