---
title: Using a SAN with Windows Sockets Applications
description: Using a SAN with Windows Sockets Applications
ms.assetid: 140505dd-2e3c-48b2-94c0-911ea460068c
keywords:
- system area networks WDK , Windows Sockets applications
- SAN WDK , Windows Sockets applications
- Windows Sockets applications WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using a SAN with Windows Sockets Applications





Windows Sockets applications can benefit from using a system area network (SAN). These applications can use a SAN to transfer data in bulk form and to drop data directly onto the SAN network, without copying across the user-kernel boundary, using a technology called [Windows Sockets Direct](windows-sockets-direct.md). Windows Sockets Direct lets these applications use a SAN transparently.

For each Windows Sockets application, Windows Sockets Direct can either:

-   Route data traffic that flows over a SAN directly to the SAN.

    The system-supplied Windows Sockets switch component of Windows Sockets Direct routes data traffic for a SAN that originates from a Windows Sockets application directly to the SAN NIC to be transferred over the SAN network. The switch uses that SAN's particular Windows Sockets service provider to transfer data.

-   Route data traffic that flows over other networks through TCP/IP.

    To route data traffic that is not for a specific SAN from a Windows Sockets application, the switch must use the TCP/IP service provider. Non-SAN-specific data traffic includes, for example, datagrams, multicast, and connections that must be routed. Non-SAN-specific data traffic is then routed through TCP/IP and the NDIS miniport driver to the SAN NIC.

 

 





