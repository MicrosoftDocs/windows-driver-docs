---
title: Creating Components for Using a SAN
description: Creating Components for Using a SAN
ms.assetid: b7405eda-734e-43f0-b0fe-747a06766291
keywords:
- system area networks WDK , creating components
- SAN WDK , creating components
- transport drivers WDK SANs
- data transfers WDK SANs
- transferring data WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Components for Using a SAN





Windows Sockets applications can benefit from using a system area network (SAN). To use a SAN, these applications must have a SAN service provider DLL and a proxy driver for that DLL.

To use a specific SAN to transfer data, you also need a reliable transport for that SAN. If a reliable transport is not fully implemented in the SAN NIC hardware, you need a transport driver for the SAN. If required, a SAN transport driver is specified by the SAN NIC vendor and communicates with its overlying SAN proxy driver and underlying SAN NIC through private interfaces.

For information about implementing a SAN service provider DLL and its proxy driver, see [Windows Sockets Direct](windows-sockets-direct.md). Note, however, that this section does not specify how to write a SAN transport driver.

You need an NDIS miniport driver to transfer data that must flow over networks other than your specific SAN such as Ethernet, ATM, or another SAN. TCP/IP uses the NDIS miniport driver to send data both to the SAN NIC and over such networks.

For information about implementing miniport and transport drivers, see [*Miniport Drivers*](https://msdn.microsoft.com/library/windows/hardware/ff556308#wdkgloss-miniport-driver) and [TDI Transports and Their Clients](https://msdn.microsoft.com/library/windows/hardware/ff565587).

 

 





