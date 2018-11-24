---
title: Components of a Remote File System
description: Components of a Remote File System
ms.assetid: b2cd153a-5bcc-4670-8542-afa55e14727a
keywords:
- network redirectors WDK , remote file systems
- redirector drivers WDK , remote file systems
- remote file systems WDK
- file system drivers WDK , remote file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




