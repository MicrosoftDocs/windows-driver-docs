---
title: Breaking Oplocks
description: Breaking Oplocks
ms.assetid: 1f3c4a99-5ad2-4597-a1c9-a21f80c40291
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Breaking Oplocks


## <span id="ddk_network_redirector_design_and_performance_if"></span><span id="DDK_NETWORK_REDIRECTOR_DESIGN_AND_PERFORMANCE_IF"></span>


After an oplock is granted, the owner of that oplock has access to the stream (based on the type of oplock that was requested). If the operation received is not compatible with the current oplock, the oplock is broken.

When an oplock is granted, the requesting IRP is pended. When an oplock is broken, the pended oplock request IRP is completed with STATUS\_SUCCESS. For Level 1, Batch, and Filter oplocks the **IoStatus.Information** member of the IRP is set to indicate the level to which the oplock is breaking. These levels are:

-   FILE\_OPLOCK\_BROKEN\_TO\_NONE - The oplock was broken and there is no current oplock on the stream. The oplock is said to have been "broken to None".

-   FILE\_OPLOCK\_BROKEN\_TO\_LEVEL\_2 - The current oplock (Level 1 or Batch) was converted to a Level 2 oplock. Note that Filter oplocks never break to Level 2, they always break to None.

For Read-Handle, Read-Write, and Read-Write-Handle oplocks, the level to which the oplock is breaking is described as a combination of zero or more of the flags OPLOCK\_LEVEL\_CACHE\_READ, OPLOCK\_LEVEL\_CACHE\_HANDLE, or OPLOCK\_LEVEL\_CACHE\_WRITE in the **NewOplockLevel** member of the REQUEST\_OPLOCK\_OUTPUT\_BUFFER structure passed as the *lpOutBuffer* parameter of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239). In a similar manner, [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988) and [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) can be used to request Windows 7 oplocks from kernel mode. For more information, see [**FSCTL\_REQUEST\_OPLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff545530).

When breaking a Level 1, Batch, Filter, Read-Write, Read-Write-Handle, or, under certain circumstances (see note), a Read-Handle oplock, the pended oplock request IRP is completed by the oplock package and the operation that caused the oplock break is itself pended (note that if the operation is issued on a synchronous handle, or it is an IRP\_MJ\_CREATE, which is always synchronous, the I/O manager causes the operation to block, rather than return STATUS\_PENDING), waiting for an acknowledgment from the owner of the oplock to tell the oplock package that they have finished their processing and it is safe for the pended operation to proceed. The purpose of this delay is to allow the owner of the oplock to put the stream back into a consistent state before the current operation proceeds. The system waits forever to receive the acknowledgment as there is no timeout. It is therefore incumbent on the owner of the oplock to acknowledge the break in a timely manner. The pended operation's IRP is set into a cancelable state. If the application or driver performing the wait terminates, the oploack package immediately completes the IRP with STATUS\_CANCELLED.

An IRP\_MJ\_CREATE IRP may specify the FILE\_COMPLETE\_IF\_OPLOCKED create option to avoid being blocked as part of oplock break acknowledgment. This option tells the oplock package not to block the create IRP until the oplock break acknowledgment is received. Instead, the create is allowed to proceed. If a successful create results in an oplock break, the return code is STATUS\_OPLOCK\_BREAK\_IN\_PROGRESS, rather than STATUS\_SUCCESS. The FILE\_COMPLETE\_IF\_OPLOCKED flag is typically used to avoid deadlocks. For example, if a client owns an oplock on a stream and the same client subsequently opens the same stream, the client would block waiting for itself to acknowledge the oplock break. In this scenario, use of the FILE\_COMPLETE\_IF\_OPLOCKED flag avoids the deadlock.

Because the NTFS file system initiates oplock breaks for Batch and Filter oplocks before checking for sharing violations, it is possible for a create that specified FILE\_COMPLETE\_IF\_OPLOCKED to fail with STATUS\_SHARING\_VIOLATION but still cause a Batch or Filter oplock to break. In this case, the information member of the [**IO\_STATUS\_BLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff550671) structure is set to FILE\_OPBATCH\_BREAK\_UNDERWAY to allow the caller to detect this case.

For Read-Handle and Read-Write-Handle oplocks, the oplock break is initiated after NTFS checks for and detects a sharing violation. This gives holders of these oplocks the opportunity to close their handles and get out of the way, thus allowing for the possibility of not returning the sharing violation to the user. It also avoids unconditionally breaking the oplock in cases where the handle that the oplock caches does not conflict with the new create.

When Level 2, Read, and, under certain circumstances (see note), Read-Handle oplocks break, the system does not wait for an acknowledgment. This is because there should be no cached state on the stream that needs to be restored to the file before allowing other clients access to it.

There are certain file system operations which check the current oplock state to determine if the oplock needs to be broken. The following sections list each operation and describe what triggers an oplock break, what determines the level to which the oplock breaks, and whether an acknowledgment of the break is required:

- [IRP_MJ_CREATE](irp-mj-create2.md)

- [IRP_MJ_READ](irp-mj-read2.md)

- [IRP_MJ_WRITE](irp-mj-write2.md)

- [IRP_MJ_CLEANUP](irp-mj-cleanup2.md)

- [IRP_MJ_LOCK_CONTROL](irp-mj-lock-control2.md)

- [IRP_MJ_SET_INFORMATION](irp-mj-set-information2.md)

- [IRP_MJ_FILE_SYSTEM_CONTROL](irp-mj-file-system-control2.md)

A break of a Windows 7 oplock requires an acknowledgment if the REQUEST\_OPLOCK\_OUTPUT\_FLAG\_ACK\_REQUIRED flag is set in the **Flags** member of the REQUEST\_OPLOCK\_OUTPUT\_BUFFER structure passed as the output parameter of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239)(*lpOutBuffer*), [**FltFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff542988)(*OutBuffer*) or [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462)(*OutBuffer*). For more information, see [**FSCTL\_REQUEST\_OPLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff545530).

**Note**  The above listed per-operation topics describe the details of when a break of a Read-Handle oplock results in the pending of the operation that broke the oplock. For example, the [IRP\_MJ\_CREATE](irp-mj-create2.md) topic contains the associated Read-Handle details.

 

 

 




