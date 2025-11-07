---
title: Oplocks
description: Oplocks allow file server clients to increase performance and reduce network use
keywords:
- oplocks, WDK, Windows Driver Kit, Windows, driver
- opportunistic locks, file system, file server, network redirector
ms.date: 11/05/2025
ms.topic: concept-article
---

# Oplocks and network redirectors

Network redirectors use opportunistic locks (oplocks) to optimize file access performance and reduce network traffic in client-server environments.

This documentation is intended for network redirector developers, although some information applies to client application developers. For more oplock documentation related to client applications, see the Windows SDK's [Opportunistic Locks](/windows/win32/fileio/opportunistic-locks) articles.

## Oplock overview

An oplock (opportunistic lock) is a lock that a client places on a file that resides on a server. In most cases, a client requests an oplock so it can [cache data locally](/windows/win32/fileio/local-caching). Network redirectors on clients with remote servers use oplocks, as do client applications on local servers. See [Types of oplocks](oplock-types.md) for a description of the various current and legacy oplocks.

Oplocks allow file server clients (such as clients using the SMB and SMB2 protocols) to dynamically alter the buffering strategy for a given file or [stream](/windows/win32/fileio/file-streams) in a consistent manner. Use of oplocks increases performance and reduces network use. To increase the network performance for remote file operations, a client can buffer file data locally, which reduces or eliminates the need to send and receive network packets. For example:

* A client might not have to write information into a file on a remote server if the client knows that no other process is accessing the data.
* A client can buffer read-ahead data from the remote file if the client knows that no other process is writing data to the remote file.

Applications and drivers can also use oplocks to transparently access files without affecting other applications that might need to use these files.

File systems like NTFS support multiple data streams per file. The system grants oplocks on stream handles, which means that the system grants the oplock for a given open of a file stream and the operations apply to that stream. With few exceptions, operations on one stream don't affect oplocks on a different stream. For more information, see [Requesting and granting oplocks](granting-oplocks.md).

For file systems that don't support alternate data streams, such as FAT, think of "file" when oplock discussions refer to "stream."

The kernel implements the core oplock functionality of the oplock package, primarily through **FsRtl*Xxx*** routines such as [**FsRtlInitializeOplock**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-_fsrtl_advanced_fcb_header-fsrtlinitializeoplock). File systems call into this package to implement the oplock functionality in their file system. The oplock articles in this section describe how the NTFS file system interoperates with the kernel oplock package. Other file systems function in a similar manner though there might be minor differences.

## Oplock keys

You can associate the stream handle with an *oplock key*, which is a GUID value that identifies multiple handles belonging to the same client cache view. It's more accurate to say that the oplock key is associated with the [**FILE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_file_object) structure that the stream handle refers to. This distinction is important when you duplicate the handle, such as with [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle). Each of the duplicate handles refers to the same underlying **FILE_OBJECT** structure.

You can explicitly provide the oplock key (to [**IoCreateFileEx**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iocreatefileex)) when you create the stream handle. If you don't explicitly specify an oplock key at handle creation, the system treats the handle as having a unique oplock key associated with it. This unique key differs from any other key on any other handle.

An oplock breaks when all of the following conditions are true:

* A file operation is received on a handle other than the one on which the oplock was granted.
* The oplock key associated with the oplock's handle differs from the key associated with the operation's handle.
* The operation isn't compatible with the currently granted oplock.

The oplock breaks even if the same process or thread performs the incompatible operation. For example, an exclusive oplock breaks immediately when:

1. A process opens a stream for which an exclusive oplock is granted.
1. That same process opens the same stream again by using a different (or no) oplock key.

For more information, see [Breaking oplocks](breaking-oplocks.md).

Remember that oplock keys exist on handles, and you "put them on" the handle when you create it. You can associate a handle with an oplock key even if no oplocks are granted.
