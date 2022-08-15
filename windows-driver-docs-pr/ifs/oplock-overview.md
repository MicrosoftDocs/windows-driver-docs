---
title: Using oplocks for network redirector performance
description: Oplocks allow file server clients to increase performance and reduce network use
ms.date: 06/30/2022
mscustom: contperf-fy22q4
---

# Using oplocks for network redirector performance

An oplock (opportunistic lock) is a lock placed by a client on a file residing on a server. In most cases, a client requests an oplock so it can cache data locally. Oplocks are used by network redirectors on clients with remote servers, as well as by client applications on local servers.

Oplocks allow file server clients (such as those using the SMB and SMB2 protocols) to dynamically alter the buffering strategy for a given file or stream in a consistent manner to increase performance and to reduce network use. To increase the network performance for remote file operations, a client can buffer file data locally, which reduces or eliminates the need to send and receive network packets. For example:

* A client might not have to write information into a file on a remote server if the client knows that no other process is accessing the data.
* A client can buffer read-ahead data from the remote file if the client knows that no other process is writing data to the remote file.

Applications and drivers can also use oplocks to transparently access files without affecting other applications that might need to use those files.

File systems like NTFS support multiple data streams per file. Oplocks are granted on stream handles, meaning that the operations apply to the given open stream of a file and, in general, operations on one stream do not affect oplocks on a different stream. There are exceptions to this, which are explicitly listed below. For file systems that do not support alternate data streams, such as FAT, think of "file" when this discussion refers to "stream".

## Types of oplocks

There are eight different types of oplocks; four oplocks types are current, the other four types are considered legacy oplocks.

The following four oplocks were implemented in Windows NT 3.1 (Level 1, Level 2, Batch) and Windows 2000 (Filter), and are considered "legacy oplocks":

* A **Level 2** (or shared) oplock indicates that there are multiple readers of a stream and no writers. This supports client read caching.

* A **Level 1** (or exclusive) oplock allows a client to open a stream for exclusive access and allows the client to perform arbitrary buffering. This supports client read caching and write caching.

* A **Batch** oplock (also exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports scenarios where the client needs to repeatedly open and close the same file, such as during batch script execution. This supports client read caching, write caching, and handle caching.

* A **Filter** oplock (also exclusive) allows applications and file system filter drivers, which open and read stream data, a way to "back out" when other applications, clients, or both try to access the same stream. This supports client read caching and write caching.

The following oplocks were added in Windows 7, and are collectively known as "Windows 7 oplocks":

* A **Read** (R) oplock (shared) indicates that there are multiple readers of a stream and no writers. This supports client read caching.

* A **Read-Handle** (RH) oplock (shared) indicates that there are multiple readers of a stream, no writers, and that a client can keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports client read caching and handle caching.

* A **Read-Write** (RW) oplock (exclusive) allows a client to open a stream for exclusive access and allows the client to perform arbitrary buffering. This supports client read caching and write caching.

* A **Read-Write-Handle** (RWH) oplock (exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports client read caching, write caching, and handle caching.

Some legacy oplocks might seem similar to Windows 7 oplocks. In particular, R seems similar to Level 2, RW seems similar to Level 1, and RWH seems similar to Batch. But they are indeed different. The Windows 7 oplocks were added to:

* Provide greater flexibility for the caller to express caching intentions.
* Allow oplock breaks and upgrades; that is, to allow modification of the oplock state from one level to a level of greater caching (for example, upgrading a Read oplock to a Read-Write oplock).

This flexibility is not achievable with the legacy oplocks. Differences between the Windows 7 oplocks and the legacy oplocks are discussed later in this documentation.

The core functionality of the oplock package is implemented in the kernel, primarily through **FsRtl*Xxx*** routines such as [**FsRtlInitializeOplock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializeoplock). File systems call into this package to implement the oplock functionality in their file system. This document describes how the NTFS file system interoperates with the kernel oplock package. Other file systems function in a similar manner though there might be minor differences.

Oplocks are granted on stream handles. This means an oplock is granted for a given open of a stream. Starting with Windows 7, the stream handle can be associated with an *oplock key*, that is, a GUID value that is used to identify multiple handles that belong to the same client cache view (see the below NOTE). The oplock key can be explicitly provided (to [**IoCreateFileEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefileex)) when the handle is created. If an oplock key is not explicitly specified when the handle is created, the system will treat the handle as having a unique oplock key associated with it, such that its key will differ from any other key on any other handle. If a file operation is received on a handle other than the one on which the oplock was granted, and the oplock key that is associated with the oplock's handle differs from the key that is associated with the operation's handle, and that operation is not compatible with the currently granted oplock, then that oplock is broken. The oplock breaks even if it is the same process or thread performing the incompatible operation. For example, if a process opens a stream for which an exclusive oplock is granted and the same process then opens the same stream again, using a different (or no) oplock key, the exclusive oplock is broken immediately.

Remember that oplock keys exist on handles, and they are "put on" the handle when the handle is created. You can associate a handle with an oplock key even if no oplocks are granted.

> [!NOTE]
>
> It is more accurate to say that the oplock key is associated with the [**FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure that the stream handle refers to. This distinction is important when the handle is duplicated, such as with [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle). Each of the duplicate handles refers to the same underlying **FILE_OBJECT** structure.
