---
title: Basic Architecture of a Network Redirector
description: Basic Architecture of a Network Redirector
ms.assetid: 60a7c79d-b89f-4c8b-9619-bd48c9e1efac
keywords:
- network redirectors WDK , architecture
- redirector drivers WDK , architecture
- TDI drivers WDK file systems
- Transport Driver Interface WDK file systems
- DLLs WDK file systems
- SYS WDK file systems
- kernel-mode file system drivers WDK file systems
- user-mode DLLs WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Basic Architecture of a Network Redirector


## <span id="ddk_basic_architecture_of_a_network_redirector_if"></span><span id="DDK_BASIC_ARCHITECTURE_OF_A_NETWORK_REDIRECTOR_IF"></span>


The following basic software components are required as part of a network redirector:

-   A kernel-mode file system device driver (SYS) that provides the network redirector functions.

-   A user-mode dynamic link library (DLL) that provides access for client user-applications to the Network Provider interface for non-file operations and enables communication with the kernel-mode file system driver providing the network redirector functions.

The kernel-mode file system driver component of the network redirector interacts with the Object Manager, Cache Manager, Memory Manager, I/O System, and other kernel systems in order to integrate remote file access into the operating system. The driver receives requests from a client application through the I/O Manager for remote file access and sends the necessary information over the network to the remote file server. The driver also receives the responses from the remote file server and passes the information back to the client application through the I/O Manager. The network redirector driver must also implement the network protocol used for remote access or provide calls to another kernel driver, user-mode application, or service that implements this network protocol or communication mechanism. The most common method to implement this network communication is to use the Transport Driver Interface (TDI) to call an existing network protocol stack (TCP/IP, for example). The network protocol stack then communicates at the bottom layer using the Network Driver Interface Specification (NDIS) with the network interface card. It is also possible to use an application-specific interface for this communication mechanism.

The user-mode DLL receives special requests from the client through the Network Provider interface that are not file operations. These requests can be used for determining capabilities of the network provider, enumerating remote network resources, logging on to a remote network, changing network passwords, connecting with remote servers, mounting remote network shares or resources, and disconnecting from remote shares. The user-mode DLL implements the equivalent of the WNet user-mode APIs for accessing the remote file system. This DLL then communicates with the kernel-mode network redirector driver through special IOCTL calls to fulfill these client requests. For example, this DLL is called by Windows Explorer when enumerating network resources (browsing the Network Neighborhood) or when connecting to remote file shares and resources (printers). This DLL is also called from the NET command-line tool to view remote resources (**net view** \\\\*computername*) and connect or disconnect to remote file shares (**net use**). This DLL can also be called by custom applications using the exposed WNet APIs of the Multiple Provider Router (MPR).

A network redirector may also need several other components:

-   A service application may be needed to act as an intermediary between the user-mode DLL and the kernel-mode driver if any global data tables need to be securely stored in the user-mode DLL. Since the user-mode DLL is instantiated in the process space of the client application, there is no way to secure any internal data tables that need to be global across all client applications. It is possible to have per-client data that is private to each client application when connecting to the user-mode network provider DLL, but not global data. A service application (an .exe file) can be used as the intermediary between the user-mode DLL and the kernel driver where global data tables are stored. For example, Microsoft Networks uses the Workstation service built into the svchost.exe to store a global table of "net use" connections and act as an intermediary to the kernel-mode driver. In the case of Microsoft Networks, the user-mode DLL, ntlanman.dll, calls the Workstation service in svchost.exe, which then calls the kernel-mode driver, mrxsmb.sys, which provides the network redirector functions.

-   A system for installing and properly registering the network redirector components in the system, which must include creating any necessary registry entries. There should also be a method to uninstall the network redirector if the software is no longer needed. It is possible to use the Microsoft Systems Installer (MSI) or Windows INF script files to perform this setup. This installation and setup could also be accomplished using a custom installation program.

-   A custom kernel-mode TDI driver needs to be installed if the network redirector uses a network protocol not included in the operating system (Xerox Network Services, for example). The new TDI driver would need to be installed that implements the network protocol to use for communication. The kernel-mode network redirector driver connects to the upper edge of the custom TDI driver. The custom TDI driver would in turn communicate at its lower edge with an NDIS driver.

    Note that if the network redirector uses the TCP/IP protocol, a custom TDI driver is not required. The network redirector would connect to the upper edge of the TCP/IP protocol TDI driver in this case.

-   An administration tool is occasionally needed to provide access from user-mode to the kernel-mode driver for special configuration, diagnostics, and administration. This tool can also be used to enable or disable tracing and logging for troubleshooting problems. The tool would communicate with the kernel driver by using various custom private IOCTLs. This tool might also provide access to the Service Control Manager (SCM) to manage an intermediary service where global data is stored securely for the user-mode Network Provider DLL.

**Note**   TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571068) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

 

 




