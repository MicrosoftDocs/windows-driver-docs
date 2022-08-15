---
title: Learning About Protocol Drivers
description: Learning About Protocol Drivers
keywords:
- protocol drivers WDK networking , connectionless lower edge
- NDIS protocol drivers WDK , connectionless lower edge
- protocol drivers WDK networking , connection-oriented clients and providers
- NDIS protocol drivers WDK , connection-oriented clients and providers
- protocol drivers WDK networking , Winsock support
- NDIS protocol drivers WDK , Winsock support
- Winsock Kernel WDK networking , protocol driver support for Winsock
- network drivers WDK , types
ms.date: 04/20/2017
---

# Learning About Protocol Drivers





You can write a protocol driver that has either a connectionless or a connection-oriented lower edge. In addition, your protocol driver can provide Winsock support. The following list describes which sections of the WDK documentation you should read, depending on the type of protocol driver that you are writing:

<a href="" id="protocol-drivers-that-have-a-connectionless-lower-edge"></a>**Protocol drivers that have a connectionless lower edge**  
If you are writing a protocol driver whose lower edge provides an interface to connectionless miniport drivers, read:

-   [NDIS Protocol Drivers](./roadmap-for-developing-ndis-protocol-drivers.md)

<a href="" id="protocol-drivers-that-are-connection-oriented-clients-or-that-are-connection-oriented-providers-of--------call-manager-services"></a>**Protocol drivers that are connection-oriented clients or that are connection-oriented providers of call manager services**  
If you are writing a connection-oriented client, which provides an interface to connection-oriented miniport drivers, or if you are writing a connection-oriented call manager, read:

-   [NDIS Protocol Drivers](./roadmap-for-developing-ndis-protocol-drivers.md)

-   [Connection-Oriented NDIS](connection-oriented-ndis.md)

<a href="" id="protocol-drivers-that-have-winsock-support"></a>**Protocol drivers that have Winsock support**  
If you are writing a protocol that provides Winsock support, read:

-   [NDIS Protocol Drivers](./roadmap-for-developing-ndis-protocol-drivers.md)

-   [Transport Helper DLLs for Windows Sockets](/previous-versions/windows/hardware/network/ff565691(v=vs.85))

 

