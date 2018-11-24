---
title: Translating to a SAN Native Address
description: Translating to a SAN Native Address
ms.assetid: 959c66f2-4801-47d5-9e80-f18f17057e23
keywords:
- proxy drivers WDK SANs , native address translations
- SAN proxy drivers WDK , native address translations
- native address translations WDK SANs
- translating native addresss WDK SANs
- AF_INET addresses WDK SANs
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Translating to a SAN Native Address





The Windows Sockets switch always uses the [WSK address families](https://msdn.microsoft.com/library/windows/hardware/ff571151) to interact with a SAN service provider, not the SAN's native address family. Therefore, a proxy driver for a SAN service provider must translate between WSK address families and native addresses accordingly.

A proxy driver uses TDI Plug and Play (PnP) notifications to maintain the list of IP addresses assigned to each NIC under its control, as described in [Registering for SAN NIC Notifications](registering-for-san-nic-notifications.md). The proxy driver uses this list to translate between native SAN addresses and IP addresses.

The proxy driver receives requests from its SAN service provider that contain IP addresses. These requests include, for example, the request to bind to a specific NIC and the request to connect to a remote peer. The proxy driver must translate to native SAN addresses to complete these requests. The proxy driver also receives incoming connection requests from remote peers that contain SAN native addresses of those remote peers. The proxy driver must translate to the IP addresses of those remote peers to complete these requests.

**Note**  TDI will not be supported in Microsoft Windows versions after Windows Vista. Use [Windows Filtering Platform](https://msdn.microsoft.com/library/windows/hardware/ff571067) or [Winsock Kernel](https://msdn.microsoft.com/library/windows/hardware/ff571083) instead.

 

 

 





