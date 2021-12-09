---
title: Supporting BypassIO operations
description: Learn more about supporting BypassIO operations
keywords:
- filter drivers WDK file system , BypassIO
- filter drivers WDK file system , BypassIO operations
ms.date: 12/08/2021
prerelease: false
ms.localizationpriority: medium
---

# Supporting BypassIO operations

Starting in Windows 11, all minifilters should add support for BypassIO operations. BypassIO operations are requested by calling [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with the [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) control code and request-specific information in a [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input) structure pointed to by the **InputBuffer** parameter.

This page provides details for each BypassIO operation. The operation request is specified as a [**FS_BPIO_OPERATIONS**](/windows-hardware/drivers/ddi/ntifs/ne-ntifs-fs_bpio_operations) value in the **Operation** member of [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input).

See [BypassIO for filters](bypassio.md) for more information about BypassIO and for additional implementation details.

## FS_BPIO_OP_ENABLE request

 This request can come from user or kernel mode. (BypassIO on non-cached writes is currently not supported.)

**FS_BPIO_OP_ENABLE** requests that BypassIO be enabled for the given file, which means a driver might not see all non-cached reads for that file.

BypassIO is a per file-open concept; that is, a **FS_BPIO_OP_ENABLE** request only impacts the file object associated with the enable request, and does not change the behavior of other opens on the same file or stream. If multiple enable requests to the same file object are sent, only the first request is meaningful, and all subsequent requests are ignored.

In the driver's pre-operation callback:

* If a driver can support BypassIO for the given file, it should forward the request down the stack.
* If the driver cannot support BypassIO for the given file, it should:
  * Call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to get some of the information needed to update the [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure.
  * Update the [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure, including the operation NTSTATUS describing why the enable request was vetoed, the driver's name, and a unique, descriptive string with additional details about why you vetoed the enable request.
  * Complete [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) with STATUS_SUCCESS.

During the post-operation, the driver can see whether all drivers below it are capable of supporting BypassIO. If yes, the driver should preserve any needed state for the file and continue completion processing. It is the filter's and file system's responsibility to maintain state to properly handle requests that might not be compatible with the BypassIO-enabled state.

> [!NOTE]
> All filters in the file system stack have the opportunity to veto the BypassIO enable request during pre-operation, but are encouraged to keep it enabled as much as possible.

The file system will automatically veto a BypassIO enable request for the following types of files:

* Directories (alternate data streams on a directory can use BypassIO)
* Volumes (DASD opens)
* NTFS-compressed files
* NTFS-encryted files
* Sparse files
* Paging files
* All files on DAX volumes

Most filters do not need to maintain state that BypassIO has been enabled on a specific stream. Instead, this information can be queried by calling [**FsRtlGetBypassIoOpenCount**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetbypassioopencount).

### FS_BPIO_OP_ENABLE example: encryption filter

When an encryption filter receives a **FS_BPIO_OP_ENABLE** operation on a file:

* If the file is already encrypted, the filter should call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto the BypassIO operation and return an appropriate [status and diagnostic message](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_results), such as:

  * **OpStatus** = STATUS_NOT_SUPPORTED_WITH_ENCRYPTION
  * **FailureReason** = "Encrypted file not supported"

* If the file is not currently encrypted, the filter should allow BypassIO. If a later request is made to encrypt this file, the filter can use the **FS_BPIO_OP_STREAM_PAUSE** operation to disable BypassIO.

## FS_BPIO_OP_DISABLE request

This request can come from user or kernel mode. It allows a driver to cleanup any associated BypassIO state.

If a driver has previously allowed BypassIO to be enabled on this file and now needs to turn off BypassIO support for a file, it should send the **FS_BPIO_OP_DISABLE** [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) operation to the top of the file system stack using the associated handle. An example of when this might occur is an encryption driver that has received a request to encrypt this file.  

If a driver receives **FS_BPIO_OP_DISABLE** but does not currently have BypassIO enabled, it should ignore the request. If this operation is sent on a file that currently does not have BypassIO enabled, it should be ignored.

This operation should not be failed.

## FS_BPIO_OP_QUERY request

This request can come from user or kernel mode.

A filter should process a **FS_BPIO_OP_QUERY** request similar to an **FS_BPIO_OP_ENABLE** operation, calling [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto as appropriate, and filling in the same diagnostic information in the appropriate fields in the [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure. The major difference is that the driver does not enter the BypassIO ENABLE state during a QUERY.

The **FS_BPIO_OP_QUERY** operation can be sent on directory and volume handles (an **FS_BPIO_OP_ENABLE** request cannot be sent on directory or volume handles).

### Query example: encryption filter

When an encryption filter receives a **FS_BPIO_OP_QUERY** operation on a file:

* If the file is already encrypted, the filter should call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto the BypassIO operation and return an appropriate [status and diagnostic message](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_results), such as:

  * **OpStatus** = STATUS_NOT_SUPPORTED_WITH_ENCRYPTION
  * **FailureReason** = "Encrypted file not supported"

* If the file is not currently encrypted, the filter should succeed the query request.

## FS_BPIO_OP_VOLUME_STACK_PAUSE request

This request can come from user or kernel mode.

If a volume stack driver previously allowed BypassIO to be enabled on a volume, and now needs to stop BypassIO (for example, due to some external request), the driver should send a **FS_BPIO_OP_VOLUME_STACK_PAUSE** [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) operation to the top of the volume stack to notify the file system to stop doing BypassIO on this volume's volume and storage stacks. The file system will drain all active BypassIO operations from this volume and then return. The volume stack driver can then process the external request.

All active BypassIO-enabled files will stop doing storage stack-level BypassIO operations.  This can be sent on a volume handle or any file handle for the given volume.

This operation can be sent multiple times to the same volume. It can be sent if there are no BypassIO-enabled files on the volume.

BypassIO will continue to operate on the file system stack.

This operation should not be failed.

### Volume stack pause example

*Bitlocker* is an example of a component that uses this operation when it needs to enable encryption on a volume.

Another example is the following scenario: Say that *Volsnap* allowed BypassIO to be enabled on a volume that had no active volume snapshots. Now, a request has been made to create a volume snapshot. Before proceeding, *Volsnap* does the following:

* Sends the **FS_BPIO_OP_VOLUME_STACK_PAUSE** operation to the top of the stack requesting that BypassIO be disabled on the volume stack. It does this each time a new snapshot is created. Upon successful return, BypassIO is now disabled and drained on the given volume.
* Processes the snapshot creation request

Volsnap must then veto all future **BPIO_OP_ENABLE** and **BPIO_OP_QUERY** requests on this volume.

## FS_BPIO_OP_VOLUME_STACK_RESUME request

A volume stack driver sends this FSCTL operation to the file system to resume BypassIO processing on the given volume. It sends this operation when the scenario that caused the driver to send **FS_BPIO_OP_VOLUME_STACK_PAUSE** is no longer active. This operation can be sent even if BypassIO is not currently enabled or paused.

This request can come from user or kernel mode.

This operation should not be failed.

### Volume stack resume example

Using the volume stack pause scenario described above, say the volume no longer has any active snapshots. *Volsnap* will send **FS_BPIO_OP_VOLUME_STACK_RESUME** only after the last snapshot goes away.

## FS_BPIO_OP_STREAM_PAUSE request

A filter can send an **FS_BPIO_OP_STREAM_PAUSE** operation to pause BypassIO on a stream. This request can come from user or kernel mode. All active BypassIO-enabled files will stop doing BypassIO operations.

Specifically, if a filter previously allowed BypassIO to be enabled on a stream and subsequently needs to stop BypassIO (due to an external request such as a request to encrypt a file or directory), it can send a **FS_BPIO_OP_STREAM_PAUSE** *down* the filter stack to tell the file system to stop doing BypassIO on the given stream. A filter should not send this operation to the top of the stack.

Before returning, the file system will pause all BypassIO handles open on the stream and complete all active BypassIO operations on the stream. This ensures that, on return, the filter can perform the file operation that it needs to do.

This operation can sent multiple times to the same stream. The file system will ignore this operation if it is sent on a stream that is not currently BypassIO-enabled.

If a filter does a stream pause operation, BypassIO will continue on the volume and storage stacks.

This operation should not be failed.

### Stream pause example: encryption filter

Say an encryption filter allowed BypassIO to be enabled on a stream that was not then encrypted, but has now received a request to encrypt this stream.

Before proceeding, the encryption filter should call [**FsRtlGetBypassIoOpenCount**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetbypassioopencount) to determine whether BypassIO is active on this stream. If yes, the encryption filter sends a **FS_BPIO_OP_STREAM_PAUSE** operation asking that BypassIO be disabled. Upon successful return, BypassIO is disabled and drained, so the filter can safely perform the encryption request. To eliminate possible race conditions, the filter must veto all future **FS_BPIO_OP_ENABLE** and **FS_BPIO_OP_QUERY** requests on this now encrypted stream.

## FS_BPIO_OP_STREAM_RESUME request

When the scenario that caused the filter to send a **FS_BPIO_OP_STREAM_PAUSE** operation no longer exists, the filter sends a **FS_BPIO_OP_STREAM_RESUME** operation to the file system to resume BypassIO processing of a given stream. This request can come from user or kernel mode.

If this operation is sent when BypassIO is not currently enabled or paused, it is ignored.

Pause and resume are not reference counted. Rather, on a resume, the file system issues a **FS_BPIO_OP_QUERY** request to the top of the file system stack to determine whether any remaining filters are still blocking. The file system will resume BypassIO only if all filters in the stack are not blocking BypassIO.

This operation should not be failed.

### Stream resume example: encryption filter

Using the **FS_BPIO_OP_STREAM_PAUSE** scenario described above, say the file that was previously encrypted after call to **FS_BPIO_OP_STREAM_PAUSE** is no longer encrypted. The filter should then send the **FS_BPIO_OP_STREAM_RESUME** operation to allow BypassIO to resume on that stream.

## FS_BPIO_OP_GET_INFO request

 This request can come from user or kernel mode. The file system returns information about BypassIO for the volume in a [**FS_BPIO_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_info) structure.
