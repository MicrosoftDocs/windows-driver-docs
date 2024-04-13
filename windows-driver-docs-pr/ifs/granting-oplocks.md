---
title: Requesting and Granting Oplocks
description: Requesting and granting oplocks
ms.date: 07/07/2023
---

# Requesting and granting oplocks

When the network redirector accesses files on remote servers, it requests the oplock from the remote server. Client applications directly request oplocks only when the lock is intended for a file on the local server.

[Oplocks](oplock-overview.md) are requested through [FSCTLs](about-fsctls.md). The following FSCTLs are used for the different [oplock types](oplock-types.md), which both user-mode applications and kernel-mode drivers can issue:

* To request legacy oplocks:
  * [FSCTL_REQUEST_OPLOCK_LEVEL_1](fsctl-request-oplock-level-1.md)
  * [FSCTL_REQUEST_OPLOCK_LEVEL_2](fsctl-request-oplock-level-2.md)
  * [FSCTL_REQUEST_BATCH_OPLOCK](fsctl-request-batch-oplock.md)
  * [FSCTL_REQUEST_FILTER_OPLOCK](fsctl-request-filter-oplock.md)
* To request Windows 7 oplocks:
  * [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md)

To request a Windows 7 oplock in user mode, call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol):

* Set **dwIoControlCode** to [FSCTL_REQUEST_OPLOCK](fsctl-request-oplock.md).
* Specify the REQUEST_OPLOCK_INPUT_FLAG_REQUEST flag in the **Flags** member of the [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure, which is passed as the **lpInBuffer** parameter.

In a similar manner, to request Windows 7 oplocks in kernel mode:

* A non-file system minifilter can call [**ZwFsControlFile**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwfscontrolfile).
* A file system minifilter must use [**FltAllocateCallbackData**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecallbackdata) and [**FltPerformAsynchronousIo**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltperformasynchronousio).

To specify which of the four Windows 7 oplocks is required, set one or more of the following flags in the **RequestedOplockLevel** member of the [**REQUEST_OPLOCK_INPUT_BUFFER**](/windows/win32/api/winioctl/ns-winioctl-request_oplock_input_buffer) structure:

* OPLOCK_LEVEL_CACHE_READ
* OPLOCK_LEVEL_CACHE_HANDLE
* OPLOCK_LEVEL_CACHE_WRITE

For more information, see [**FSCTL_REQUEST_OPLOCK**](./fsctl-request-oplock.md).

If the requested oplock can be granted, the file system returns STATUS_PENDING. For this reason, oplocks are never granted for synchronous I/O. The FSCTL IRP doesn't complete until the oplock is broken.

If the oplock can't be granted, the file system returns an appropriate error code is returned. The most commonly returned error codes are STATUS_OPLOCK_NOT_GRANTED and STATUS_INVALID_PARAMETER (and their equivalent user-mode analogs).

The Filter oplock allows an application to "back out" when other applications/clients try to access the same stream. This mechanism allows an application to access a stream without causing other accessors of the stream to receive sharing violations when attempting to open the stream. To avoid sharing violations, a special three-step procedure should be used to request a Filter oplock (FSCTL_REQUEST_FILTER_OPLOCK):

1. Open the file with a required access of FILE_READ_ATTRIBUTES and a share mode of FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE.

2. Request a Filter oplock on the handle from step 1.

3. Open the file again for read access.

The handle opened in step 1 won't cause other applications to receive sharing violations, since it's open only for attribute access (FILE_READ_ATTRIBUTES), and not data access (FILE_READ_DATA). This handle is suitable for requesting the Filter oplock, but not for performing actual I/O on the data stream. The handle opened in step 3 allows the holder of the oplock to perform I/O on the stream; the oplock granted in step 2 allows the holder of the oplock to "get out of the way" without causing a sharing violation to another application that attempts to access the stream.

The NTFS file system provides an optimization for this procedure through the FILE_RESERVE_OPFILTER create option flag. If this flag is specified in step 1 of the previous procedure, it allows the file system to fail the create request with STATUS_OPLOCK_NOT_GRANTED if the file system can determine that step 2 will fail. If step 1 succeeds, there's no guarantee that step 2 will succeed, even if FILE_RESERVE_OPFILTER was specified for the create request.

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
<li>Prior to Windows 7, the operating system verifies if a byte range lock ever existed on the stream since the last time it was opened, and fails the request if so.</li>
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
</ul>
<p>Be aware that if the current oplock state is:</p>
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
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: the request is granted.</p></li>
<li>Read or Read-Write and the existing oplock has the same oplock key as the request: the existing oplock's IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE, the request is granted.
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
<li>If there are other open requests on the stream (even by the same thread) they must have the same oplock key.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
</ul>
<p>If the current oplock state is:</p>
<ul>
<li><p>No oplock: the request is granted.</p></li>
<li>Read, Read-Handle, Read-Write, or Read-Write-Handle and the existing oplock has the same oplock key as the request: the existing oplock's IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE, the request is granted.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li><p>Level 2, Level 1, Batch, Filter: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
</tbody>
</table>

> [!NOTE]
>
> Read and Level 2 oplocks can coexist on the same stream, and Read and Read-Handle oplocks can coexist, but Level 2 and Read-Handle oplocks cannot coexist.
