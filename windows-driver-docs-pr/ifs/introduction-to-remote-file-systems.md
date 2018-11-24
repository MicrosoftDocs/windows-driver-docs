---
title: Introduction to Remote File Systems
description: Introduction to Remote File Systems
ms.assetid: 24fe7b8e-b956-4c27-be12-8317e4f35ba6
keywords:
- network redirectors WDK , remote file systems
- redirector drivers WDK , remote file systems
- remote file systems WDK
- file system drivers WDK , remote file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Remote File Systems


## <span id="ddk_introduction_to_remote_file_systems_if"></span><span id="DDK_INTRODUCTION_TO_REMOTE_FILE_SYSTEMS_IF"></span>


Remote file systems enable an application that runs on a client computer to access files stored on a different computer. Remote file systems also often make other resources (remote printers, for example) accessible from a client computer. The remote file and resource access takes place using some form of local area network (LAN), wide area network (WAN), point-to-point link, or other communication mechanism. These file systems are often referred as network file systems or distributed file systems.

Microsoft Networks is the native remote file system included in Windows Server 2003, Windows XP, and Windows 2000. Microsoft Networks provides remote access to files as well as access to remote printers and plotters. Microsoft Networks was called LAN Manager Network in earlier versions of Windows.

Microsoft also includes support for several other remote file systems on Windows:

-   NetWare Core Protocol (NCP)

-   WebDAV (file access that uses remote web servers)

-   AppleTalk file and printer sharing (supports connections from Macintosh clients to systems running Windows Server 2003 and Windows 2000 Server)

-   Network File System (NFS)

-   IBM mainframe VSAM and AS/400 file access, included with Microsoft Host Integration Server 2000

**Note**  In versions of the Windows operating system prior to Windows Server 2003 R2, you could obtain NFS by installing Microsoft Services for UNIX. With Windows Server 2003 R2 and later versions of the Windows operating system, NFS is included as an optional Windows component.

 

Remote file systems are implemented by a collection of software components. The number and complexity of the software components required varies based on the design and complexity of the remote file system.

Software on the client system provides remote file and resource access. This client software functions as a "network redirector" forwarding local calls for file operations to some remote server. This network redirector makes the remote resources appear as if they are local.

Software on the server system implements the remote file server operations that access local file storage or resources on the server. Requests are received from client network redirectors that are processed on the file server, and the responses are sent back to the client.

A system can act as both a client to some systems and as a server to other clients. So, it is common to find both client and server software running on a single system.

This section contains the following topic:

[Components of a Remote File System](components-of-a-remote-file-system.md)

 

 




