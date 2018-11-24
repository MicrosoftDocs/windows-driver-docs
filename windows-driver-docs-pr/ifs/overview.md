---
title: Overview
description: Overview
ms.assetid: 3b2895a2-9a2e-46eb-b8fb-47d6db4a1de0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview


## <span id="ddk_network_redirector_design_and_performance_if"></span><span id="DDK_NETWORK_REDIRECTOR_DESIGN_AND_PERFORMANCE_IF"></span>


Opportunistic locks, or oplocks, provide a mechanism that allows file server clients (such as those utilizing the SMB and SMB2 protocols) to dynamically alter buffering strategy for a given file or stream in a consistent manner to increase performance and to reduce network use. To increase the network performance for remote file operations, a client can locally buffer file data, which reduces or eliminates the need to send and receive network packets. For example, a client may not have to write information into a file on a remote server if the client knows that no other process is accessing the data. Likewise, the client may buffer read-ahead data from the remote file if the client knows that no other process is writing data to the remote file. Applications and drivers can also use oplocks to transparently access files without affecting other applications that might need to use those files.

File systems like NTFS support multiple data streams per file. Oplocks are granted on stream handles, meaning that the operations apply to the given open stream of a file and, in general, operations on one stream do not affect oplocks on a different stream. There are exceptions to this, which are explicitly listed below. For file systems that do not support alternate data streams, such as FAT, think of "file" when this document refers to "stream".

There are currently eight different types of oplocks:

-   A **Level 2** (or shared) oplock indicates that there are multiple readers of a stream and no writers. This supports client read caching.

-   A **Level 1** (or exclusive) oplock allows a client to open a stream for exclusive access and allows the client to perform arbitrary buffering. This supports client read caching and write caching.

-   A **Batch** oplock (also exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports scenarios where the client needs to repeatedly open and close the same file, such as during batch script execution. This supports client read caching, write caching, and handle caching.

-   A **Filter** oplock (also exclusive) allows applications and file system filters (including minifilters), which open and read stream data, a way to "back out" when other applications, clients, or both try to access the same stream. This supports client read caching and write caching.

-   A **Read** (R) oplock (shared) indicates that there are multiple readers of a stream and no writers. This supports client read caching.

-   A **Read-Handle** (RH) oplock (shared) indicates that there are multiple readers of a stream, no writers, and that a client can keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports client read caching and handle caching.

-   A **Read-Write** (RW) oplock (exclusive) allows a client to open a stream for exclusive access and allows the client to perform arbitrary buffering. This supports client read caching and write caching.

-   A **Read-Write-Handle** (RWH) oplock (exclusive) allows a client to keep a stream open on the server even though the local accessor on the client machine has closed the stream. This supports client read caching, write caching, and handle caching.

Level 1, Level 2, and Batch oplocks were implemented in Windows NT 3.1. The Filter oplock was added in Windows 2000. R, RH, RW, and RWH oplocks have been added in Windows 7.

Some oplocks seem quite similar. In particular, R seems similar to Level 2, RW seems similar to Level 1, and RWH seems similar to Batch. The R, RH, RW, and RWH oplocks (hereinafter referred to collectively as "Windows 7 oplocks") have been added to Windows 7 to provide greater flexibility for the caller to express caching intentions, and to allow oplock breaks and upgrades (that is, modification of the oplock state from one level to a level of greater caching; for example, upgrading a Read oplock to a Read-Write oplock). This flexibility is not achievable with the Level 2, Level 1, Batch, and Filter oplocks (hereinafter referred to collectively as "legacy oplocks"). Differences between the Windows 7 oplocks and the legacy oplocks are discussed later in this documentation.

The core functionality of the oplock package is implemented in the kernel (primarily through *FsRtlXxx* routines). File systems call into this package to implement the oplock functionality in their file system. This document describes how the NTFS file system interoperates with the kernel oplock package. Other file systems function in a similar manner though there might be minor differences.

Oplocks are granted on stream handles. This means an oplock is granted for a given open of a stream. Starting with Windows 7, the stream handle can be associated with an *oplock key*, that is, a GUID value that is used to identify multiple handles that belong to the same client cache view (see the note later in this topic). The oplock key can be explicitly provided (to [**IoCreateFileEx**](https://msdn.microsoft.com/library/windows/hardware/ff548283)) when the handle is created. If an oplock key is not explicitly specified when the handle is created, the system will treat the handle as having a unique oplock key associated with it, such that its key will differ from any other key on any other handle. If a file operation is received on a handle other than the one on which the oplock was granted, and the oplock key that is associated with the oplock's handle differs from the key that is associated with the operation's handle, and that operation is not compatible with the currently granted oplock, then that oplock is broken. The oplock breaks even if it is the same process or thread performing the incompatible operation. For example, if a process opens a stream for which an exclusive oplock is granted and the same process then opens the same stream again, using a different (or no) oplock key, the exclusive oplock is broken immediately.

Remember that oplock keys exist on handles, and they are "put on" the handle when the handle is created. You can associate a handle with an oplock key even if no oplocks are granted.

**Note**  It is more accurate to say that the oplock key is associated with the [**FILE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff545834) structure that the stream handle refers to. This distinction is important when the handle is duplicated, such as with [DuplicateHandle](http://go.microsoft.com/fwlink/p/?linkid=124237). Each of the duplicate handles refers to the same underlying **FILE\_OBJECT** structure.

 

 

 




