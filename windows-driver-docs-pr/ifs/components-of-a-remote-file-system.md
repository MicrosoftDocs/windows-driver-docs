---
title: Components of a Remote File System
author: windows-driver-content
description: Components of a Remote File System
ms.assetid: b2cd153a-5bcc-4670-8542-afa55e14727a
keywords: ["network redirectors WDK , remote file systems", "redirector drivers WDK , remote file systems", "remote file systems WDK", "file system drivers WDK , remote file systems"]
---

# Components of a Remote File System


## <span id="ddk_components_of_a_remote_file_system_if"></span><span id="DDK_COMPONENTS_OF_A_REMOTE_FILE_SYSTEM_IF"></span>


The following basic elements are required to implement a remote file system:

-   Network redirector software installed on the client.

-   A well-defined transport protocol used for communication.

-   File server software installed on the server.

For example, the Microsoft Network remote file system is implemented as follows:

-   The client for Microsoft Networks software provides the client network redirector components.

-   The Common Internet File System (CIFS), which is also called the Server Message Block (SMB) protocol, defines the network transport protocol used for communication.

-   The LAN Manager Server (sometimes called SMB Server) provides the file server service.

The network redirector software installed on the client consists of several software components, some that operate in user-mode and some that operate in kernel-mode.

The following sections discuss concepts that are important to developers of remote file systems on Windows Server 2003, Windows XP, and Windows 2000. The following topics are discussed:

[Introduction to Network Redirectors](introduction-to-network-redirectors.md)

[Kernel Network Redirector Driver Components](kernel-network-redirector-driver-components.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Components%20of%20a%20Remote%20File%20System%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


