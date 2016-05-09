---
title: Introduction to Remote File Systems
description: Introduction to Remote File Systems
ms.assetid: 24fe7b8e-b956-4c27-be12-8317e4f35ba6
keywords: ["network redirectors WDK , remote file systems", "redirector drivers WDK , remote file systems", "remote file systems WDK", "file system drivers WDK , remote file systems"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Introduction%20to%20Remote%20File%20Systems%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




