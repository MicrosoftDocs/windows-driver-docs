---
title: Supporting BypassIO operations
description: Learn more about supporting BypassIO operations
keywords:
- filter drivers WDK file system , BypassIO
- filter drivers WDK file system , BypassIO operations
ms.date: 12/04/2023
prerelease: false
---

# Supporting BypassIO operations

Starting in Windows 11, all minifilters should add support for BypassIO operations. BypassIO operations are requested by calling [**FltFsControlFile**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltfscontrolfile) or [**ZwFsControlFile**](/previous-versions/ff566462(v=vs.85)) with:

* The [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) control code.
* The request-specific information in a [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input) structure pointed to by the **InputBuffer** parameter.
* A caller-allocated [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure pointed to by the **OutputBuffer** parameter, in which the system returns the results of the operation.

This page provides details for each BypassIO operation. The operation request is specified as a [**FS_BPIO_OPERATIONS**](/windows-hardware/drivers/ddi/ntifs/ne-ntifs-fs_bpio_operations) value in the **Operation** member of [**FS_BPIO_INPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_input).

For more information about BypassIO, see [BypassIO for filters](bypassio.md).

## FS_BPIO_OP_ENABLE request

 This request can come from user or kernel mode. BypassIO on noncached *writes* is currently not supported.

**FS_BPIO_OP_ENABLE** requests that the system enable BypassIO for the given file, which means a driver might not see all noncached reads for that file.

BypassIO is a per file-open concept; that is, a **FS_BPIO_OP_ENABLE** request only impacts the file object associated with the enable request, and doesn't change the behavior of other opens on the same file or stream. If multiple enable requests to the same file object are sent, only the first request is meaningful, and all subsequent requests are ignored.

In the driver's preoperation callback:

* If a driver can support BypassIO for the given file, it should forward the request down the stack.
* If the driver can't support BypassIO for the given file, it should call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) with the following information:

  * The driver's name, which is in the [**FLT_RELATED_OBJECTS**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_related_objects) structure that the **FltObjects** parameter points to.
  * An NTSTATUS error code that describes why you are vetoing the enable request in the **OperationStatus** parameter.
  * A unique, descriptive string with details about why you vetoed the enable request in the **FailureReason** parameter.

  **FltVetoBypassIo** writes the driver name, error code, and string describing why the minifilter vetoed the enable request in the [**FS_BPIO_OUTPUT**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_output) structure and writes an ETW event with the status, filter-provided reason, and filter's name to the event log.

The minifilter should complete [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) with STATUS_SUCCESS if **FltVetoBypassIo** succeeds; otherwise it should return the error that **FltVetoBypassIo** returned.

During the post-operation, the driver can see whether all drivers below it are capable of supporting BypassIO. If yes, the driver should preserve any needed state for the file and continue completion processing. It's the filter's and file system's responsibility to maintain state to properly handle requests that might not be compatible with the BypassIO-enabled state.

> [!NOTE]
> All filters in the file system stack have the opportunity to veto the BypassIO enable request during pre-operation, but are encouraged to keep it enabled as much as possible.

The file system automatically vetoes a BypassIO enable request for the following types of files:

* Directories (alternate data streams on a directory can use BypassIO)
* Volumes (DASD opens)
* NTFS-compressed files
* NTFS-encryted files
* Sparse files
* Paging files
* All files on DAX volumes

Most filters don't need to maintain state that BypassIO was enabled on a specific stream. Instead, this information can be queried by calling [**FsRtlGetBypassIoOpenCount**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetbypassioopencount).

### FS_BPIO_OP_ENABLE example: encryption filter

When an encryption filter receives a **FS_BPIO_OP_ENABLE** operation on a file:

* If the file is already encrypted, the filter should call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto the BypassIO operation, providing appropriate [status and a diagnostic message](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_results), such as:

  * **OpStatus** = STATUS_NOT_SUPPORTED_WITH_ENCRYPTION
  * **FailureReason** = "Encrypted file not supported"

* If the file isn't currently encrypted, the filter should allow BypassIO. If a later request is made to encrypt this file, the filter can use the **FS_BPIO_OP_STREAM_PAUSE** operation to disable BypassIO.

## FS_BPIO_OP_DISABLE request

This request can come from user or kernel mode. It allows a driver to clean up any associated BypassIO state.

If a driver previously allowed BypassIO to be enabled on this file and now needs to turn off BypassIO support for a file, it should send the **FS_BPIO_OP_DISABLE** [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) operation to the top of the file system stack using the associated handle. An example of when this condition might occur is an encryption driver that received a request to encrypt this file.  

If a driver receives **FS_BPIO_OP_DISABLE** but doesn't currently have BypassIO enabled, it should ignore the request. If this operation is sent on a file that currently doesn't have BypassIO enabled, it should be ignored.

This operation shouldn't be failed.

## FS_BPIO_OP_QUERY request

This request can come from user or kernel mode.

A filter should process a **FS_BPIO_OP_QUERY** request similar to an **FS_BPIO_OP_ENABLE** operation, calling [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto as appropriate with the same diagnostic information as previously described in the appropriate parameters. The major difference is that the driver doesn't enter the BypassIO ENABLE state during a QUERY.

The **FS_BPIO_OP_QUERY** operation can be sent on directory and volume handles (an **FS_BPIO_OP_ENABLE** request can't be sent on directory or volume handles).

### Query example: encryption filter

When an encryption filter receives a **FS_BPIO_OP_QUERY** operation on a file:

* If the file is already encrypted, the filter should call [**FltVetoBypassIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltvetobypassio) to veto the BypassIO operation, providing an appropriate [status and diagnostic message](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_results), such as:

  * **OpStatus** = STATUS_NOT_SUPPORTED_WITH_ENCRYPTION
  * **FailureReason** = "Encrypted file not supported"

* If the file isn't currently encrypted, the filter should succeed the query request.

## FS_BPIO_OP_VOLUME_STACK_PAUSE request

This request can come from user or kernel mode.

If a volume stack driver previously allowed BypassIO to be enabled on a volume, and now needs to stop BypassIO (for example, due to some external request), the driver should send a **FS_BPIO_OP_VOLUME_STACK_PAUSE** [**FSCTL_MANAGE_BYPASS_IO**](/windows-hardware/drivers/ddi/ntifs/ni-ntifs-fsctl_manage_bypass_io) operation to the top of the volume stack to notify the file system to stop doing BypassIO on this volume's volume and storage stacks. The file system drains all active BypassIO operations from this volume and then returns. The volume stack driver can then process the external request.

All active BypassIO-enabled files then stop doing storage stack-level BypassIO operations. This operation request:

* Can be sent on a volume handle or any file handle for the given volume.
* Can be sent multiple times to the same volume.
* Can be sent if there are no BypassIO-enabled files on the volume.

BypassIO continues to operate on the file system stack.

This operation shouldn't be failed.

### Volume stack pause example

*BitLocker* is an example of a component that uses this operation when it needs to enable encryption on a volume.

Another example is the following scenario: Say that *Volsnap* allowed BypassIO to be enabled on a volume that had no active volume snapshots. Later, a request was made to create a volume snapshot. *Volsnap* does the following actions before proceeding:

* Sends the **FS_BPIO_OP_VOLUME_STACK_PAUSE** operation to the top of the stack requesting that the system disable BypassIO on the volume stack. It does this each time a new snapshot is created. Upon successful return, BypassIO is now disabled and drained on the given volume.
* Processes the snapshot creation request

Volsnap must then veto all future **BPIO_OP_ENABLE** and **BPIO_OP_QUERY** requests on this volume.

## FS_BPIO_OP_VOLUME_STACK_RESUME request

A volume stack driver sends this FSCTL operation to the file system to resume BypassIO processing on the given volume. It sends this operation when the scenario that caused the driver to send **FS_BPIO_OP_VOLUME_STACK_PAUSE** is no longer active. This operation can be sent even if BypassIO isn't currently enabled or paused.

This request can come from user or kernel mode.

This operation shouldn't be failed.

### Volume stack resume example

Using the volume stack pause scenario previously described, say the volume no longer has any active snapshots. *Volsnap* will send **FS_BPIO_OP_VOLUME_STACK_RESUME** only after the last snapshot goes away.

## FS_BPIO_OP_STREAM_PAUSE request

A filter can send an **FS_BPIO_OP_STREAM_PAUSE** operation to pause BypassIO on a stream. This request can come from user or kernel mode. All active BypassIO-enabled files stop doing BypassIO operations.

Specifically, if a filter previously allowed BypassIO to be enabled on a stream and later needs to stop BypassIO (due to an external request such as a request to encrypt a file or directory), it can send a **FS_BPIO_OP_STREAM_PAUSE** *down* the filter stack to tell the file system to stop doing BypassIO on the given stream. A filter shouldn't send this operation to the top of the stack.

Before the file system returns, it pauses all BypassIO handles open on the stream and completes all active BypassIO operations on the stream. These actions ensure that, on return, the filter can perform the file operation that it needs to do.

This operation can be sent multiple times to the same stream. The file system ignores it if it's sent on a stream that isn't currently BypassIO-enabled.

If a filter does a stream pause operation, BypassIO continues on the volume and storage stacks.

This operation shouldn't be failed.

### Stream pause example: encryption filter

Say an encryption filter allowed BypassIO to be enabled on a stream that wasn't then encrypted, but later received a request to encrypt this stream.

Before the encryption filter proceeds, it should call [**FsRtlGetBypassIoOpenCount**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-fsrtlgetbypassioopencount) to determine whether BypassIO is active on this stream. If yes, the encryption filter sends a **FS_BPIO_OP_STREAM_PAUSE** operation asking that the system disable BypassIO. Upon successful return, BypassIO is disabled and drained, so the filter can safely perform the encryption request. To eliminate possible race conditions, the filter must veto all future **FS_BPIO_OP_ENABLE** and **FS_BPIO_OP_QUERY** requests on this now encrypted stream.

## FS_BPIO_OP_STREAM_RESUME request

When the scenario that caused the filter to send a **FS_BPIO_OP_STREAM_PAUSE** operation no longer exists, the filter sends a **FS_BPIO_OP_STREAM_RESUME** operation to the file system to resume BypassIO processing of a given stream. This request can come from user or kernel mode.

If this operation is sent when BypassIO isn't currently enabled or paused, it's ignored.

Pause and resume aren't reference counted. Rather, on a resume, the file system issues a **FS_BPIO_OP_QUERY** request to the top of the file system stack to determine whether any remaining filters are still blocking. The file system resumes BypassIO only if all filters in the stack aren't blocking BypassIO.

This operation shouldn't be failed.

### Stream resume example: encryption filter

Using the **FS_BPIO_OP_STREAM_PAUSE** scenario previously described, say the file that was previously encrypted after call to **FS_BPIO_OP_STREAM_PAUSE** is no longer encrypted. The filter should then send the **FS_BPIO_OP_STREAM_RESUME** operation to allow BypassIO to resume on that stream.

## FS_BPIO_OP_GET_INFO request

 This request can come from user or kernel mode. The file system returns information about BypassIO for the volume in a [**FS_BPIO_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-fs_bpio_info) structure.
