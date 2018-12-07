---
title: Granting Oplocks
description: Granting Oplocks
ms.assetid: 7faf17ef-1596-4952-9575-616f66b37ed6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Granting Oplocks


## <span id="ddk_network_redirector_design_and_performance_if"></span><span id="DDK_NETWORK_REDIRECTOR_DESIGN_AND_PERFORMANCE_IF"></span>


Oplocks are requested through [FSCTL](http://go.microsoft.com/fwlink/p/?linkid=124238)s. The following list shows the FSCTLs for the different oplock types (which user-mode applications and kernel-mode drivers can issue):

-   FSCTL\_REQUEST\_OPLOCK\_LEVEL\_1

-   FSCTL\_REQUEST\_OPLOCK\_LEVEL\_2

-   FSCTL\_REQUEST\_BATCH\_OPLOCK

-   FSCTL\_REQUEST\_FILTER\_OPLOCK

-   FSCTL\_REQUEST\_OPLOCK

The first four FSCTLs in the list are used to request legacy oplocks. The last FSCTL is used to request Windows 7 oplocks with the REQUEST\_OPLOCK\_INPUT\_FLAG\_REQUEST flag specified in the **Flags** member of the REQUEST\_OPLOCK\_INPUT\_BUFFER structure, passed as the *lpInBuffer* parameter of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239). In a similar manner, [**ZwFsControlFile**](https://msdn.microsoft.com/library/windows/hardware/ff566462) can be used to request Windows 7 oplocks from kernel mode. A file system minifilter must use [**FltAllocateCallbackData**](https://msdn.microsoft.com/library/windows/hardware/ff541703) and [**FltPerformAsynchronousIo**](https://msdn.microsoft.com/library/windows/hardware/ff543420) to request a Windows 7 oplock. To specify which of the four Windows 7 oplocks is required, one or more of the flags OPLOCK\_LEVEL\_CACHE\_READ, OPLOCK\_LEVEL\_CACHE\_HANDLE, or OPLOCK\_LEVEL\_CACHE\_WRITE is set in the **RequestedOplockLevel** member of the REQUEST\_OPLOCK\_INPUT\_BUFFER structure. For more information, see [**FSCTL\_REQUEST\_OPLOCK**](https://msdn.microsoft.com/library/windows/hardware/ff545530).

When a request is made for an oplock and the oplock can be granted, the file system returns STATUS\_PENDING (because of this, oplocks are never granted for synchronous I/O). The FSCTL IRP does not complete until the oplock is broken. If the oplock cannot be granted, an appropriate error code is returned. The most commonly returned error codes are STATUS\_OPLOCK\_NOT\_GRANTED and STATUS\_INVALID\_PARAMETER (and their equivalent user-mode analogs).

As mentioned previously, the Filter oplock allows an application to "back out" when other applications/clients try to access the same stream. This mechanism allows an application to access a stream without causing other accessors of the stream to receive sharing violations when attempting to open the stream. To avoid sharing violations, a special three-step procedure should be used to request a Filter oplock (FSCTL\_REQUEST\_FILTER\_OPLOCK):

1.  Open the file with a required access of FILE\_READ\_ATTRIBUTES and a share mode of FILE\_SHARE\_READ | FILE\_SHARE\_WRITE | FILE\_SHARE\_DELETE.

2.  Request a Filter oplock on the handle from step 1.

3.  Open the file again for read access.

The handle opened in step 1 will not cause other applications to receive sharing violations, since it is open only for attribute access (FILE\_READ\_ATTRIBUTES), and not data access (FILE\_READ\_DATA). This handle is suitable for requesting the Filter oplock, but not for performing actual I/O on the data stream. The handle opened in step 3 allows the holder of the oplock to perform I/O on the stream, while the oplock granted in step 2 allows the holder of the oplock to "get out of the way" without causing a sharing violation to another application that attempts to access the stream.

The NTFS file system provides an optimization for this procedure through the FILE\_RESERVE\_OPFILTER create option flag. If this flag is specified in step 1 of the previous procedure, it allows the file system to fail the create request with STATUS\_OPLOCK\_NOT\_GRANTED if the file system can determine that step 2 will fail. Be aware that if step 1 succeeds, there is no guarantee that step 2 will succeed, even if FILE\_RESERVE\_OPFILTER was specified for the create request.

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
<li>If opened for SYNCHRONOUS access, STATUS_OPLOCK_NOT_GRANTED is returned (oplocks are not granted for synchronous I/O requests).</li>
</ul></li>
<li>There are no <a href="https://msdn.microsoft.com/library/windows/hardware/ff565748" data-raw-source="[TxF](https://msdn.microsoft.com/library/windows/hardware/ff565748)">TxF</a> transactions on any stream of the file.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li>There are no other opens on the stream (even by the same thread).
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
</ul>
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: The request is granted.</p></li>
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
<li>Be aware that prior to Windows 7, the operating system verifies if a byte range lock ever existed on the stream since the last time it was opened, and fails the request if so.</li>
</ul></li>
</ul>
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: The request is granted.</p></li>
<li>Level 2 and/or Read: The request is granted. You can have multiple Level 2/Read oplocks granted on the same stream at the same time. Multiple Level 2 (but not Read) oplocks can even exist on the same handle.
<ul>
<li>If a Read oplock is requested on a handle that already has a Read oplock granted to it, the first Read oplock&#39;s IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE before the second Read oplock is granted.</li>
</ul></li>
<li><p>Level 1, Batch, Filter, Read-Handle, Read-Write, Read-Write-Handle: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td align="left"><p>Read</p></td>
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
</ul></li>
</ul>
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: The request is granted.</p></li>
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
</ul></li>
</ul>
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: the request is granted.</p></li>
<li>Read: the request is granted.
<ul>
<li>If an existing Read oplock has the same oplock key as the new request, its IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE. This means that the oplock is upgraded from Read to Read-Handle.</li>
<li>Any existing Read oplock that does not have the same oplock key as the new request remains unchanged.</li>
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
<li>If there are other opens on the stream (even by the same thread) they must have the same oplock key.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
</ul>
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: the request is granted.</p></li>
<li>Read or Read-Write and the existing oplock has the same oplock key as the request: the existing oplock&#39;s IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE, the request is granted.
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
<p>Be aware that if the current oplock state is:</p>
<ul>
<li><p>No Oplock: the request is granted.</p></li>
<li>Read, Read-Handle, Read-Write, or Read-Write-Handle and the existing oplock has the same oplock key as the request: the existing oplock&#39;s IRP is completed with STATUS_OPLOCK_SWITCHED_TO_NEW_HANDLE, the request is granted.
<ul>
<li>Else STATUS_OPLOCK_NOT_GRANTED is returned.</li>
</ul></li>
<li><p>Level 2, Level 1, Batch, Filter: STATUS_OPLOCK_NOT_GRANTED is returned.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

**Note**   Read and Level 2 oplocks may coexist on the same stream, and Read and Read-Handle oplocks may coexist, but Level 2 and Read-Handle oplocks may not coexist.

 

 

 




