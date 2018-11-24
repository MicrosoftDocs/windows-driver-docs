---
title: TCP/IP Offload
description: TCP/IP Offload
ms.assetid: 1f074ce5-2614-47a5-9ee0-a5e43f05273d
keywords:
- network drivers WDK , TCP/IP offload
- TCP/IP offload WDK networking
- offload WDK TCP/IP transport
- TCP/IP offload WDK networking , about TCP/IP offload
- offload WDK TCP/IP transport , about TCP/IP offload
- task offload WDK TCP/IP transport
- connection offload WDK TCP/IP transport
- packets WDK networking , TCP/IP offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# TCP/IP Offload





To increase its performance, the Microsoft TCP/IP transport can offload tasks or connections to a NIC that has the appropriate TCP/IP-offload capabilities.

Beginning with Windows Vista, the Windows operating system supports the following TCP/IP offload services:

-   Checksum tasks

-   Applications Internet protocol security (IPsec) offload version 1

-   IPsec offload version 2
    - \[The IPsec Task Offload feature is deprecated and should not be used.\]

-   Large send offload version 1

-   Large send offload version 2

-   Connection offload

The TCP/IP transport that is provided beginning with Windows Vista supports TCP/IP offload services for both IPv4 and IPv6 packets.

NDIS 6.0 and later miniport drivers support TCP/IP offload services in a multiple-protocol driver environment. Multiple NDIS 6.0 and later protocol drivers that are bound to a TCP/IP offload-capable miniport adapter can configure TCP/IP offload services.

This section includes:

-   [Accessing TCP/IP Offload NET\_BUFFER\_LIST Information](accessing-tcp-ip-offload-net-buffer-list-information.md)
-   [Using the TCP/IP Offload Administrator Interface](using-the-tcp-ip-offload-administrator-interface.md)
-   [Security Guidelines for Offload-Capable Miniport Drivers](security-guidelines-for-offload-capable-miniport-drivers.md)
-   [TCP/IP Task Offload](task-offload.md)
-   [Connection Offload](connection-offload.md)

 

 





