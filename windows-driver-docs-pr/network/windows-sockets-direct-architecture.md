---
title: Windows Sockets Direct Architecture
description: Windows Sockets Direct Architecture
ms.assetid: 2f6ac4a7-76fe-45b4-8b5b-3a5f1d5c0553
keywords:
- Windows Sockets Direct WDK , architecture
- TCP/IP WDK SANs
- NIC components WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Sockets Direct Architecture





Windows Sockets Direct provides a high-speed, high-performance connection between two network nodes on the same system area network (SAN) by mapping a SAN transport interface directly into an application process. This SAN connection enables user-mode processes to perform direct input and output (I/O) without copying across the user-kernel boundary.

The SAN architecture figure in [Introduction to System Area Networks](introduction-to-system-area-networks.md) shows how Windows Sockets Direct provides a SAN connection. The shaded areas in the figure represent components that a SAN NIC vendor must supply to enable use of a SAN.

The following paragraphs describe the components that appear in the figure.

### Supplied Components for SAN Network Interface Controllers

Each SAN network interface controller (NIC) uses the following software components to provide support for NDIS and for Windows Sockets Direct.

-   An NDIS miniport driver for a SAN NIC provides support for NDIS so that it can communicate with Windows Sockets applications using a standard TCP/IP protocol driver. This NDIS miniport driver supports standard media types such as Ethernet or ATM.

-   The SAN service provider DLL and its associated proxy driver provide support for Windows Sockets Direct. These Windows Sockets Direct components export the native transport semantics of an interconnect for the SAN to Windows Sockets applications. These semantics can include, for example, address family and message orientation.

The SAN NIC vendor supplies the NDIS miniport driver and Windows Sockets Direct components. The SAN NIC vendor might also supply a SAN transport driver if transport service is not implemented fully in the NIC. The proxy driver for a SAN service provider DLL and possibly a SAN transport driver are contained either in the NDIS miniport driver or in separate drivers, at the discretion of the SAN NIC vendor.

### Windows Sockets Switch Components

The Windows Sockets switch is an operating system-supplied component of Windows Sockets Direct. The switch is a Windows Sockets service provider that is layered on top of TCP/IP and SAN service providers. The Windows operating system inserts the switch between the Windows Sockets interface and the other service providers. For clarity, the switch appears in the figure as a separate entity. However, the switch and the base TCP/IP service provider are actually implemented in the same DLL. The switch performs the following actions:

-   Makes the installed collection of SAN service providers and the standard TCP/IP provider look like a single provider to Windows Sockets applications.

-   Chooses, on a per-connection basis, whether to use a native SAN service provider or the standard TCP/IP provider to service an application socket.

-   Emulates TCP/IP semantics when using a native SAN service provider.

The top and bottom interfaces of the switch conform to the Windows Sockets Service Provider Interface (SPI). The switch's bottom interface uses extensions to the Windows Sockets SPI to take advantage of a SAN's capabilities. Those extensions are described in [Windows Sockets SPI Extensions for SANs](windows-sockets-spi-extensions-for-sans.md) and fully documented in the [Windows Sockets Direct Reference](https://msdn.microsoft.com/library/windows/hardware/ff565857).

The switch manages application access to all networks. A computer can contain multiple SAN NICs from multiple vendors, as well as one or more LAN and WAN NICs, such as a LAN NIC that supports an Ethernet network. The switch manages application access to all networks associated with these NICs transparently.

### TCP/IP Functions

As with any NIC exposed through NDIS, the TCP/IP protocol driver assigns one or more IP addresses to each SAN NIC. The Windows Sockets switch and SAN service providers determine these assignments, as described in [Receiving and Translating NIC Addresses](receiving-and-translating-nic-addresses.md). The switch uses this IP address information to determine which SAN service provider to use for a given socket connection. SAN service providers use this IP address information to translate IP addresses into native SAN addresses.

The switch works closely with the standard base TCP/IP service provider to obtain functionality that SAN service providers do not support. The TCP/IP service provider supports listening for connections on multiple providers and synchronization across multiple providers.

The TCP/IP service provider also handles all communication over standard LAN and WAN interconnects, raw IP sockets, all UDP sockets, and connections between subnets.

 

 





