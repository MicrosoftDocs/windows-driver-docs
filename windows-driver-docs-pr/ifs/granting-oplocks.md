---
title: Requesting and Granting Oplocks
description: Requesting and granting oplocks
ms.date: 02/07/2025
ms.topic: how-to
---

# Requesting and granting oplocks

When the network redirector accesses files on remote servers, it requests the oplock from the remote server. Client applications directly request oplocks only when the lock is intended for a file on the local server.

[Oplocks](oplock-overview.md) are requested through [FSCTLs](about-fsctls.md). The following FSCTLs are used for the different [oplock types](oplock-types.md), which both user-mode applications and kernel-mode drivers can issue.

* To request Windows 7 oplocks:
  * [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md)
* To request legacy oplocks:
  * [FSCTL_REQUEST_OPLOCK_LEVEL_1](fsctl-request-oplock-level-1.md)
  * [FSCTL_REQUEST_OPLOCK_LEVEL_2](fsctl-request-oplock-level-2.md)
  * [FSCTL_REQUEST_BATCH_OPLOCK](fsctl-request-batch-oplock.md)
  * [FSCTL_REQUEST_FILTER_OPLOCK](fsctl-request-filter-oplock.md)

## Requesting an oplock in user mode

To request a Windows 7 oplock in user mode, call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol):

* Set **dwIoControlCode** to [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md).
* Pass a pointer to a [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure in the **lpInBuffer** parameter.
  * Refer to that structure's documentation for information on how to format the oplock request.
* Pass a pointer to a [**REQUEST_OPLOCK_OUTPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_output_buffer) structure in the **lpOutBuffer** parameter.

For more information, see [**FSCTL_REQUEST_OPLOCK**](fsctl-request-oplock.md).

If the requested oplock can be granted, **DeviceIoControl** returns FALSE and [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR_IO_PENDING. For this reason, oplocks are never granted for synchronous I/O. The overlapped operation doesn't complete until the oplock is broken. After the operation completes, the **REQUEST_OPLOCK_OUTPUT_BUFFER** will contain information about the oplock break.

If the oplock can't be granted, the file system returns an appropriate error code. The most commonly returned error codes are ERROR_OPLOCK_NOT_GRANTED and ERROR_INVALID_PARAMETER.

## Requesting an oplock in kernel mode

To request Windows 7 oplocks in kernel mode:

### File system minifilters

A file system minifilter must use [**FltAllocateCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecallbackdata) and fill in the allocated [**FLT_CALLBACK_DATA**](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_callback_data) like so:

* Set its **[Iopb](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_io_parameter_block)->MajorFunction** field to [IRP_MJ_FILE_SYSETM_CONTROL](flt-parameters-for-irp-mj-file-system-control.md).
* Set its **Iopb->MinorFunction** field to IRP_MN_USER_FS_REQUEST.
* Set its **Iopb->[Parameters](/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_parameters).FileSystemControl.Buffered.FsControlCode** member to [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md).
* Allocate a buffer whose size is equal to the larger of [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) or [**REQUEST_OPLOCK_OUTPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_output_buffer).
  * Set the allocated **FLT_CALLBACK_DATA**'s **Iopb->Parameters.FileSystemControl.Buffered.SystemBuffer** member to point to that buffer.
  * Set the allocated **FLT_CALLBACK_DATA**'s **Iopb->Parameters.FileSystemControl.Buffered.InputBufferLength** and **Iopb->Parameters.FileSystemControl.Buffered.OutputBufferLength** fields to the size of that buffer.

Refer to the documentation of the [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure for information on how to format the oplock request.

Then the file system minifilter must call [**FltPerformAsynchronousIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltperformasynchronousio), passing the allocated **FLT_CALLBACK_DATA** as the **CallbackData** parameter.

If the requested oplock can be granted, the **FltPerformAsynchronousIo** call returns STATUS_PENDING. For this reason, oplocks are never granted for synchronous I/O. The operation doesn't complete until the oplock is broken. After the operation completes, the **REQUEST_OPLOCK_OUTPUT_BUFFER** will contain information about the oplock break.

If the oplock can't be granted, the file system returns an appropriate error code. The most commonly returned error codes are STATUS_OPLOCK_NOT_GRANTED and STATUS_INVALID_PARAMETER.

### Other Kinds of Drivers

Other kinds of drivers can call [**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile):

* Set **FsControlCode** to [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md).
* Pass a pointer to a [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure in the **InputBuffer** parameter and set the **InputBufferLength** parameter to the size of that buffer.
* Pass a pointer to a [**REQUEST_OPLOCK_OUTPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_output_buffer) structure in the **OutputBuffer** parameter and set the **OutputBufferLength** parameter to the size of that buffer.

Refer to the documentation of the [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure for information on how to format the oplock request.

If the requested oplock can be granted, the **ZwFsControlFile** call returns STATUS_PENDING. For this reason, oplocks are never granted for synchronous I/O. The operation doesn't complete until the oplock is broken. After the operation completes, the **REQUEST_OPLOCK_OUTPUT_BUFFER** will contain information about the oplock break.

If the oplock can't be granted, the file system returns an appropriate error code. The most commonly returned error codes are STATUS_OPLOCK_NOT_GRANTED and STATUS_INVALID_PARAMETER.

## Avoiding Sharing Violations When Requesting Oplocks

### Using the Atomic Create-With-Oplock Method

Atomic create-with-oplock isn't an oplock type. Rather, it's a procedure that allows open operations to avoid causing sharing-mode violations in the time span between opening a file and receiving an oplock. With legacy oplocks, Filter oplocks and opening two handles is required. With Windows 7 oplocks, an application or driver can request any type of oplock using this procedure and need open only one handle.

To perform the atomic create-with-oplock procedure, you should:

1. Use [**FltCreateFileEx2**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltcreatefileex2) or [**ZwCreateFile**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatefile), as appropriate, to open the file. In the CreateOptions parameter, pass the flag **FILE_OPEN_REQUIRING_OPLOCK**. You can set the *DesiredAccess* and *ShareAccess* parameters as desired. For example, in the *DesiredAccess* parameter set **GENERIC_READ** so you can read the file, and in the *ShareAccess* parameter set the **FILE_SHARE_READ | FILE_SHARE_DELETE** flags to allow others to read, rename, and/or mark the file for deletion while you have it open.
2. Use the [**FSCTL_REQUEST_OPLOCK**](fsctl-request-oplock.md) control code to request an oplock on the resulting file object or handle, as described in [Requesting an Oplock In Kernel Mode](#requesting-an-oplock-in-kernel-mode).

Don't perform any file system operations on the file between steps 1 and 2. Doing so can cause deadlocks.

The most common oplock to request using this procedure is the Read-Handle type. This allows you to allow other callers as much concurrent access as possible, while still allowing you to be notified if you need to close your handle to avoid causing a sharing violation to a conflicting open.

### Using the Legacy Filter Oplock

The legacy Filter oplock also allows an application to "back out" when other applications/clients try to access the same stream, but is less flexible than the atomic create-with-oplock method. This mechanism allows an application to access a stream without causing other accessors of the stream to receive sharing violations when attempting to open the stream. To avoid sharing violations, the following three-step procedure should be used to request a Filter oplock:

1. Open the file with a required access of FILE_READ_ATTRIBUTES and a share mode of FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE. The handle opened in this step won't cause other applications to receive sharing violations because it's open only for attribute access (FILE_READ_ATTRIBUTES) and not data access (FILE_READ_DATA). This handle is suitable for requesting the Filter oplock, but not for performing actual I/O on the data stream.

2. Request a Filter oplock (FSCTL_REQUEST_FILTER_OPLOCK) on the handle from step 1. The oplock granted in this step allows the oplock holder to "get out of the way" without causing a sharing violation to another application that attempts to access the stream.

3. Open the file again for read access. The handle opened in this step allows the oplock holder to perform I/O on the stream.

The NTFS file system provides an optimization for this procedure through the FILE_RESERVE_OPFILTER create option flag. If this flag is specified in step 1 of the previous procedure, it allows the file system to fail the create request with STATUS_OPLOCK_NOT_GRANTED if the file system can determine that step 2 will fail. If step 1 succeeds, there's no guarantee that step 2 will succeed, even if FILE_RESERVE_OPFILTER was specified for the create request.

## Conditions For Granting Oplocks

The following table identifies the required conditions necessary to grant an oplock.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Request type</th>
<th align="left">Conditions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Level 1</p>
<p>Filter</p>
<p>Batch</p></td>
<td align="left"><p>Granted only if all of the following conditions are true:</p>
<ul>
<li>The request is for a given stream of a file.
<ul>
<li>If a directory, STATUS_INVALID_PARAMETER is returned.</li>
</ul></li>
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned (oplocks aren't granted for synchronous I/O requests).</li>
</ul></li>
<li>There are no <a href="/windows-hardware/drivers/kernel/windows-kernel-mode-kernel-transaction-manager" data-raw-source="[TxF](../kernel/windows-kernel-mode-kernel-transaction-manager.md)">TxF</a> transactions on any stream of the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no other opens on the stream (even by the same thread).
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: The request is granted.</p></li>
<li><p>Level 2: The original Level 2 request is broken with FILE_OPLOCK_BROKEN_TO_NONE. The requested exclusive oplock is then granted.</p></li>
<li><p>Level 1, Batch, Filter, Read, Read-Handle, Read-Write, or Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>Level 2</p></td>
<td align="left"><p>Granted only if all of the following conditions are true:</p>
<ul>
<li>The request is for a given stream of a file.
<ul>
<li>If a directory, STATUS_INVALID_PARAMETER is returned.</li>
</ul></li>
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no TxF transactions on the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no current Byte Range Locks on the stream.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
<li>Before Windows 7, the operating system verifies if a byte range lock ever existed on the stream since the last time it was opened, and fails the request if so.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: The request is granted.</p></li>
<li>Level 2 and/or Read: The request is granted. You can have multiple Level 2/Read oplocks granted on the same stream at the same time. Multiple Level 2 (but not Read) oplocks can even exist on the same handle.
<ul>
<li>If a Read oplock is requested on a handle that already has a Read oplock granted to it, the first Read oplock's IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE before the second Read oplock is granted.</li>
</ul></li>
<li><p>Level 1, Batch, Filter, Read-Handle, Read-Write, Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>Read</p></td>
<td align="left"><p>Granted only if all of the following conditions are true:</p>
<ul>
<li>The request is for a given stream of a file.
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no TxF transactions on the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no current Byte Range Locks on the stream.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no writable <a href="/windows-hardware/drivers/kernel/section-objects-and-views">user-mapped sections</a> on the stream.
<ul>
<li>Else STATUS_CANNOT_GRANT_REQUESTED_OPLOCK is returned. The <b>REQUEST_OPLOCK_OUTPUT_BUFFER.Flags</b> field will have the REQUEST_OPLOCK_OUTPUT_FLAG_WRITABLE_SECTION_PRESENT flag set.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: The request is granted.</p></li>
<li>Level 2 and/or Read: The request is granted. You can have multiple Level 2/Read oplocks granted on the same stream at the same time.
<ul>
<li>Additionally, if an existing oplock has the same oplock key as the new request, its IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE.</li>
</ul></li>
<li>Read-Handle and the existing oplock have a different oplock key from the new request: The request is granted. Multiple Read and Read-Handle oplocks can coexist on the same stream (see the note following this table).
<ul>
<li>Else (oplock keys are the same) STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li><p>Level 1, Batch, Filter, Read-Write, Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>Read-Handle</p></td>
<td align="left"><p>Granted only if all of the following conditions are true:</p>
<ul>
<li>The request is for a given stream of a file.
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no TxF transactions on the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no current Byte Range Locks on the stream.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no writable <a href="/windows-hardware/drivers/kernel/section-objects-and-views">user-mapped sections</a> on the stream.
<ul>
<li>Else STATUS_CANNOT_GRANT_REQUESTED_OPLOCK is returned. The <b>REQUEST_OPLOCK_OUTPUT_BUFFER.Flags</b> field will have the REQUEST_OPLOCK_OUTPUT_FLAG_WRITABLE_SECTION_PRESENT flag set.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: the request is granted.</p></li>
<li>Read: the request is granted.
<ul>
<li>If an existing Read oplock has the same oplock key as the new request, its IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE. The result is that the oplock is upgraded from Read to Read-Handle.</li>
<li>Any existing Read oplock that doesn't have the same oplock key as the new request remains unchanged.</li>
</ul></li>
<li><p>Level 2, Level 1, Batch, Filter, Read-Write, Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>Read-Write</p></td>
<td align="left"><p>Granted only if all of the following conditions are true:</p>
<ul>
<li>The request is for a given stream of a file.
<ul>
<li>If a directory, STATUS_INVALID_PARAMETER is returned.</li>
</ul></li>
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no TxF transactions on the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>If there are other opens on the stream (even by the same thread), they must have the same oplock key.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no writable <a href="/windows-hardware/drivers/kernel/section-objects-and-views">user-mapped sections</a> on the stream.
<ul>
<li>Else STATUS_CANNOT_GRANT_REQUESTED_OPLOCK is returned. The <b>REQUEST_OPLOCK_OUTPUT_BUFFER.Flags</b> field will have the REQUEST_OPLOCK_OUTPUT_FLAG_WRITABLE_SECTION_PRESENT flag set.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: the request is granted.</p></li>
<li>Read or Read-Write and the existing oplock has the same oplock key as the request: the existing oplock's IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE and the request is granted.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li><p>Level 2, Level 1, Batch, Filter, Read-Handle, Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>Read-Write-Handle</p></td>
<td align="left"><p>Granted only if all of the following are true:</p>
<ul>
<li>The request is for a given stream of a file.
<ul>
<li>If a directory, STATUS_INVALID_PARAMETER is returned.</li>
</ul></li>
<li>The stream is opened for ASYNCHRONOUS access.
<ul>
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no TxF transactions on the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>If there are other open requests on the stream, even by the same thread, they must have the same oplock key.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no writable <a href="/windows-hardware/drivers/kernel/section-objects-and-views">user-mapped sections</a> on the stream.
<ul>
<li>Else STATUS_CANNOT_GRANT_REQUESTED_OPLOCK is returned. The <b>REQUEST_OPLOCK_OUTPUT_BUFFER.Flags</b> field will have the REQUEST_OPLOCK_OUTPUT_FLAG_WRITABLE_SECTION_PRESENT flag set.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: the request is granted.</p></li>
<li>Read, Read-Handle, Read-Write, or Read-Write-Handle and the existing oplock has the same oplock key as the request: the existing oplock's IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE and the request is granted.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li><p>Level 2, Level 1, Batch, Filter: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
> Read and Level 2 oplocks can coexist on the same stream, and Read and Read-Handle oplocks can coexist, but Level 2 and Read-Handle oplocks can't coexist.
