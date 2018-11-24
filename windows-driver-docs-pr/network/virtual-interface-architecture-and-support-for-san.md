---
title: Virtual Interface Architecture and Support for SAN
description: Virtual Interface Architecture and Support for SAN
ms.assetid: 83d28f33-7354-4f59-8b01-4842286f12fb
keywords:
- system area networks WDK , VI architecture
- SAN WDK , VI architecture
- VI architecture WDK SANs
- Virtual Interface architecture WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Interface Architecture and Support for SAN





The Virtual Interface (VI) architecture, proposed by Compaq, Intel, and Microsoft, is a design for an interface between a SAN NIC and a host computer system. This architecture represents only one aspect of design with regard to system area networks (SAN). There are alternate designs that share the same fundamental characteristics.

The VI architecture defines a set of capabilities and characteristics for SAN interconnects. For example, the VI architecture includes support for remote direct memory access (RDMA) operations. The VI architecture also describes specific mechanisms for interacting with a SAN NIC to manage endpoints and connections, and to process data transfer requests.

The Windows Sockets switch works with a broader class of SAN interconnects beyond those that use the VI architecture. SAN extensions to the Windows Sockets service provider interface (SPI) shield the switch from the hardware interface for a particular SAN NIC. That hardware interface is encapsulated within a SAN service provider DLL and its kernel-mode proxy driver. These components are supplied by a SAN vendor. For more information about SAN extensions, see [Windows Sockets SPI Extensions for SANs](windows-sockets-spi-extensions-for-sans.md).

 

 





